#I used selenium to access web browser and navigate to download
#This code is contigent on the web structure for the GSE page as at May 28, 2020
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#Optioons allow you to set certain parameters, such as download path, windows size, headless chrome etc. 
options = Options()
options.headless = True
options.disable_gpu = True

options.add_argument("--window-size=1920,1080")
prefs = {'download.default_directory' : r'C:\Users\brown\Downloads\\',"directory_upgrade": True}
options.add_experimental_option("prefs", prefs)



driver = webdriver.Chrome("C:\\\\Users\\\\brown\\\\Downloads\\\\chromedriver_win32\\\\chromedriver.exe", options = options)
driver.maximize_window()
driver.implicitly_wait(2) #you could reduce or comment out the time delays 
driver.get("https://gse.com.gh/daily-shares-and-etfs-trades/")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="post-16458"]/div/div[2]/div[1]/div/div/div/div[1]/ul/li[2]/a').click() #click on Advanced Query
driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dt/a').click() #click on select share code button
#driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[50]/input').click()

driver.execute_script("arguments[0].click();",driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[12]/input'))#select option 12 from select share
driver.execute_script('arguments[0].click();', driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[1]/div/dl/dd/div/ul/li[50]/input'))#select option 50

driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[2]/div/dl/dt/a/span')) #click on select available data(columns)

#choose all available codes
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="daily_date"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="share_code"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="year_high"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="year_low"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="prev_closing_price"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="opening_price"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="closing_price"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="price_change"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="closing_bid_price"]'))#.click()
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="closing_offer_price"]'))#.click()

driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="total_shares"]'))
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="total_value"]'))
driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="last_trans_price"]'))


time.sleep(1)



action = ActionChains(driver)

# last_price = driver.find_element_by_xpath('//*[@id="last_trans_price"]')
# total_shares = driver.find_element_by_xpath('//*[@id="total_shares"]')
# total_value = driver.find_element_by_xpath('//*[@id="total_value"]')



# action.pause(1).perform()
# action.move_to_element(total_shares).perform()
# action.click(total_shares).perform()


# action.pause(1).perform()
# action.move_to_element(total_value).perform()
# action.click(total_value).perform()

# action.pause(1).perform()
# action.move_to_element(total_value).perform()
# action.click(last_price).perform()



#action.perform()


#click on date
action.move_to_element(driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[1]/div/div')).perform()
action.click(driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[1]/div/div')).perform()
action.pause(1).perform()


driver.execute_script('arguments[0].click()', driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[1]/div/div'))
driver.execute_script('arguments[0].click()', driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/thead/tr[2]/th[2]'))
time.sleep(1)
#select date as 01-01-2004
for i in range(16):
    driver.execute_script('arguments[0].click();',
                          driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/thead/tr[2]/th[1]'))#.click()
driver.execute_script('arguments[0].click();',
                      driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/tbody/tr/td/span[1]'))#.click()
driver.execute_script('arguments[0].click();',
                      driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/tbody/tr[1]/td[5]'))#.click()

time.sleep(1)

#this code selects current date(May 27th, 2020)
to_date = driver.find_element_by_xpath('//*[@id="tr_form"]/div/div[3]/div/div[2]/div/div')
to_date.click()
driver.execute_script('arguments[0].click();',  to_date)
driver.execute_script('arguments[0].click();',
                      driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/thead/tr[2]/th[2]'))#.click()
driver.execute_script('arguments[0].click();',
                      driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[2]/table/tbody/tr/td/span[5]'))#.click()
driver.execute_script('arguments[0].click();',
                      driver.find_element_by_xpath('//*[@id="thim-body"]/div[5]/div[1]/table/tbody/tr[5]/td[4]'))#.click()



driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="generate"]'))#.click()

driver.execute_script('arguments[0].click();',driver.find_element_by_xpath('//*[@id="DataTables_Table_0_wrapper"]/div[1]/a[2]/span'))#.click()
