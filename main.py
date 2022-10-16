import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

def emailAgent():
    try:
        preferences = browser.find_element(By.XPATH, "//div[@data-testid='overview']")

        mfpreferences = preferences.get_attribute('innerHTML')
        if 'Male / Female' in mfpreferences or 'Male' in mfpreferences:
            time.sleep(3)
            id = int(browser.current_url.split('/')[-1])
            if id not in idsForAppliedAds:

                # Click the Email Agent Button
                e = browser.find_element(By.XPATH, '//button[@data-testid="message-btn"]')
                e.click()

                time.sleep(3)

                # Fill-out Form 
                f = browser.find_elements(By.XPATH, '//input')
                f[1].send_keys('Nikhil Balbadri')
                f[2].send_keys('nikhilbalbadri@gmail.com')
                f[3].send_keys('0894731162')

                time.sleep(3)
                # Multiline text entry require (SHIFT + ENTER) for a newline.
                t = browser.find_element(By.NAME, 'message')
                t.send_keys('Hi there, I hope you are doing well. This is Nikhil Balbadri currently in my late 20’s. It’s been 3 years for me in Ireland and currently working as a Software Developer at BoyleSports and looking for a long-term place to shift to in Dublin. The letting caught my interest and would like to drop in my application for the same. I am an easy-going guy and get along well. I clean up after myself and respect others’ space in the house. I do like occasional craic with the housemates, well what’s fun without that? I have positive references from my previous landlords and fellow housemates. I am ok with viewings on video call anytime, don’t mind in person as well, but we will have to schedule it. I just have a few basic questions, Is Wi-Fi included in the rent? How much do the utility bills come up for a month or two? Do we have a weekly cleaning service in the common area? Nearest gym to the house? I don’t have a motorcycle with me right now, but I am planning for it so what options do I have for parking? Feel free to get in touch with any queries you have. I would be happy to answer them. Looking forward to hearing from you. Thank you, Nikhil Balbadri')
    
                time.sleep(3)

                #Send form
                e = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
                e.click()

                time.sleep(5)

                try:
                    g = browser.find_element(By.XPATH, '//button[@class="styles__CloseContainer-qea560-4 cbFYJA"]')
                    g.click()
                    idsForAppliedAds.append(id)

                except NoSuchElementException:
                    idsForAppliedAds.append(id)

                time.sleep(1)
        time.sleep(3)
        browser.execute_script("window.history.go(-1)")
    except:
        time.sleep(3)
        browser.execute_script("window.history.go(-1)")

def loopFunction():
    try:
        for x in range(ppp+1):
            if x>0:
                time.sleep(4)
                a = browser.find_element(By.XPATH,'//button[@aria-label="Next >"]')
                a.click()
                time.sleep(2)    
            f = browser.find_elements(By.XPATH, "//ul[@data-testid='results']/li")
            for x in range(len(f)-1):
                time.sleep(4)
                f = browser.find_elements(By.XPATH, "//ul[@data-testid='results']/li")
                f[x].click()
                time.sleep(2)
                emailAgent()
                time.sleep(2)
    except IndexError:
        print("Error in loop")

def hosting():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usuage")
    chrome_options.add_argument("--no-sandbox")
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome(options=chrome_options)
    return browser
 
while True:

    data = open(r'IdsforAppliedAds.json')
    idsForAppliedAds = json.load(data)
    data.close()

    browser = hosting()
    #browser = webdriver.Chrome("C:/chromedriver/chromedriver")
    browser.maximize_window()
    browser.get('https://www.daft.ie/auth/authenticate')

    time.sleep(2)

    username_input = browser.find_element(By.ID,'username')
    username_input.send_keys('nikhilbalbadri@gmail.com')

    time.sleep(2)

    password_input = browser.find_element(By.ID,'password')
    password_input.send_keys('Manunited1994$')

    time.sleep(2)

    login_btn = browser.find_element(By.CSS_SELECTOR,'input[type="submit"]')
    login_btn.click()

    time.sleep(2)

    acceptcookies_btn = browser.find_element(By.XPATH, '//button[@data-tracking="cc-accept"]')
    acceptcookies_btn.click()


    browser.get('https://www.daft.ie/sharing/ireland?rentalPrice_to=1000&ownerOccupied=false&firstPublishDate_from=now-3d%2Fd&sort=publishDateDesc&location=dublin-city&location=swords-dublin')

    time.sleep(2)


    pagination = browser.find_element(By.XPATH, "//p[@data-testid='pagination-results']").get_attribute("innerHTML")
    totalAds = int(pagination.split()[-1])
    ppp = (totalAds)//20
               
    loopFunction()

    a_file = open("IdsforAppliedAds.json", "w")
    json.dump(idsForAppliedAds, a_file)
    a_file.close()

    browser.quit()

    time.sleep(600)
