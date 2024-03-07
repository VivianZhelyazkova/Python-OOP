import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    def test_arguments_type(self):
        worker = Worker("a", 1, 1)
        self.assertEqual(worker.name, "a")
        self.assertEqual(worker.salary, 1)
        self.assertEqual(worker.energy, 1)

    def test_energy_incremented_after_the_rest(self):
        energy = 1
        worker = Worker("a", 1, energy)
        worker.rest()
        self.assertEqual(worker.energy, 2)

    def test_error_is_raised_with_zero_or_negative_energy(self):
        worker = Worker("a", 1, -1)
        with self.assertRaises(Exception) as E:
            worker.work()
        self.assertEqual(str(E.exception), 'Not enough energy.')

    def test_salary_increased_correctly(self):
        salary = 1
        worker = Worker("a", salary, 1)
        worker.work()
        self.assertEqual(worker.money, salary)

    def test_energy_decreased_after_work(self):
        energy = 1
        worker = Worker("a", 1, energy)
        worker.work()
        self.assertEqual(worker.energy, 0)

    def test_get_info_returns_proper_string(self):
        name = "a"
        money = 0
        proper_string = f'{name} has saved {money} money.'
        worker = Worker(name, 1, 1)
        self.assertEqual(worker.get_info(), proper_string)


if __name__ == '__main__':
    unittest.main()
