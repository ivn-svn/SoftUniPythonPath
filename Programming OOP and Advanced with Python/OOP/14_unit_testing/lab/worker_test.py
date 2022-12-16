from unittest import TestCase

from worker import Worker


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
        Testif the worker's energy is decreased after the work method is called
        Test if the get_info method returns the proper string with correct values
    '''

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__work__when_enough_energy__expect_money_to_be_increased(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
            '''
            In Python, the with statement replaces a try-catch block with a concise shorthand. 
            More importantly, it ensures closing resources right after processing them. 
            A common example of using the with statement is reading or writing to a file.
            '''
        self.assertIsNotNone(ex)

    def test__work__when_enough_energy_expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test__work__when_enough_energy_expect_energy_to_decrement(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f"{self.NAME} has saved {0} money."
        self.assertEqual(expected_info, actual_info)


if __name__ == "__main__":
    TestCase.unittest.main()
