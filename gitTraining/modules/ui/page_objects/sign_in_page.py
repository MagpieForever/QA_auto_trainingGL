from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

#SignInPage - inherited class of BasePage
class SignInPage(BasePage):
    #declare Class attribute URL
    URL = 'https://github.com/login'
    
    #initialisation of inherited class with additional changes
    def __init__(self) -> None:
        super().__init__()
    
    # method to go to a necessary url    
    def go_to(self):
        self.driver.get(SignInPage.URL)
    
    #method for inputting login & password -where do we get them from?? manul input maybe   
    def try_login(self, username, password):
        #finding the field in which the incorrect user's name will be input
        login_elem = self.driver.find_element(By.ID, "login_field")
        
        #input wrong name or wrong email
        login_elem.send_keys(username)
        
        #find field to which the wrong password will be input
        pass_elem = self.driver.find_element(By.ID, "password")
        
        #input the wrong password
        pass_elem.send_keys(password)
        
        #find button sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")
        
        #emulation of left button click
        btn_elem.click()
        
    def check_title(self,expected_title):
        return self.driver.title == expected_title
        
        
