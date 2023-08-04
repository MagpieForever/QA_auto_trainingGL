import pytest
@pytest.mark.check
def test_check_name(user):
    assert user.name == 'Daria'
    
@pytest.mark.check   
def  test_check_second_name(user):
    assert user.second_name == 'Kozak'

'''@pytest.mark.check
def test_change_name(user):
        #user = User()
        #user.create()
        
        assert user.name == 'Sergii'
        
        #user.remove()
        
        
@pytest.mark.check       
def test_change_second_name(user):
        #user = User()
        #user.create()
    
        assert user.second_name == 'Butenko'
        
        #user.remove()'''

    
    