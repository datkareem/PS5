#name: Kareem T
#date: 11/28/2020
#desc: chromedriver web-scraping bot notifying user of PS5 availability in their area. Input path to chromedriver and mp3 file. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import os

chromedriver = "C://x/chromedriver.exe"
user_path = 'C://x.mp3'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chromedriver, options=options)

stores = ["target", "bestbuy", "walmart", "amazon", "sony", "gamestop"]
links = {"target":("https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596#", '//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div')
        ,"bestbuy":("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161",'//*[@id="fulfillment-add-to-cart-button-1521bb08-00e4-4fe2-99ca-cc255ffc41b2"]/div/div/div/button')
        ,"walmart":("https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815",'//*[@id="product-overview"]/div/div[3]/div/div[2]/div[1]/section/div[1]/div[2]/div/div/div/span')
        ,"amazon":("https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62",'//*[@id="availability"]/span')
        ,"sony":("https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817",'/html/body/div[1]/div/div[3]/producthero-component/div/div/div[3]/producthero-info/div/div[4]/div[2]')
        ,"gamestop":("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html?condition=New",'//*[@id="primary-details"]/div[4]/div[9]/div[2]/div[1]/label/div/div[5]/span[2]')}

def init_stores():
    i = 0
    driver.get(links[stores[0]][0])
    for store in stores[1:]:
        driver.execute_script(f'window.open("{links[store][0]}", "_blank")')
        i+=1
        driver.switch_to.window(driver.window_handles[i])

def check_stores():
    i = 0
    driver.switch_to.window(driver.window_handles[0])
    for store in stores:
        driver.get(links[store][0])
        time.sleep(5)
        try:
            target = driver.find_elements_by_xpath(f'{links[store][1]}')
            print(f"{store}\'s button: {target[0].text}")
            if "out" not in target[0].text and "Out" not in target[0].text and "unavailable" not in target[0].text:
                print(f'Sale @ {store}! Goto: {links[store][0]}')
                os.startfile('')
        except IndexError:
            print(f"Could not find {store}'s identifier")
        finally:
            if i + 1 < len(stores): driver.switch_to.window(driver.window_handles[i+1])
            i+=1

def test_id(store):
    driver.get(links[store][0])
    time.sleep(5)
    try:
        target = driver.find_elements_by_xpath(f'{links[store][1]}')
        print(f"{store}\'s button: {target[0].text}")
        if "out" in target[0].text or "Out" in target[0].text or "unavailable" in target[0].text:
            print(f'WORKING @ {store}! Goto: {links[store][0]}')
    except IndexError:
        print(f"Could not find {store}'s identifier")
        
def test_suite():
    for store in stores:
        test_id(store)

def main2():
    test_suite()

def main():
    bot = True
    init_stores()
    while(bot):
        check_stores()
        time.sleep(5)

if __name__ == "__main__":
    main()