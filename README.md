# Exercise-7.1

I separated the tests into individual files, and used pytest to test all of them at once.

### First ten tests:
1. **login** - System.py 
   * **My file:** 1_login_test.py
   * This test passes.
1. **check_password** - System.py
   * **My file:** 2_check_password_test.py
   * This test passes.
1. **change_grade** - Staff.py
   * **My file:** 3_change_grade_test.py
   * This test is asserted false because the new grade defined by the user is not the same as the updated grade data in the users.json file. 
1. **create_assignment** - Staff.py
   * **My file:** 4_create_assignment_test.py
   * This test passes.
1. **add_student** - Professor.py
   * **My file:** 5_add_student_test.py
   * This test fails because there is a TypeError in the Professor.py file.
1. **drop_student** - Professor.py
   * **My file:** 6_drop_student_test.py
   * This test passes.
1. **submit_assignment** - Student.py
   * **My file:** 7_submit_assignment_test.py
   * This test fails because there is a KeyError from the assignment name; the course name is hard-coded in Student.py so the only accepted assignment names are “assignment1” and “assignment2”.
1. **check_ontime** - Student.py
   * **My file:** 8_check_ontime_test.py
   * This test is asserted false because the function always returns true.
1. **check_grades** - Student.py
   * **My file:** 9_check_grades_test.py
   * This test passes.
1. **view_assignments** - Student.py
   * **My file:** 10_view_assignments_test.py
   * This test is asserted false because Student.py is hard-coded to always return the grades for the course “comp-sci”.
### My tests:
1. **drop_student (permissions)** - Professor.py
   * **My file:** 11_drop_student_permissions_test.py
   * This test checks if the system allows a professor who is not in charge of a certain course to remove a student from that course.
   * This test is asserted false because the system allows the professor to remove the student.
1. **check_grades (permissions)** - Staff.py
   * **My file:** 12_check_grades_permissions_test.py
   * This test checks if the system allows a TA to check the grades of a student in a course the TA does not assist with.
   * This test is asserted false because the system allows the TA to check the grades.
1. **create_assignment (if the assignment already exists)** - Staff.py
   * **My file:** 13_create_assignment_exist_test.py
   * This test checks if a professor can create an assignment that already exists. This would be a problem because it would create complications if students have already created submissions for the original assignment.
   * This test is asserted false because the system allows the professor to create the assignment, and the original assignment’s information is overwritten.
1. **check_grades (case_sensitive)** - Student.py
   * **My file:** 14_check_grades_case_sensitive_test.py
   * This test checks if a student can check their grades for courses with “Grade” written instead of “grade” in the json file.
   * This test fails because there is a key error within the Student.py file.
1. **login (after failure)** - System.py
   * **My file:** 15_login_failed_test.py
   * A login is attempted, but failed, while another user is logged in. This test checks if the system allows actions to be performed. This could be a security issue, and should not be allowed.
   * This test is asserted false because the system allows the action to be performed.
