
import unittest

from person_def import Person
from course_def import Course
from institution_def import Institution
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor 

class Test_Person(unittest.TestCase):
    #follow this for naming to be clearer
    def test_PersonInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        #person.last_name = 'Test'

        # Assert assert.equals is used for strings 
        assert person.last_name == ('LastName')

#Always start test classes with class Test_Something
class Test_course(unittest.TestCase):
    #def has to have test_
    def test_course(self):
        #Arrange & Act 
        course = Course('Math',65,'MA150',3)
        
        # Act
        # course.credits = 3
        
        assert course.credits == 3
     
if __name__ == '__main__':
    unittest.main() 
    
class Test_student(unittest.TestCase):
    def test_student(self):
        student = Student('LastName', 'FirstName', 'none', 'none', 'none')
        
        courseTwo = CourseOffering(3,'English',2023,2)
        courseThree = CourseOffering(1,'Science',2023,4)
        courseOffering = CourseOffering(2,'Math',2023,4) 
        
        student.course_list.append(courseOffering)
        student.course_list.append(courseTwo)
        student.course_list.append(courseThree)
        
        #print(str(Student.list_courses(self)))
     
        #Testing the constructor 
        assert student.course_list != 0
        assert student.school == ('none')
        
class Test_courseOffering(unittest.TestCase):
    def test_courseOffering(self):
        courseOffering = CourseOffering(2,'MA',2023,4) 
        studentOne = Student('Builder', 'Bob', 'none', 'none', 'bb')
        studentTwo = Student('Bobcat', 'Boomer', 'none', 'none', 'hihj')
        studentThree = Student('Brown', 'Bobby', 'none', 'none', 'hd')
        studentFour = Student('Bee', 'Bumble', 'none', 'none', 'ebal')
        studentFive = Student('Brown', 'Charlie', 'none', 'none', 'hdhdhd')
        courseOffering.register_students(studentOne,studentTwo,studentThree,studentFive,studentFour)
        
        
        courseOffering.submit_grade(studentOne.username,95)
        courseOffering.submit_grade(studentTwo.username,50)
        courseOffering.submit_grade(studentThree.username,70)
        courseOffering.submit_grade(studentFour.username,85)
        courseOffering.submit_grade(studentFive.username,50)
        
        assert courseOffering.get_grade(studentThree) == 'C-'
        
        #checking the registered students mehtod 
        assert courseOffering.registered_students.__contains__(studentFive)
        #testing the constructor
        assert courseOffering.quarter == 4

class Test_institution(unittest.TestCase):
    def test_institution(self):
        institution = Institution('Quinnipiac','.edu') 
        
        #testing the constructor
        assert institution.name != 'Fairfield'

class Test_instructor(unittest.TestCase):
    def test_instructor(self):
        instructor = Instructor('Builder','Bob','Quinnipiac',10/10/2000,'bobBuilder') 
        
        #testing the constructor
        assert instructor.first_name == 'Bob'