import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

#import time

@pytest.mark.ui 

def test_incorrect_user_name():
    #making the object for controllign the browser
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    driver = webdriver.Chrome(service=Service(r"/Users/dariakozak/Documents/GitHub/gitTraining/" + "chromedriver"), chrome_options=options)  
    #opening the page
    driver.get('https://github.com/login')
    #finding element on the page where the input will be made - fails - import by?
    login_elem = driver.find_element(By.ID, "login_field")
    # send_keys - inputs the sting in the found field
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')
    #time.sleep(3)
   
    #find the field for typing passord in it
    pass_elem = driver.find_element(By.ID, "password")
    #input the wrong password
    pass_elem.send_keys("wrong password")
    #time.sleep(3)
    
    #find the button sign in
    btn_elem = driver.find_element(By.NAME, "commit")
    
    #emulation of click with the left button of mouse
    btn_elem.click()
    #time.sleep(3)
    
    #check that the title of the page is as we expect
    assert driver.title == "Sign in to GitHub · GitHub"
    
    #closing the page
    driver.close()