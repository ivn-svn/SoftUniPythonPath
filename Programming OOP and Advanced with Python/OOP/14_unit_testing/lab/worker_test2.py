from worker import Worker
from unittest import TestCase
import unittest


class WorkerTests(TestCase):

    NAME = "Test Worker"
    SALARY = 1024
    ENERGY = 2

    '''
    Create the following tests:
        Test if the worker is initialized with the correct name, salary, and energy
        Test if the worker's energy is incremented after the rest method is calkd
        Test if an error is raised if the worker tries to work with negative energy or equal to O
        Test if the worker's money is increased by his salary correctly after the work method is called
        Test if the worker's energy is decreased after the work method is called
        Test if the get_info method returns the proper string with correct values
    '''

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_if__worker_init__with_correct_name_salary_energy(self):
        # Test if the worker is initialized with the correct name, salary, and energy
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if__rest__increments_energy(self):
        #     Test if the worker's energy is incremented after the rest method is calkd
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_if__work__with_negative_energy_or_equal_0_raises_error(self):
        #     Test if an error is raised if the worker tries to work with negative energy or equal to O
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
            '''
            In Python, the with statement replaces a try-catch block with a concise shorthand. 
            More importantly, it ensures closing resources right after processing them. 
            '''
        self.assertIsNotNone(ex)

    def test_if__work__increases_worker_salary_correctly_after_work(self):
        # Test if the worker's money is increased by his salary correctly after the work method is called
        self.worker.work()
        self.worker.work()
        expected_salary_after_work = self.SALARY * 2
        actual_salary_after_work = self.worker.money
        self.assertEqual(expected_salary_after_work, actual_salary_after_work)

    def test_if__work__increases_worker_salary_correctly_after_work(self):
        # Test if the worker's energy is decreased after the work method is called
        self.worker.work()
        self.worker.work()
        expected_salary_after_work = self.SALARY * 2
        actual_salary_after_work = self.worker.money
        self.assertEqual(expected_salary_after_work, actual_salary_after_work)

    def test_if__work__decreases_worker_energy_after_work(self):
        # Test if the worker's energy is decreased after the work method is called
        self.worker.work()
        actual_energy_after_work = self.worker.energy
        expected_energy_after_work = self.ENERGY - 1
        self.assertEqual(expected_energy_after_work, actual_energy_after_work)

    def test___get_info__correct(self):
        # Test if the get_info method returns the proper string with correct values
        actual_get_info_output = self.worker.get_info()
        expected_get_info_output = f"{self.NAME} has saved {0} money."
        self.assertEqual(expected_get_info_output, actual_get_info_output)


if __name__ == "__main__":
    unittest.main()
