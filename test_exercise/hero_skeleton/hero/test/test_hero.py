from hero.project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Mrossie", 1000, 100.0, 100.0)
        self.enemy = Hero("Vivi", 1000, 100.0, 100.0)

    def test_init(self):
        actual = [self.hero.username, self.hero.level, self.hero.health, self.hero.damage]
        expected = ["Mrossie", 1000, 100.0, 100.0]
        self.assertEqual(actual, expected)

    def test_battle_with_yourself(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)
        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_battle_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_negative_health(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_with_zero_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual(str(error.exception), f"You cannot fight Vivi. He needs to rest")

    def test_battle_enemy_with_negative_health(self):
        self.enemy.health = -1
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual(str(error.exception), f"You cannot fight Vivi. He needs to rest")

    def test_battle_draw(self):
        expected = "Draw"
        actual = self.hero.battle(self.enemy)
        self.assertEqual(actual, expected)

    def test_battle_hero_wins(self):
        self.enemy.damage = 1.0
        self.enemy.level = 1
        expected = "You win"
        actual = self.hero.battle(self.enemy)
        expected_stats = [1001, 104.0, 105.0]
        actual_stats = [self.hero.level, self.hero.health, self.hero.damage]
        self.assertEqual(actual, expected)
        self.assertEqual(actual_stats, expected_stats)

    def test_battle_enemy_wins(self):
        self.hero.damage = 1.0
        self.hero.level = 1
        expected = "You lose"
        expected_hero_stats = [1, (100.0 - self.enemy.level * self.enemy.damage), 1.0]
        expected_enemy_stats = [1001, 104.0, 105.0]
        actual = self.hero.battle(self.enemy)
        actual_hero_stats = [self.hero.level, self.hero.health, self.hero.damage]
        actual_enemy_stats = [self.enemy.level, self.enemy.health, self.enemy.damage]

        self.assertEqual(actual, expected)
        self.assertEqual(actual_enemy_stats, expected_enemy_stats)
        self.assertEqual(actual_hero_stats, expected_hero_stats)

    def test_str(self):
        expected = f"Hero Mrossie: 1000 lvl\n" \
                   f"Health: 100.0\n" \
                   f"Damage: 100.0\n"
        actual = self.hero.__str__()
        self.assertEqual(expected, actual)
