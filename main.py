import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EcosiaSearch():
    # Recommended wait: 2 seconds
    def __init__(self, wait):
        self.bot = webdriver.Chrome()
        self.wait = wait
        self.search_list = ["facebook", "youtube", "amazon", "gmail", "google", "ebay", 
        "yahoo", "weather", "craigslist", "yahoo mail", "google maps", "walmart", 
        "netflix", "google translate", "google docs", "news", "translate", "home depot", 
        "cnn", "hotmail", "fox news", "facebook login", "calculator", "google drive", 
        "maps", " msn", "usps tracking", "lowes", "paypal", "google classroom", "target", 
        "instagram", "bank of america", "espn", "aol mail", "wells fargo", "zillow", 
        "pinterest", "entertainment", "twitter", "indeed", "you tube", "best buy", "speed test", 
        "trump", "roblox", "linkedin", "youtube tp mp3", "amazon prime", "sports", "nba", 
        "capital one", "chase", "aol", "costco", "usp tracking", "hulu", "reddit", "traductor", 
        "kohls", "pandora", "bing", "america airlines",  "etsy", "finance", "usps", "twitch", 
        "airbnb", "pizza hut", "nfl", "google flights", "dominos", "fb", "spotify", "macys", 
        "google scholar", "expedia", "123movies", "fedex tracking", "verizon", "wells fargo login", 
        "you", "united airlines", "discord", "facebook log in", "google news", "bed bath and beyond", 
        "outlook", "restaurants near me", "walgreens", "credit karma", "harbor freight", "gamestop", 
        "solitaire", "xfinity", "mapquest", "southwest", "ikea", "timer", "joke"]
    
    def search(self):
        bot = self.bot
        wait = self.wait
        search_list = self.search_list
        bot.get('https://www.ecosia.org/?c=en')
        x = None
        Flag = True
        while Flag:
            y = x
            x = random.randint(0,99)
            if y == x:
                x = random.randint(0,99)
                y =x
            time.sleep(wait)
            bot.get('https://www.ecosia.org/search?q=' + search_list[x])
            time.sleep(wait)
    
bot = EcosiaSearch(2)
bot.search()