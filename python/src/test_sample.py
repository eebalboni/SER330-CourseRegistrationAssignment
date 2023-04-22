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
    def test_studentInit_WhenAllConditionsAreMet_succeeds(self):
        
        course = Course("Computer Science", 1234, "Test Class", 3)
        cc = CourseOffering(course, "123", "2023", "1")
        student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
        
        cc.submit_grade(student1,'A')
        assert student1.last_name == 'Test'
        assert student1.gpa == 0
        assert len(student1.transcript) == 1
        assert student1.credits == 0
        assert len(student1.course_list) == 0
        assert len(student1.transcript)==1
        assert student1.list_courses == course
        
        
    
class Test_courseOffering(unittest.TestCase):
    def test_courseOffering(self):
        #Arrange
        courseOffering = CourseOffering(2,'MA',2023,4) 
        studentOne = Student('Builder', 'Bob', 'none', 'none', 'bb')
        studentTwo = Student('Bobcat', 'Boomer', 'none', 'none', 'hihj')
        
        #studentThree = Student('Brown', 'Bobby', 'none', 'none', 'hd')
        
        #studentFour = Student('Bee', 'Bumble', 'none', 'none', 'ebal')
        studentFive = Student('Brown', 'Charlie', 'none', 'none', 'hdhdhd')
        stdList = [studentOne,studentTwo,studentFive]
        
        #Act
        courseOffering.register_students(stdList)
        courseOffering.submit_grade(studentOne,70)
        courseOffering.submit_grade(studentTwo,50)
       # courseOffering.submit_grade(studentThree,70)
       # courseOffering.submit_grade(studentFour,85)
        courseOffering.submit_grade(studentFive,50)
        
        #Assert
        #checking the registered students mehtod 
        # assert courseOffering.get_grade(studentOne) == 'C-'
        assert len(courseOffering.registered_students) == len(stdList) 
        assert courseOffering.quarter == 4

class Test_instructor(unittest.TestCase):
    def test_instructor(self):
        #Arrange
        #need instructor
        instructor = Instructor('Builder','Bob','Quinnipiac','10/10/2000','bobBuilder') 
        course = Course('Software',25,'Quality Assurance',3)
        courseOffering = CourseOffering(course, '2','2023','3') 
        courseOfferingTwo = CourseOffering(course, '2','2022','4') 
        coursesList = [courseOffering,courseOfferingTwo]
        instructor.course_list = coursesList
        
        instructorTwo = Instructor('Boomer','Bob','Quinnipiac','10/10/2000','bobBuilder') 
        courseOfferingThree = CourseOffering(course, '2','2022','3') 
        courseOfferingFour = CourseOffering(course, '2','2021','3') 
        courseOffers = [courseOfferingFour,courseOfferingThree]
        instructorTwo.course_list = courseOffers
        
         
        instructorThree = Instructor('Boomer','Bob','Quinnipiac','10/10/2000','bobBuilder') 
        courseOfferingFive = CourseOffering(course, '2','2022','3') 
        courseOfferingSix = CourseOffering(course, '2','2024','3') 
        courseOffersTwo = [courseOfferingSix,courseOfferingFive]
        instructorThree.course_list = courseOffersTwo
        
        #Act
        returnedCourses = instructor.list_courses()
        
        
        #Assert
        assert len(instructorTwo.list_courses('2022')) == 1
        assert len(instructorTwo.list_courses('2022', '3')) == 1
        assert len(returnedCourses) == len(coursesList)
        assert instructor.first_name == 'Bob'

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
    

def test_institution():    
    # Arrange
    # Define a course and a course offering
    #this is test institution
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    course2 = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

    # Define a student
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")
    
    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    # Enroll the student into the school
    institution.enroll_student(student1)

    courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
    institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

    #instructor
    instructor1 = Instructor('last','first',institution,'06/08/2000','ee')
    institution.hire_instructor(instructor1)
    
    # Assert
    assert len(courseOffering.registered_students) == 1
    assert len(institution.course_catalog) == 1
    assert institution.domain == 'qu.edu'
    assert len(institution.faculty_list) == 1
    assert institution.add_course(course2) == 'Course has already been added'
    assert len(institution.student_list) == 1
    #assert institution.assign_instructor(instructor1,courseName,'0',courseNumber,'1',courseOfferYear,courseQuarter) == 'Course not found. Please create a course and course offering'
    assert len(institution.course_catalog) == 1
    