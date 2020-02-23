from unittest import TestCase

import classroom_manager

class TestAssignment(TestCase):

    def setup(self):
        self.assignment = classroom_manager.Assignment("testuser", 100.0)


    # test initiator for assignment
    def test_init(self):
        self.setup()
        self.assertEqual(100.0, self.assignment.max_score)
        self.assertEqual("testuser", self.assignment.name)
        self.assertEqual(None, self.assignment.grade)

    #test if a grade can be assigned
    def test_assignGrade(self):
        self.setup()

        #test if a grade can be assigned
        self.assignment.assign_grade(100.0)
        self.assertEqual(100.0, self.assignment.grade)

    # test if a grade is assigned over the max you will get none

    def test_assignGradeMax(self):
        self.setup()

        #test if a grade can be assigned
        self.assignment.assign_grade(100.1)
        self.assertEqual(None, self.assignment.grade)

class TestAction_Student(TestCase):

    def setup(self):
        self.student = classroom_manager.Student(1, "John", "Smith")

    def setupAssignment(self):
        self.assignment = classroom_manager.Assignment("testuser", 100.0)

    def test_init(self):

        #initiate the student object
        self.setup()

        #check if the properties of the student are initialized properly
        self.assertEqual(1, self.student.id)
        self.assertEqual("John", self.student.first_name)
        self.assertEqual("Smith", self.student.last_name)
        self.assertEqual([], self.student.assignments)

    def test_get_full_name(self):
        # initiate the student object
        self.setup()

        # check if the student's name is correct
        self.assertEqual("John Smith", self.student.get_full_name())

    def test_submitAssignment(self):
        #setup student
        self.setup()
        #setup assignment
        self.setupAssignment()

        self.student.submit_assignment(self.assignment)

        # if there is only 1 assignment in the student assignments
        self.assertEqual(1, len(self.student.assignments))

        # check if the assignment is the assignment from setup assignment
        self.assertEqual(self.assignment, self.student.assignments[0])

    

