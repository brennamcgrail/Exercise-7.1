import pytest
import System

#Tests if the program can handle a wrong username
def test_login_failed(grading_system):
    username = 'calyam'
    password = '#yeet'
    grading_system.login(username,password)

    username = 'akend3'
    password =  '123fail'
    grading_system.login(username,password)

    grading_system.usr.drop_student('yted91', 'cloud_computing')
    grading_system.reload_data()
    users = grading_system.users
    
    if users['yted91']['courses'] != 'cloud_computing':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
