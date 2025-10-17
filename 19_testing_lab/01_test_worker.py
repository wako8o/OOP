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


from unittest import TestCase, main

class TestWorker(TestCase):

    def test_work_init(self):

        # Arrange
        worker = Worker('Emil', 100, 10)

        self.assertEqual('Emil', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_has_energy_raise_exception(self):

        # Arrange
        worker = Worker('Emil', 100, 0)
        self.assertEqual(0, worker.money)
        self.assertEqual(0, worker.energy)

        # Act & Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))
        # Assert

        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)


    def test_reset(self):

        # Arrange
        worker = Worker('Emil', 100, 10)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)
        worker.work()
        worker.rest()

        self.assertEqual(100, worker.money)
        self.assertEqual(10, worker.energy)

    def test_get_info(self):

        worker = Worker('Emil', 100, 10)
        result = worker.get_info()
        self.assertEqual(f'Emil has saved 0 money.', result)


if __name__ == '__main__':
    main()
