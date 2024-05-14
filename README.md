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
 
 Download "ferrari" image, limit set 5.
 ```
 python scraper.py --kw ferrari --lm 5
 ```

## License

```
MIT License

Copyright (c) 2024 Jsnn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

