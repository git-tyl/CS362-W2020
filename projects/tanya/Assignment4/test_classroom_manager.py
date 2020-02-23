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
        print("test self")