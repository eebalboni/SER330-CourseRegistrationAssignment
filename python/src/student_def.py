from person_def import Person
import datetime

class Student(Person):
    def __init__(self, last_name, first_name, school, date_of_birth, username):
        Person.__init__(self, last_name, first_name, school, date_of_birth, username, 'student')
        self.course_list = [] #list of offering objects
        self.transcript = {} #course:grade

    def list_courses(self):
        ordered = sorted(self.transcript.keys(), key = lambda x: (x.year, x.quarter), reverse=True)
        return ordered

    @property
    def credits(self):
        total = 0
        for x in self.course_list:
            total += x.course.credits
        return total

    @property
    def gpa(self):
        earned = 0
        available = 0

        grade_scale = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33,'B':3.0,'B-':2.67, 'C+':2.33,'C':2.0,'C-':1.67, 'D+':1.33, 'D':1.0, 'D-': 0.67,'F':0}

        for x in self.course_list:
            if self.username in x.grades.keys(): #check to see if a grade has already been submitted
                earned += (grade_scale[x.get_grade(self)] * x.course.credits)
                available += x.course.credits

        if available == 0:
            GPA = 0
        else:
            GPA = earned / available

        return GPA

    def __str__(self):
        return ('\n' + 'Student Name: ' + self.first_name + ' ' + self.last_name + '\n' +
            'School: ' + self.school.name + '\n' +
            'DOB: ' + self.date_of_birth.strftime('%b %d, %Y') + '\n' +
            'Username: ' + self.username + '\n' +
            'Email: ' + self.email + '\n' +
            'GPA: ' + str(self.gpa) + '\n' +
            'Credits: ' + str(self.credits) + '\n')