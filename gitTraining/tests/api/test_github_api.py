import pytest

from modules.api.clients.github import GitHub

#1
@pytest.mark.api
def test_user_exists(github_api):
    #api = GitHub() #moved to fixture
    #user = api.get_user('defunkt')
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

#2
@pytest.mark.api
def test_user_not_exists(github_api): #from fixture,  response for instance of a particular github user
    #api = GitHib() #moved to fixture
    #user = api.get_user('butenkosergii')
    r = github_api.get_user('butenkosergii') #gets from instance the body of response
    assert r['message'] == 'Not Found' #analyses the response message to see "Not found"
#3
@pytest.mark.api
def test_repo_can_be_found(github_api): #use of fixture
    r = github_api.search_repo('become-qa-auto')
    #print(r)
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r ['items'][0]['name']
#4
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    print(r)
    assert r['total_count'] == 0
#5
@pytest.mark.api    
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('t')
    assert r['total_count'] != 0
    
#6
@pytest.mark.api 
def test_emoji_3rd_place_medal_is_found(github_api):
    r = github_api.get_emoji("3rd_place_medal")
    print(r)
    assert "3rd_place_medal" in r
    
#7    
@pytest.mark.api
def test_cnt_by_part_of_emoji(github_api):
    number_inst = github_api.count_by_part_of_emoji("_place_medal")
    assert number_inst == 3
    print('test finished')
    

    


    
       
    
            
#pytest -s -m api 