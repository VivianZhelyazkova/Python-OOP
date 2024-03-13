from project.student import Student
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

    def test_enroll_with_existing_course(self):
        expected_message = "Course already added. Notes have been updated."
        expected_courses = {"Python": ["a", "b", "c", "f"]}
        actual_message = self.student.enroll("Python", ["f"])
        actual_courses = self.student.courses
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(expected_courses, actual_courses)

    def test_enroll_with_non_existent_course_and_notes_Y(self):
        expected_message = "Course and course notes have been added."
        expected_courses = {"Python": ["a", "b", "c"], "JavaScript": ["f"]}
        actual_message = self.student.enroll("JavaScript", ["f"], "Y")
        actual_courses = self.student.courses
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(expected_courses, actual_courses)

    def test_enroll_with_non_existent_course_and_notes_empty(self):
        expected_message = "Course and course notes have been added."
        expected_courses = {"Python": ["a", "b", "c"], "JavaScript": ["f"]}
        actual_message = self.student.enroll("JavaScript", ["f"], "")
        actual_courses = self.student.courses
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(expected_courses, actual_courses)

    def test_enroll_with_non_existent_course_no_notes(self):
        expected_message = "Course has been added."
        expected_courses = {"Python": ["a", "b", "c"], "JavaScript": []}
        actual_message = self.student.enroll("JavaScript", ["f"], "N")
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(expected_message, actual_message)

    def test_add_notes_with_existing_course(self):
        expected_message = "Notes have been updated"
        expected_courses = {"Python": ["a", "b", "c", "d"]}
        actual_message = self.student.add_notes("Python", "d")
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(expected_message, actual_message)

    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("JavaScript", "d")
        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        expected_message = "Course has been removed"
        expected_courses = {}
        actual_message = self.student.leave_course("Python")
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(expected_message, actual_message)

    def test_leave_raises(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course("JavaScript")
        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")
