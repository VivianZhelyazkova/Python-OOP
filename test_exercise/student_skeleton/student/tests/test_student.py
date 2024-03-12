from student.project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Pesho", {"Python": ["a", "b", "c"]})

    def test_init_with_no_courses(self):
        s = Student("Gosho", None)
        expected = ["Gosho", {}]
        actual = [s.name, s.courses]
        self.assertEqual(expected, actual)

    def test_init_with_courses(self):
        expected = ["Pesho", {"Python": ["a", "b", "c"]}]
        actual = [self.student.name, self.student.courses]
        self.assertEqual(expected, actual)

    
