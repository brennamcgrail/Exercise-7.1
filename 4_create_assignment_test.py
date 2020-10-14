import pytest
import System

#Tests if the program can handle a wrong username
def test_create_assignment(grading_system):
    username = 'calyam'
    password = '#yeet'
    
    grading_system.login(username,password)
    grading_system.usr.create_assignment('newAssignment', '02/18/20', 'cloud_computing')
    grading_system.reload_data()
    
    courses = grading_system.courses
    
    if courses['cloud_computing']['assignments']['newAssignment']['due_date'] != '02/18/20':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
