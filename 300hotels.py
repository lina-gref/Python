#this script was written a while ago (in 2019 I guess), using one of the prev. versions of Python and chrome driver.
#I worked in a company which provided booking for business tourism. It included working with hotels and payments. My team worked on API, hotel database and backoffice.

#the urls, the names of the entities, API method elements were changed due to the NDA and the contract I had with my former employer.
#but it won't affect the understanding of the code.
#I had a strict task: to make a script which could create 300 entities with several connected entities ASAP. This script worked and helped my former team to save a lot of time for further testing.



import requests
import re
from selenium import webdriver
from selenium.webdriver.common.alert import Alert 
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
#standard settings of selenium + python for further actions

driver = webdriver.Chrome()
actions = ActionChains(driver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
driver = webdriver.Chrome(options=chrome_options)
#I didn't like the pop-up in Chrome browser alarming about the browser being controlled by a program. This part is optional.

def loginpass ():
    #a simple log in function
    driver.get("THE URL OF THE PAGE YOU NEED")
    driver.find_element_by_id("email").send_keys("YOUR LOGIN")
    driver.find_element_by_id("password").send_keys("YOUR PASSWORD", Keys.ENTER)

def addHotel (name):
    #adding the exact entity of a hotel, the entity appeared in the backoffice. The 'name' standing in the brackets is used for adding to the entity name each iteration till the end of the loop.
    #here and further I used different locator types, such as id, xpath, class_name.
    driver.find_element_by_id("hotel_form_builder_name").send_keys(name)
    driver.find_element_by_id("hotel_form_builder_nameEn").send_keys("NAME")
    driver.find_element_by_id("hotel_form_builder_detail").send_keys("DESCRIPTION")
    driver.find_element_by_id("hotel_form_builder_detailEn").send_keys("DESCRIPTION")
    sleep(7)
    driver.find_element_by_xpath('//*[@aria-labelledby="select2-hotel_form_builder_countryId-container"]').click()
    driver.find_element_by_class_name("select2-search__field").send_keys("COUNTRY")
    sleep(7)
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("span[aria-labelledby=\"select2-hotel_form_builder_cityId-container\"]").click()
    driver.find_element_by_class_name("select2-search__field").send_keys("CITY")
    sleep(7)
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    driver.find_element_by_class_name("leaflet-bar-part").click()
    sleep(7)
    driver.find_element_by_class_name("glass").send_keys("ADDRESS ACC. TO THE FORMAT")
    sleep(7)
    driver.find_element_by_class_name("glass").send_keys(Keys.ENTER)
    sleep(7)
    driver.find_element_by_class_name("leaflet-marker-icon").click()
    driver.find_element_by_id("hotel_form_builder_postCode").send_keys("POST CODE")
    driver.find_element_by_id("hotel_form_builder_emailReception").send_keys("EMAIL")
    driver.find_element_by_id("hotel_form_builder_emailAccounting").send_keys("EMAIL")
    driver.find_element_by_id("hotel_form_builder_channelManagerId").click()
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id("hotel_form_builder_channelManagerId").send_keys(Keys.ENTER)
    driver.find_element_by_id("hotel_form_builder_save").click()
    sleep(5)
    mytext = driver.current_url
    textlook = r'\d+'
    global hotelId
    hotelId = ''.join(re.findall(textlook, mytext))

def addSleep ():
    #function for adding an entity connected to the hotel: rooms.
    #each entity (this and below) is created for each hotel in the loop.
    driver.find_element_by_partial_link_text("the text you're looking for").click()
    driver.find_element_by_partial_link_text("the text you're looking for").click()
    driver.find_element_by_id("room_category_form_builder_description").send_keys("NAME")
    driver.find_element_by_id("room_category_form_builder_descriptionEng").send_keys("NAME")
    driver.find_element_by_id("room_category_form_builder_roomSleeps_0").click()  
    driver.find_element_by_id("room_category_form_builder_roomSleeps_1").click()
    driver.find_element_by_id("room_category_form_builder_roomSleeps_2").click()
    driver.find_element_by_id("room_category_form_builder_roomSleeps_3").click()
    driver.find_element_by_id("room_category_form_builder_save").click()
    sleep(5)
    mytext = driver.current_url
    global sleepId
    sleepId = ''.join(re.findall(r'category\/([0-9]+)', mytext))
    driver.find_element_by_partial_link_text("the text you're looking for").click()

def addRate ():
    #function for adding an entity connected to the hotel: rates
    driver.find_element_by_partial_link_text("the text you're looking for").click()
    driver.find_element_by_partial_link_text("the text you're looking for").click()
    driver.find_element_by_id("select2-corp_rate_form_builder_codeCorpRate-container").click()
    driver.find_element_by_class_name("select2-search__field").send_keys("NAME")
    sleep(7)
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    driver.find_element_by_id("corp_rate_form_builder_roomCategoryIds_0").click()
    driver.find_element_by_id("corp_rate_form_builder_save").click()
    sleep(5)
    mytext = driver.current_url
    global rateId
    rateId = ''.join(re.findall(r'corp-rate\/([0-9]+)', mytext))
    driver.find_element_by_partial_link_text("the text you're looking for").click()
    sleep(7)
    driver.find_element_by_class_name("ti-unlock").click()
    sleep(7)
    Alert(driver).accept()
    driver.get("the url you need")


def quoteprice ():
    #function for calling an API method to create quotas and prices for each hotel in the loop.
    url = "the url you need for API"

    payload = "{\n    \"password\": \"YOUR PASSWORD*\",\n    \"username\": \"YOUR USERNAME\",\n    \"action\": \"YOUR ACTION\",\n    \"data\": {\n        \"SOME ID\" : \""+ENTITY_NAME+"\",\r\n        \"updates\": [\n            {\n                \"SOME DATE\": \"DATE ACC. TO THE FORMAT\",\n                \"ONE MORE DATE\": \"DATE ACC. TO THE FORMAT\",\n                \"roomTypeId\" : \""+ENTITY_NAME+"\",\r\n                \"RATE\": \""+ENTITY_NAME+"\",\r\n                                 \"CURRENCY\": \"CURRENCY CODE\",\n                \"quota\": \"AMOUNT\",               \n                \"prices\": [\n                    {\n                        \"SOME CODE\": \"INT\",\n                        \"price\": \"AMOUNT\"\n                    },\n                    {\n                        \"ONE MORE CODE\": \"INT\",\n                        \"price\": \"AMOUNT\"\n                    },\n                    {\n                        \"code\": \"INT\",\n                        \"price\": \"AMOUNT\"\n                    },\n                    {\n                        \"code\": \"INT\",\n                        \"price\": \"AMOUNT\"\n                    }\n                ]\n            }\n        ]\n    }\n}"
    headers = {
  'Content-Type': 'application/json'
    }

    response = requests.request("YOUR HTTP METHOD", url, headers=headers, data = payload)

    driver.get("getting back to the url of hotel creating")

#calling the declared functions in the right order to create 300 entities with connected entities
loginpass ()
for i in range (300):
    #declaring a loop.
    name = "Test Hotel" + str(i)  #making correct hotel name + numeration with each iteration
    addHotel (name)
    addSleep ()
    addRate ()
    quoteprice ()