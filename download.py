#I used selenium to access web browser and navigate to download
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options() #options allow you to open a headless chrome browser. ie,run the code with chrome browser running in background
options.headless = True

driver = webdriver.Chrome("C:\\\\Users\\\\brown\\\\Downloads\\\\chromedriver_win32\\\\chromedriver.exe")#open browser
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://gse.com.gh/daily-shares-and-etfs-trades/") #open website
time.sleep(3)
driver.find_element_by_xpath('//*[@id="post-16458"]/div/div[2]/div[1]/div/div/div/div[1]/ul/li[2]/a').click() #click on Advanced Query
driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dt/a').click() #click on select share code button
#driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[50]/input').click() #choose option 50

driver.execute_script("arguments[0].click();",driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[12]/input') )#choose option 12
driver.execute_script('arguments[0].click();', driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[50]/input'))#choose option 50

driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[2]/div/dl/dt/a/span')) #click select available value fields

#practically select all available fields
driver.find_element_by_xpath('//*[@id="daily_date"]').click()
driver.find_element_by_xpath('//*[@id="share_code"]').click()
driver.find_element_by_xpath('//*[@id="year_high"]').click()
driver.find_element_by_xpath('//*[@id="year_low"]').click()
driver.find_element_by_xpath('//*[@id="prev_closing_price"]').click()
driver.find_element_by_xpath('//*[@id="opening_price"]').click()
driver.find_element_by_xpath('//*[@id="closing_price"]').click()
driver.find_element_by_xpath('//*[@id="price_change"]').click()
driver.find_element_by_xpath('//*[@id="closing_bid_price"]').click()
driver.find_element_by_xpath('//*[@id="closing_offer_price"]').click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="total_shares"]')) #note that we use JS script here for element that are not visible
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="total_value"]'))
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="last_trans_price"]'))


# the piece chooses the date, Jan-01-2004 by navigating the calender object
from_date = driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[1]/div/div')
from_date.click()
driver.execute_script('arguments[0].click()', from_date)
year = driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/thead/tr[2]/th[2]')
driver.execute_script('arguments[0].click()', year)
time.sleep(1)
for i in range(16):
    driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/thead/tr[2]/th[1]').click()
driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/tbody/tr/td/span[1]').click()
driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/tbody/tr[1]/td[5]').click()

time.sleep(1)

#choose current date(May 27,2020) as at when code was written
to_date = driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[2]/div/div') 
to_date.click()
driver.execute_script('arguments[0].click();',  to_date)

driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/thead/tr[2]/th[2]').click()
driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/tbody/tr/td/span[5]').click()
driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/tbody/tr[5]/td[4]').click()



driver.find_element_by_xpath('//*[@id="generate"]').click() #click generate
#driver.find_element_by_xpath('//*[@id="DataTables_Table_0_wrapper"]/div[1]/a[2]/span').click() #click on CSV to download

#time.sleep(3)
#driver.close()
