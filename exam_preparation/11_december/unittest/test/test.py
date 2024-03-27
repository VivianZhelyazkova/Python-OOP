from project.team import Team
import unittest


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Levski")
        self.other_team = Team("Ludogorec")

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
        result = self.team.add_member(John=25)
        self.assertEqual(result, "Successfully added: John")
        self.assertEqual(self.team.members, {"John": 25})

    def test_add_multiple_members(self):
        result = self.team.add_member(John=25, Jane=30)
        self.assertEqual(result, "Successfully added: John, Jane")
        self.assertEqual(self.team.members, {"John": 25, "Jane": 30})

    def test_add_existing_member(self):
        self.team.add_member(John=25)
        result = self.team.add_member(John=30, Pesho=30)
        self.assertEqual(result, "Successfully added: Pesho")
        self.assertEqual(self.team.members, {"John": 25, "Pesho": 30})

    def test_remove_member_existing_member(self):
        self.team.add_member(John=25)
        actual_return = self.team.remove_member("John")
        expected_return = f"Member John removed"
        expected = {}
        actual = self.team.members
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected, actual)

    def test_remove_non_existing_member(self):
        actual_return = self.team.remove_member("John")
        expected_return = f"Member with name John does not exist"
        expected = {}
        actual = self.team.members
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_gt_true(self):
        self.team.add_member(John=25)
        expected = True
        actual = self.team.__gt__(self.other_team)
        self.assertEqual(expected, actual)

    def test_gt_false(self):
        self.other_team.add_member(John=25)
        expected = False
        actual = self.team.__gt__(self.other_team)
        self.assertEqual(expected, actual)

    def test_len(self):
        self.team.add_member(John=25, Pesho=35)
        expected = 2
        actual = self.team.__len__()
        self.assertEqual(expected, actual)

    def test_add(self):
        self.team.add_member(John=25, Jane=30)
        self.other_team.add_member(Alice=28, Bob=32)
        new_team = self.team.__add__(self.other_team)
        self.assertIsInstance(new_team, Team)
        self.assertEqual(new_team.name, "LevskiLudogorec")
        self.assertEqual(new_team.members, {"John": 25, "Jane": 30, "Alice": 28, "Bob": 32})

    def test_str(self):
        self.team.add_member(John=25, Jane=30)
        expected = f"Team name: Levski\nMember: Jane - 30-years old\nMember: John - 25-years old"
        actual = self.team.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
