# Web-Image-Scraper
## Introduction

 A simple image scraper developed by requests, bs4, dotenv etc.
 Scraping Pexels/Unsplash/Pinterest images.

 Pinterest section using [pinscrape](https://github.com/iamatulsingh/pinscrape) by [iamatulsingh](https://github.com/iamatulsingh)

 ## Requirements

 First, use `pip install -r requirements.txt` to install require packages from requirements.txt file.

  Before using Pexels section, you need to get the API-key of Pexels from official website, then create an .env file, save as the format down below.
 ```
 PEXELS_API_KEY = "YOUR_API_KEY"
 ```

 ## How to use
 Using CLI to interact with scraper, or you can run `scraper.py` straightly and it will ask you variables like the keyword, download limit.
 ```
usage: scraper.py [-h] [--kw KW] [--lm LM]

--- Web-image-scraper usage ---

options:
  -h, --help  show this help message and exit
  --kw KW     Keyword of scrape image
  --lm LM     Download limit
 ```

 ### Basic usage
 
 Download "ferrari" image, limit set 5
 ```
 python scraper.py --kw ferrari --lm 5
 ```

## License

```
```

