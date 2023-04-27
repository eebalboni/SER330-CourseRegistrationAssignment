import unittest

from student_def import Student


class Test_student(unittest.TestCase):
    def test_studentInit_WhenAllConditionsAreMet_succeeds(self):
        
        #Arrange && Act
        student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
        
        #Assert
        assert student1.last_name == 'Test'
        assert student1.gpa == 0
        assert student1.credits == 0
        assert len(student1.course_list) == 0
       
        
    