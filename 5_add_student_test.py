import pytest
import System

#Tests if the program can handle a wrong username
def test_add_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.add_student('yted91', 'databases')
    
    grading_system.reload_data()
    users = grading_system.users
    
    if users['yted91']['courses'] == 'databases':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
