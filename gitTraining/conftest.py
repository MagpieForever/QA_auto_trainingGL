#file conftest should always be in root dir!

import pytest
from modules.api.clients.github import GitHub

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None    

    def create(self):
        self.name = 'Daria'
        self.second_name = 'Kozak'
    
    def remove(self):
        self.name = ''
        self.second_name = ''
        


@pytest.fixture

def user():
    user = User()
    user.create()
    
    yield user
    
    user.remove()
    
@pytest.fixture   
def github_api():
    api = GitHub() #creates an instance of GitHub - body of request to the searched link
    yield api  #return on the created instance to tests under name github_api

     