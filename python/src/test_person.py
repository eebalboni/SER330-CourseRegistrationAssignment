import unittest

from person_def import Person

class Test_Person(unittest.TestCase):
    #follow this for naming to be clearer
    def test_PersonInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        #person.last_name = 'Test'

        # Assert assert.equals is used for strings 
        assert person.last_name == ('LastName')