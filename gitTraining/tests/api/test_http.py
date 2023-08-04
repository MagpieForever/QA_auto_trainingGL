#test which will send HTTP request to git hub site

import pytest         #pytest will do the job
import requests       #request is the module for sending requests 

@pytest.mark.http     # mark should be added to pytest.ini
def test_first_request():
    r= requests.get('https://api.github.com/zen') #sending request to get response from address and saving ti "r"
    # printing data saved as r as text, text is attribute of variable r
    print(f'Printing response from https://api.github.com/zen: {r.text}') 
# the command to give ot pytest: pytest -m http -s 
# -s means analogue for print() in the python code

@pytest.mark.http
def test_second_request():
    # request to get response from api.github.com/users/defunkt and saving it as r
    r =requests.get('https://api.github.com/users/defunkt')
    #print(f'Response is {r.text}')
    #print(f'Response body is {r.json()}')
    #calling method json() on variable r (it will create json from this data)
    body = r.json()
    #print(f'Body is {body}')
    

    assert body['name']== 'Chris Wanstrath' #body is a dictionary, we get access to value via key and check it == Chris Wanstrath
    assert r.status_code == 200 # status_code if a property, we get access to it with dot notation and check that is it 200
    
    headers = r.headers #headers is a property of r, getting access to it via dot notation
    #print(f'Headers are {headers}')
    #print(f'Response status code is {r.status_code}')
    assert headers['Server'] == 'GitHub.com' #Get access to value of "Server" via key in dictionary 'headers'
    #print(f'Response body is {r.headers}')
 
@pytest.mark.http
def  test_status_code_request():
    r =requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404 # make check

 

    
#request module is used to send requests from python code
#syntax : r= request.get('address)
# to install : python -m pip install requests