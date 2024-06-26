import requests
import os
import argparse
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from pexels_api import API
from pinscrape import pinscrape


class Scraper:

    def __init__(self, key, lmt):
        env_var = dotenv_values(".env")
        self.pexels_api_key = env_var["PEXELS_API_KEY"]
        self.key = key
        self.limit = lmt

    def get_parser():
        parser = argparse.ArgumentParser(description="--- Web-image-scraper usage ---")
        parser.add_argument("--kw", type=str, help="Keyword of scrape image")
        parser.add_argument("--lm", type=int, default=1, help="Download limit")
        return parser

    # working, using beautiful soup to scrape and download images
    def download_unsplash_images(self):
        site = "Unsplash"
        url = f"https://unsplash.com/s/photos/{self.key}/"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")

            images = soup.find_all("img", {"class": "tB6UZ a5VGX"}, limit=self.limit)

            images_links = [img.get("src") for img in images]

            print("Downloading Unsplash images...")
            for ind, link in enumerate(images_links):
                if not os.path.exists(f"Download/"):
                    os.mkdir(f"Download/")

                img = requests.get(link)

                with open(
                    f"Download/from" + site + self.key + str(ind + 1) + ".jpg",
                    "wb",
                ) as file:
                    file.write(img.content)
            print("Complete")
        else:
            print("responding error")

    # working, using official api key and pexels_api module
    def download_pexels_images(self, pages=1, img_per_page=1):
        site = "Pexels"
        api_key = self.pexels_api_key
        api = API(api_key)

        api.search(self.key, img_per_page, pages)

        images_links = api.get_entries()

        print("Downloading Pexels images...")
        for ind, link in enumerate(images_links):
            # if not os.path.exists(f"Download/From {site} of {key} Images"):
            #     os.mkdir(f"Download/From {site} of {key} Images")

            if not os.path.exists(f"Download/"):
                os.mkdir(f"Download/")

            img = requests.get(link.original)

            with open(
                f"Download/from" + site + self.key + str(ind + 1) + ".jpg",
                "wb",
            ) as file:
                file.write(img.content)
        print("Complete")

    # working, using pinscrape to download images
    def download_pinterest_images(self):
        site = "Pinterest"

        print("Downloading Pinterest images...")
        pinscrape.scraper.scrape(
            key=self.key,
            output_folder=f"Download/",
            max_images=self.limit,
        )
        print("Complete")


def main():
    try:
        # testing parser function
        args = Scraper.get_parser().parse_args()
        if args.kw:
            key = args.kw
        else:
            key = input("Which type of images you want to download: ")

        if args.lm:
            download_limit = args.lm
        else:
            download_limit = int(input("How many images you want to download: "))

        if download_limit > 0:
            scraper = Scraper(key, download_limit)
            scraper.download_unsplash_images()
            scraper.download_pexels_images()
            scraper.download_pinterest_images()
        else:
            raise ValueError("Download limit error")
    except ValueError as e:
        print(f"An error occurred: {e}. Please enter a valid number.")


if __name__ == "__main__":
    main()
