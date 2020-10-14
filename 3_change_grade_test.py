import pytest
import System

#Tests if the program can handle a wrong username
def test_change_grade(grading_system):
    username = 'goggins'
    password =  'augurrox'
    
    grading_system.login(username,password)
    users = grading_system.users
    
    origGrade = users['akend3']['courses']['databases']['assignment2']['grade']
    newGrade = 80
    
    grading_system.usr.change_grade('akend3', 'databases', 'assignment2', newGrade)
    grading_system.reload_data()
    users = grading_system.users

    updatedGrade = users['akend3']['courses']['databases']['assignment2']['grade']
    
    if origGrade == updatedGrade:
        assert False
        
    if newGrade != updatedGrade:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
