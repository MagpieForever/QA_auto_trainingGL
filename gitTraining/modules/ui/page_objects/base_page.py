from typing import Self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




class BasePage:
    #path where executable file is 
    PATH = r"/Users/dariakozak/Documents/GitHub/gitTraining/"
    #name of chromedriver
    DRIVER_NAME = 'chromedriver'
    
    #def __init__(self,options = webdriver.ChromeOptions()) -> None:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"    
        #find out what Service does - no explanation in the lesson - 1: Service is the new class introduced in selenium 4 to start a webdriver:
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME),chrome_options = options)
    
    def close(self):
        self.driver.close()
        
    #making the object for controllign the browser
    #options = webdriver.ChromeOptions()
    #options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    #driver = webdriver.Chrome(service=Service(r"/Users/dariakozak/Documents/GitHub/gitTraining/" + "chromedriver"), chrome_options=options)  