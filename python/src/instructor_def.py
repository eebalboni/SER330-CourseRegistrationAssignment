from person_def import Person
import datetime

class Instructor(Person):
    def __init__(self, last_name, first_name, school, date_of_birth, username):
        Person.__init__(self, last_name, first_name, school, date_of_birth, username, 'instructor')
        self.course_list = [] # key = self.course.name

    def list_courses(self, year=None, quarter=None):
        if year and quarter: #filter by year and quarter
            filtered = list(filter(lambda x: x.year == year and x.quarter == quarter, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]
        elif year: #only year arg given
            filtered = list(filter(lambda x: x.year == year, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

        elif quarter: #only quarter arg given
            filtered = list(filter(lambda x: x.quarter == quarter, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

        else: #no filters given, default to None
            final = sorted(self.course_list, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

    def __str__(self):
        return ('\n' + 'Instructor Name: ' + self.first_name + ' ' + self.last_name + '\n' +
            'School: ' + self.school.name + '\n' +
            'DOB: ' + self.date_of_birth.strftime('%b %d, %Y') + '\n' +
            'Username: ' + self.username + '\n')