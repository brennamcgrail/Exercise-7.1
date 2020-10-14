import pytest
import System

#Tests if the program can handle a wrong username
def test_submit_assignment(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    
    grading_system.login(username,password)
    grading_system.usr.submit_assignment('cloud_computing', 'newAssignment', '1234567', '2/20/20')
    
    grading_system.reload_data()
    users = grading_system.users
    
    if users['hdjsr7']['courses']['cloud_computing']['newAssignment']['submission'] != '1234567':
            assert False
            
    if users['hdjsr7']['courses']['cloud_computing']['newAssignment']['submission_date'] != '2/20/20':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
