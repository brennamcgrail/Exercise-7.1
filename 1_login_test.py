import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    users = grading_system.users
    grading_system.login(username,password)
    if users[username]['role'] != grading_system.usr.__class__.__name__.lower():
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
