import unittest

from course_def import Course

#Always start test classes with class Test_Something
class Test_course(unittest.TestCase):
    #def has to have test_
    def test_course(self):
        #Arrange & Act 
        course = Course('Math',65,'MA150',3)
        
        # Act 
        # course.credits = 4
        
        # Assert
        assert course.credits == 3
     
if __name__ == '__main__':
    unittest.main() 