from project.truck_driver import TruckDriver

from unittest import TestCase, main

class TruckDriverTests(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver('Jonny', 1_000)


    def test_correct_initializing(self):                                                     # test 1                   : 1, x, x, x, x, x      16%
        self.assertEqual('Jonny', self.truck_driver.name)
        self.assertEqual(1_000, self.truck_driver.money_per_mile)
        self.assertEqual(100, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)


if __name__ == '__main__':
    main()
