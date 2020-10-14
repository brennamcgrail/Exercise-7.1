import pytest
import System

#Tests if the program can handle a wrong username
def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    
    grading_system.login(username,password)
    
    test = grading_system.usr.check_ontime('2/7/20', '2/9/20')
    test2 = grading_system.usr.check_ontime('2/9/20', '2/7/20')
    test3 = grading_system.usr.check_ontime('2/9/20', '2/9/20')
    
    if test != True:
        assert False
            
    if test2 == True:
        assert False
        
    if test3 != True:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
