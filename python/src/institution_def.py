import datetime
from course_def import Course
from student_def import Student
from course_offering_def import CourseOffering
from instructor_def import Instructor

class Institution:
    def __init__(self, name, domain): #adding a domain to constructor, since there is no standard method you can build for it
        self.name = name
        self.domain = domain

        #key = student username, value = student object
        self.student_list = {} 
        self.course_catalog = {} #key = course name; value = courses; #institution.coursecatalog[course].append(courseoffering)
        self.course_schedule = {} #key = course name; value = list course offerings
        self.faculty_list = {} #key = username #value = instructor

    def list_students(self):
        print('\n' + 'Enrolled Students (' + self.name + ') \n' + '-------------------------------------------')
        slist = [x.last_name + ', ' + x.first_name for x in self.student_list.values()]
        student_list = sorted(slist) #alphabetize
        for x in student_list:
            print(x)
        print('\n')

    def enroll_student(self, student):
        if isinstance(student,Student):
            if student.username in self.student_list.keys():
                return(student.first_name + ' ' + student.last_name + ' is already enrolled!')
            else:
                self.student_list[student.username] = student
        else:
            raise TypeError('Only accepts student object')

    def register_student_for_course(self, this_student, course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                if this_student in self.student_list.values(): #if student is enrolled in school
                    if this_student in offering.registered_students: #if student is already enrolled in this offering
                        return(this_student.first_name + ' ' + this_student.last_name + ' is already enrolled in this course')
                    else:
                        offering.register_students([this_student])
                        #print('\n' + this_student.first_name + ' ' + this_student.last_name + ' has been enrolled ' + offering.__str__() +'\n')

    def list_instructors(self):
        print('\n' + 'Instructor List (' + self.name + ') \n' + '-------------------------------------------')
        flist = [x.last_name + ', ' + x.first_name for x in self.faculty_list.values()]
        faculty_list = sorted(flist)
        for x in faculty_list:
            print(x)
        print('\n')

    def hire_instructor(self, instructor):
        if isinstance(instructor, Instructor):
            if instructor.username in self.faculty_list.keys():
                return(instructor.first_name + ' ' + instructor.last_name + ' already works at this institution!')
            else:
                self.faculty_list[instructor.username] = instructor
        else:
            raise TypeError('Only accepts instructor object')

    def assign_instructor(self,this_instructor,course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                if offering.instructor == this_instructor:
                    return(this_instructor.first_name + ' ' + this_instructor.last_name + ' is already teaching this course')
                else:
                    offering.instructor = this_instructor
                    this_instructor.course_list.append(offering)
                    return(this_instructor.first_name + ' ' + this_instructor.last_name + ' has been assigned to teach course')
            else:
                return('Course not found. Please create a course and course offering')

    def list_course_catalog(self):
        print('\n' + 'Course Catalog (' + self.name + ') \n' + '----------------------------------------')
        for item in self.course_catalog.values():
            print(item.__str__())
        print('\n')

    def list_course_schedule(self, year, quarter, dept=None):
        if dept: #filter by year, quarter, and department
            schedule = []
            print('\n' + 'Course Schedule (' + dept + ', '+ quarter + ' '+ str(year) + ') \n' + '----------------------------------------')
            for offerings in self.course_schedule.values(): #each item in list is a list of offerings for a given course
                filtered = list(filter(lambda x: x.year == year and x.quarter == quarter and x.course.department == dept, offerings)) #filters
                for item in filtered:
                    schedule.append(item.__str__())
            if schedule:
                for x in schedule:
                    print(x)
            else:
                return('No offerings during this semester')
            #return schedule
        else: #filter only by dept
            schedule = []
            print('\n' + 'Course Schedule (' + quarter + ' '+ str(year) + ') \n' + '----------------------------------------')
            if self.course_schedule: #if the course schedule is not empty
                for offerings in self.course_schedule.values():
                    filtered = list(filter(lambda x: x.year == year and x.quarter == quarter, offerings)) #filters
                    for item in filtered:
                        schedule.append(item.__str__())
                if schedule:
                    for x in schedule:
                        print(x)
                else:
                    return('No offerings scheduled during this semester')
            else:
                return('No offerings currently scheduled')
            #return schedule

    def list_registered_students(self,course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                print('Registered Students List (' + offering.__str__() + ') \n' + '------------------------------------------------------------')
                for student in offering.registered_students:
                    print(student.last_name + ', ' + student.first_name) #list of students in offering

    def add_course(self, course): #this adds courses, NOT course offerings
        if isinstance(course, Course):
            if course.name in self.course_catalog.keys(): #if course object is already in dict
                return 'Course has already been added'     #we dont need it
            else:
                self.course_catalog[course.name] = course #otherwise create a new entry in our course catalog
        else:
            raise TypeError('Only accepts course object as argument')

    def add_course_offering(self, course_offering):
        if isinstance(course_offering, CourseOffering): #check for right instance
            if course_offering.course.name in self.course_catalog.keys(): #check to see if course in course catalog
                
                self.course_schedule.setdefault(course_offering.course.name, []) #sets default values to list

                # Course Offerings are stored as a collection in a dictionary based on course_name
                self.course_schedule[course_offering.course.name].append(course_offering)
            else:
                return 'Please create a course before creating course offering'
        else:
            raise TypeError('Only accepts course offering as argument')