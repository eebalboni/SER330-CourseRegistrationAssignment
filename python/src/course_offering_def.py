import datetime
from student_def import Student 
class CourseOffering:
    def __init__(self, course, section_number, year, quarter):
        self.course = course
        self.section_number = section_number
        self.instructor = None #instructor saved for later #6
        self.year = year
        self.quarter = quarter
        self.registered_students = [] #keep a list of registered students
        self.grades = {} #keep a dictionary of grades keyed by username

    def register_students(self, *args):
        for arg in args:
            self.registered_students.append(arg)
            arg.course_list.append(self) #add courseoffering to list of this student's course

    def get_students(self):
        return self.registered_students

    def submit_grade(self, student, grade):
        valid_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
        if isinstance(student, Student) and grade in valid_grades: # if arg is instance of student and is a valid grade
            self.grades[student.username] = grade #add student grade to course offering
            key = self.__str__()
            student.transcript[key] = grade #add grade to student's transcript
        #elif not(isinstance(student, Student)) and grade in valid_grades:
        #    self.grades[student] = grade
        else:
            return 'Please enter a valid grade'

    def get_grade(self, student):
        if isinstance(student, Student): #if student for an arg
            return self.grades[student.username]
        else:
            return self.grades[student] #it will raise a key-val errot if arg is incorrect

    def __str__(self): #EX: Algorithms, MPCS 55001-1, Gerry Brady, (Fall 2017)
        if self.instructor: #if an instructor has been assigned
            return (self.course.name + ', ' + self.course.department +
                ' ' + str(self.course.number)+'-'+str(self.section_number) +
                ', ' + self.instructor.first_name + ' ' + self.instructor.last_name +
                ' (' + self.quarter + ' ' + str(self.year) + ')')
        else: #else just list course with no instructore name
            return (self.course.name + ', ' + self.course.department +
                ' ' + str(self.course.number)+'-'+str(self.section_number) +
                ' ' + ' (' + self.quarter + ' ' + str(self.year) + ')')