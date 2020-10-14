import pytest
import System

#Tests if the program can handle a wrong username
def test_check_password(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'pass1234')
    test3 = grading_system.check_password(username,'PASS1234')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
