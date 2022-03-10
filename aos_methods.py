import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import aos_locators as locators

# Using Selenium WebDriver, open the web browser.
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    # print test start day and time;
    print('---------------------~*~---------------------')
    print(f'########### The test is started at {datetime.datetime.now()}')
    # Maximize the browser window.
    driver.maximize_window()
    # Add implicitly wait for 30 seconds
    driver.implicitly_wait(30)
    # Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)
    driver.get(locators.home_page_url)
    print(f'{driver.current_url}')  # Tip: Use print(driver.current_url) to find the actual AOS Website URL
    print(f'{driver.title}')  # Tip: Use print(driver.title) to find the actual title.

    # Check URL and home page title are as expected.
    if driver.current_url == locators.home_page_url and driver.title == locators.home_page_title:
        print(f'{locators.home_page_url} launched successfully!')
        # print(f'The actual AOS website URL is {driver.current_url} and the actual title is {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.home_page_url} did not launch.Please check the code or website')
        print(f'Current URL is {driver.current_url}. Page title is {driver.title}')
        sleep(0.25)
        tearDown()


def tearDown():
    if driver is not None:
        print('---------------------~*~---------------------')
        print(f'########### The test is completed at {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# 5. Create Selenium Automated Scripts that will do the following
# Create New Account - using Faker library fake data
def create_new_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.5)
    # assert driver.find_element((By.ID,'registerPage')).is_displayed()
    # sleep(0.25)

    for i in range(len(locators.list_opt)):
        if locators.list_names[i]:
            driver.find_element(By.NAME, locators.list_names[i]).send_keys(locators.list_val[i])
            sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)


# Validate New Account is created
def validate_new_account():
    # Validate New Account created (new username is displayed in the top menu)
    if driver.title == locators.home_page_title:
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, locators.new_user_name).is_displayed()
        sleep(0.25)


def logout():
    # #Logout
    driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
    # driver.find_element(By.XPATH, f'//@id="menuUserLink"/span[contains(.,"{new_user_name}")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    # driver.find_element(By.ID,'hrefUserIcon').click()
    # java_script=driver.find_element(By.XPATH,'//label[contains(.,Sign out")]')
    # driver.execute_script("argument[0].click()",java_script)
    # 6. Close the browser and display user-friendly messages.


# 1.  Add Login functionality
def login():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    assert driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').is_displayed()
    sleep(0.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_user_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').click()
    sleep(0.25)


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('AOSmessage.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_user_name}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


def check_homepage_text():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            if locators.homepage_textid[i]:
                assert driver.find_element(By.ID,locators.homepage_textid[i]).is_displayed()
                sleep(0.25)
        # assert driver.find_element(By.ID,'speakersTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'laptopsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'miceTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'headphonesTxt').is_displayed()
        # sleep(0.25)
        print('Homepage texts are displayed!')


def check_shopnow_button():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            if locators.homepage_textid[i]:
                driver.find_element(By.ID,locators.homepage_textid[i]).click()
                sleep(0.25)
                path=locators.homepage_texts[i]
                #print(f'{path}')
                #assert driver.find_element(By.XPATH,'f//h3[contains(text(),"{path}")]').is_displayed()
                sleep(0.5)
                driver.find_element(By.XPATH,'//a[contains(text(),"HOME")]').click()
                sleep(0.25)
                #driver.get(locators.home_page_url)
                #sleep(0.25)
        print('Shop Now button are clickable')
        sleep(0.25)


def check_main_menu():
    if driver.title == locators.home_page_title:
    #for i in range(len(locators.homepage_menu)):
        # b = driver.find_element(By.XPATH, f'//a[contains(text(),{locators.homepage_menu[i]})]')
        b = driver.find_element(By.XPATH,"//a[contains(text(),'SPECIAL OFFER')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu SPECIAL OFFER is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu POPULAR ITEMS is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'CONTACT US')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu CONTACT US is clickable')
        sleep(0.25)

    print('menu item are clickable')


def check_mainlogo():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        assert driver.find_element(By.XPATH,'//span[contains(text(),"dvantage")]').is_displayed()
        print('Main logo is displayed')


def check_socialmedia_link():
    driver.get(locators.home_page_url)
    if driver.title == locators.home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME,'follow_facebook').click()
        sleep(0.25)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        if driver.current_url == locators.fb_page_url:
            sleep(0.25)
            print("Facebook links on Homepage is clickable")
            sleep(0.25)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME,'follow_twitter').click()
        sleep(0.25)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        if driver.current_url == locators.tw_page_url:
            sleep(0.25)
            print("Twitter links on Homepage is clickable")
            sleep(0.25)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME,'follow_linkedin').click()
        sleep(0.25)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        #if driver.current_url == locators.in_page_url:
        sleep(0.25)
        print("LinkedIn links on Homepage is clickable")
        sleep(0.25)
        #driver.close()
        sleep(0.25)
    #driver.switch_to.window(driver.window_handles[0])


def contact_us():
    sleep(0.25)
    Select(driver.find_element(By.NAME,'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(0.25)
    Select(driver.find_element(By.NAME,'productListboxContactUs')).select_by_visible_text('HP H2310 In-ear Headset')
    sleep(0.25)
    driver.find_element(By.NAME,'emailContactUs').send_keys(locators.new_email)
    sleep(0.25)
    driver.find_element(By.NAME,'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.25)
    driver.find_element(By.ID,'send_btnundefined').click()
    assert driver.find_element(By.XPATH,'//p[contains(text(),"Thank you for contacting Advantage support.")]')
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'CONTINUE SHOPPING').click()
    if driver.current_url == locators.home_page_url:
        print('CONTACT US form is working properly')

#setUp()
#check_shopnow_button()
#check_main_menu()
#contact_us()
#check_homepage_text()
#tearDown()
# # Create New Account
# create_new_account()
# # Validate New Account is created
# validate_new_account()
# print(f'------New account is created, Username is {locators.new_user_name}')
# # Logout
# logout()
# sleep(0.5)
# # Login
# login()
# # Validate New User can login (see if you can reuse New Account Validation)
# validate_new_account()
# print(f'------New user {locators.new_user_name} can log in!')
# logger('created')
# # Logout
# logout()
# print(f'------New user {locators.new_user_name} can log out successfully!')
# sleep(0.25)
# tearDown()
