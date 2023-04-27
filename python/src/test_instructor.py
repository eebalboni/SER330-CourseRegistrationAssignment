import unittest
from course_def import Course
from course_offering_def import CourseOffering
from instructor_def import Instructor 

class Test_instructor(unittest.TestCase):
    def test_instructor(self):
        #Arrange
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