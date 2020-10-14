import pytest
import System

#Tests if the program can handle a wrong username
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    
    grading_system.login(username,password)
    test = grading_system.usr.view_assignments('databases')
    
    course = grading_system.courses['databases']['assignments']
    
    assignments = []
    for item in course:
        assignments.append([item, course[item]['due_date']])
    
    if test != assignments:
            assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
