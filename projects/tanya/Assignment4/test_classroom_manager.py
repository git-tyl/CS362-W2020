from unittest import TestCase

import classroom_manager

class TestAssignment(TestCase):

    #setup assignment variable
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

    #setup a list of assignment
    def setupAssignments(self):
        # setup student
        self.setup()

        # setup assignment1
        self.assignment1 = classroom_manager.Assignment("assignment1", 100.0)
        #assign grade to 1
        self.assignment1.assign_grade(100.0)
        # setup assignment2
        self.assignment2 = classroom_manager.Assignment("assignment2", 100.0)
        # assign grade to 2
        self.assignment2.assign_grade(50.0)
        # setup assignment3
        self.assignment3 = classroom_manager.Assignment("assignment3", 100.0)
        # no grade is assigned is None
        # add the assignments to student assignments properties
        self.student.submit_assignment(self.assignment1)
        self.student.submit_assignment(self.assignment2)
        self.student.submit_assignment(self.assignment3)

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

    def test_get_assignment(self):

        #setup student and assignment
        self.setupAssignments()

        # check if there are 3 assignments in the student assignments
        self.assertEqual(3, len(self.student.get_assignments()))

        self.assertEqual(self.assignment1, self.student.get_assignments()[0])
        self.assertEqual(self.assignment2, self.student.get_assignments()[1])
        self.assertEqual(self.assignment3, self.student.get_assignments()[2])


    def test_get_assignment(self):

        # setup student and assignment
        self.setupAssignments()

        # check if there are 3 assignments in the student assignments
        self.assertEqual(3, len(self.student.get_assignments()))

        # get the assignment named testuser1
        self.assertEqual(self.assignment1, self.student.get_assignment("assignment1"))

        # check if assignment name is correct
        self.assertEqual("assignment1", self.student.get_assignment("assignment1").name)

        # check if assignment 2 name is correct
        self.assertEqual("assignment2", self.student.get_assignment("assignment2").name)

        # check if assignment 3 has none grade
        self.assertEqual(None, self.student.get_assignment("assignment3").grade)

    #test the average function
    def test_get_average(self):
        # setup student and assignment
        self.setupAssignments()

        # check if there are 3 assignments in the student assignments
        self.assertEqual(3, len(self.student.get_assignments()))

        # get the assignment named testuser1
        self.assertEqual(self.assignment1, self.student.get_assignment("assignment1"))

        # check if assignment name is correct
        self.assertEqual("assignment1", self.student.get_assignment("assignment1").name)

        # check if assignment 2 name is correct
        self.assertEqual("assignment2", self.student.get_assignment("assignment2").name)

        # check if assignment 3 name is correct
        self.assertEqual("assignment3", self.student.get_assignment("assignment3").name)

        # check if assignment 3 has none grade

        self.assertEqual(None, self.student.get_assignment("assignment3").grade)

        #get avarege

        self.assertEqual(75.0, self.student.get_average())

    # test the average function
    def test_get_average_zero_division(self):

        # setup student and assignment

        # setup student
        self.setup()

        # setup assignment1
        self.assignment1 = classroom_manager.Assignment("assignment1", 100.0)
        # assign grade to 1
        # setup assignment2
        self.assignment2 = classroom_manager.Assignment("assignment2", 100.0)
        # assign grade to 2
        # setup assignment3
        self.assignment3 = classroom_manager.Assignment("assignment3", 100.0)
        # no grade is assigned is None
        # add the assignments to student assignments properties
        self.student.submit_assignment(self.assignment1)
        self.student.submit_assignment(self.assignment2)
        self.student.submit_assignment(self.assignment3)

        # check if there are 3 assignments in the student assignments
        self.assertEqual(3, len(self.student.get_assignments()))

        # get the assignment named testuser1
        self.assertEqual(self.assignment1, self.student.get_assignment("assignment1"))

        # check if assignment name is correct
        self.assertEqual("assignment1", self.student.get_assignment("assignment1").name)

        # check if assignment 1 has none grade
        self.assertEqual(None, self.student.get_assignment("assignment1").grade)

        # check if assignment 2 name is correct
        self.assertEqual("assignment2", self.student.get_assignment("assignment2").name)

        # check if assignment 2 has none grade
        self.assertEqual(None, self.student.get_assignment("assignment2").grade)

        # check if assignment 3 name is correct
        self.assertEqual("assignment3", self.student.get_assignment("assignment3").name)

        # check if assignment 3 has none grade
        self.assertEqual(None, self.student.get_assignment("assignment3").grade)

        # get avarege
        self.assertEqual(0, self.student.get_average())