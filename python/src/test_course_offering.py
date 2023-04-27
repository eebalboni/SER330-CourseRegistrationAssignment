import unittest

from person_def import Person
from course_def import Course
from institution_def import Institution
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor 

class Test_courseOffering(unittest.TestCase):
    def test_courseOffering(self):
        #Arrange
        courseOffering = CourseOffering(2,'MA',2023,4) 
        studentOne = Student('Builder', 'Bob', 'none', 'none', 'bb')
        studentTwo = Student('Bobcat', 'Boomer', 'none', 'none', 'hihj')
        studentFive = Student('Brown', 'Charlie', 'none', 'none', 'hdhdhd')
        stdList = [studentOne,studentTwo,studentFive]
        
        #Act
        courseOffering.register_students(stdList)
        courseOffering.submit_grade(studentOne,70)
        courseOffering.submit_grade(studentTwo,50)
        courseOffering.submit_grade(studentFive,50)
        
        #Assert
        assert len(courseOffering.registered_students) == len(stdList) 
        assert courseOffering.quarter == 4


def test_VerifyGradeSubmission_WhenAllConditionsAreMet_ReturnsTrue_Pytest():
    # Arrange
    course = Course("Computer Science", 1234, "Test Class", 3)
    cc = CourseOffering(course, "123", "2023", "1")
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
    studentsList = [student1]
   
    # Act
    #cc.register_students(studentsList)
    cc.submit_grade(student1, 'B')
    # Assert
    # Grades is a dictionary not a list
    # Grades are stored in the dictionary by user name
    # Given this we can test for multiple conditions
    # does 1 and only 1 grade exist?
    assert len(cc.grades) == 1
    # Is the key of the grade the username for student 1?
    assert cc.grades.keys().__contains__("userName")
    #s  Ithe value of this grade a B?
    assert cc.grades.get("userName") == 'B'