import unittest

from course_def import Course
from institution_def import Institution
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor 

class Test_Institution(unittest.TestCase):
    def test_institution(self):    
        # Arrange
        
        #declaring attributes needed later
        department = "ComputerScience"
        courseNumber = 1234
        courseName = "TestClass"
        courseCredits = 3
        courseSectionNumber = 123
        courseOfferYear = '2023'
        courseQuarter = '1'
        
        # Define courses and a course offering
        course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
        course2 = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
        course3 = Course(department=department, number=courseNumber, name='csc', credits= courseCredits)
        courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

        # Define a student
        student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")
        
        # Define an institution
        institution = Institution("Quinnipiac University", "qu.edu")
        institution2 = Institution("Quinnipiac University", "qu.edu")

        # Act
        #Add the course to the institution (to the course catalog)
        institution.add_course(course)

        # Add the course to to the planned course offerings
        institution.add_course_offering(courseOffering)

        # Enroll the student into the school
        institution.enroll_student(student1)

        # Register the student for the course
        institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

        #instructor
        instructor1 = Instructor('last','first',institution,'06/08/2000','ee')
        institution.hire_instructor(instructor1)
        
        # Assert
        assert len(courseOffering.registered_students) == 1
        assert len(institution.course_catalog) == 1
        assert len(institution.student_list) == 1
        assert len(institution.faculty_list) == 1
        assert len(institution.course_catalog) == 1
         
        #Testing outputs
        assert institution.domain == 'qu.edu'
        assert institution.add_course(course2) == 'Course has already been added'
        
        #Testing outputs
        assert institution.list_course_schedule('2023','1') != 'No offerings during this semester'
        assert institution.list_course_schedule('2023','1',department) != 'No offerings during this semester'
        assert institution.list_course_schedule('2022','1') != 'No offerings during this semester'
        assert institution.list_course_schedule('2022','1',department) == 'No offerings during this semester'
        
        #Testing outputs
        assert institution.assign_instructor(instructor1,courseName,department,courseNumber,courseSectionNumber,courseOfferYear,courseQuarter) == 'first last has been assigned to teach course' 
        assert institution.assign_instructor(instructor1,courseName,department,courseNumber,courseSectionNumber,courseOfferYear,courseQuarter) == 'first last is already teaching this course'
        assert institution.assign_instructor(instructor1,courseName,department,courseNumber,courseSectionNumber,courseOfferYear,0) == 'Course not found. Please create a course and course offering'
       
        #Testing outputs
        assert institution2.list_course_schedule('2002','4') == 'No offerings currently scheduled'
        assert institution2.add_course_offering(CourseOffering(course3,courseSectionNumber,courseOfferYear,courseQuarter)) == 'Please create a course before creating course offering'
       
        #Testing for type errors
        self.assertRaises(TypeError,institution.hire_instructor,course)
        self.assertRaises(TypeError,institution.enroll_student,instructor1)
        self.assertRaises(TypeError,institution.add_course,student1)
        self.assertRaises(TypeError,institution.add_course_offering,instructor1)
        
        #Testing outputs
        assert institution.enroll_student(student1) == 'Test Test is already enrolled!'
        assert institution.hire_instructor(instructor1) == 'first last already works at this institution!'
        assert institution.register_student_for_course(student1,courseName,department,courseNumber,courseSectionNumber,courseOfferYear,courseQuarter) == 'Test Test is already enrolled in this course'
    