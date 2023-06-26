import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = Options()
options.page_load_strategy = "normal"
options.add_argument("--headless=new")
# Path to your local chrome driver
chrome_driver_path = "C:/Users/__YOUR_USER__/DevTools/chromedriver.exe"


class Scraper:
    def __init__(self, link, type_of_search):
        self.link = link
        self.type_of_search = type_of_search
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        self.pages_num = 0
        self.addresses = []
        self.square_footages = []
        self.prices = []
        self.links = []
        self.rents = []

    def scrape(self):
        self.driver.get(self.link)
        body = self.driver.find_element(By.TAG_NAME, "body")
        # Simulates scroll down to display all offers
        body.send_keys(Keys.ARROW_DOWN)
        # Gives enough time to load everything, you can experiment with that value
        time.sleep(5)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        offers_num = int(soup.find(name="span", class_="css-19fwpg e17mqyjp2").text)
        self.pages_num = offers_num // 72
        for i in range(0, self.pages_num + 1):
            if i != 0:
                self.driver.get(self.link + f"&page={i+1}")
                body = self.driver.find_element(By.TAG_NAME, "body")
                body.send_keys(Keys.ARROW_DOWN)
                # Gives enough time to load everything, you can experiment with that value
                time.sleep(2)
                page_source = self.driver.page_source
                soup = BeautifulSoup(page_source, "html.parser")
            offers = soup.find_all(name="li", class_="css-iq9jxc e1n6ljqa1")
            for offer in offers:
                link = offer.find(name="a", class_="css-1up0y1q e1n6ljqa3").get("href")
                link = f"https://www.otodom.pl{link}"
                self.links.append(link)
                address = offer.find(name="p", class_="css-14aokuk e1ualqfi4").text
                self.addresses.append(address)
                try:
                    if self.type_of_search == "inwestycja" or self.type_of_search == "dzialka" or self.type_of_search == "lokal" or self.type_of_search == "haleimagazyny" or self.type_of_search == "garaz":
                        square_footage = offer.find_all(name="span", class_="css-1on0450 ei6hyam2")[1].text
                    else:
                        square_footage = float(offer.find_all(name="span", class_="css-1on0450 ei6hyam2")[2].text.split(" ")[0])
                except IndexError:
                    square_footage = "None"
                self.square_footages.append(square_footage)
                if self.type_of_search == "inwestycja":
                    price = offer.find_all(name="span", class_="css-1on0450 ei6hyam2")[0].text
                else:
                    price = offer.find_all(name="span", class_="css-1on0450 ei6hyam2")[0].text
                    price = price.replace(u'\xa0', "")
                self.prices.append(price)
                if self.type_of_search == "mieszkanie" or self.type_of_search == "kawalerka":
                    rent = offer.find(name="span", class_="css-5qfobm ei6hyam4").text.strip("+ ")

                else:
                    rent = "None"
                self.rents.append(rent)

        return [self.addresses, self.square_footages, self.prices, self.links, self.rents]
