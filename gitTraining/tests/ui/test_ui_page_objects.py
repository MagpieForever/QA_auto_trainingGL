from modules.ui.page_objects.sign_in_page import SignInPage

import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #create an instance of page
    sign_in_page = SignInPage()
    
    #open the page https://github.com/login
    sign_in_page.go_to()
    
    #trying to log into GitHib
    sign_in_page.try_login("page_object@gmail.com", "wrong password")
    
    #check that the title of tha page is as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    
    #close the object
    sign_in_page.close()
    
    
    
