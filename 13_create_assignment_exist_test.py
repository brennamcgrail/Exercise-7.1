import pytest
import System

#Tests if the program can handle a wrong username
def test_create_assignment_exist(grading_system):
    username = 'saab'
    password = 'boomr345'
    
    grading_system.login(username,password)
    grading_system.usr.create_assignment('assignment1', '02/18/20', 'comp_sci')
    grading_system.reload_data()
    
    courses = grading_system.courses
    
    if courses['comp_sci']['assignments']['assignment1']['due_date'] == '02/18/20':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
