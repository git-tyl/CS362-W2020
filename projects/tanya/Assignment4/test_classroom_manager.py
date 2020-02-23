from unittest import TestCase

import classroom_manager

class TestAssignment(TestCase):

    def setup(self):
        print("test setup")

    #test initiator for assignment
    def test_init(self):
        assignment = classroom_manager.Assignment("test", 5)
        self.assertEqual(5, assignment.max_score)
        self.assertEqual("test", assignment.name)

    # test initiator for assigment
    def test_init(self):
        assignment = classroom_manager.Assignment("test", 5)
        self.assertEqual(5, assignment.max_score)
        self.assertEqual("test", assignment.name)
        self.assertEqual(None, assignment.grade)

class TestAction_Student(TestCase):

    def setup(self):
        print("test self")