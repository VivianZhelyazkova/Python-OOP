from project.team import Team
import unittest


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Levski")

    def test_init(self):
        expected = ["Levski", {}]
        actual = [self.team.name, self.team.members]
        self.assertEqual(expected, actual)

    def test_name_setter_raise(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "424gkdg"
        self.assertEqual(str(error.exception), "Team Name can contain only letters!")

    def test_name_setter(self):
        self.team.name = "Ludogorec"
        expected = "Ludogorec"
        actual = self.team.name
        self.assertEqual(expected, actual)

    def test_add_member(self):
        