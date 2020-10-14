import pytest
import System

#Tests if the program can handle a wrong username
def test_drop_student_permissions(grading_system):
    username = 'goggins'
    password = 'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.drop_student('akend3', 'comp_sci')
    
    grading_system.reload_data()
    users = grading_system.users
    
    if users['akend3']['courses'] != 'comp_sci':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
