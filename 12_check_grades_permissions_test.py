import pytest
import System

#Tests if the program can handle a wrong username
def test_check_grades_permissions(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    
    grading_system.login(username,password)
    test = grading_system.usr.check_grades('hdjsr7', 'databases')
    
    course = grading_system.courses['databases']['assignments']
    assignments = []
    
    for key in course:
        assignments.append(key)
        
    users = grading_system.users
    grades = []
    for item in assignments:
        grades.append([item, users['hdjsr7']['courses']['databases'][item]['grade']])
        
    if test == grades:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
