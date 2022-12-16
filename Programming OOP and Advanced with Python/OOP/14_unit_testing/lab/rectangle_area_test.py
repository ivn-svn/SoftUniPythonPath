import unittest
import rectangle_area


class TestArea(unittest.TestCase):

    def test_area(self):
        f = 4
        s = rectangle_area.calculate_area_rectangle(2, 2)
        self.assertEqual(f, s)


if __name__ == '__main__':
    unittest.main()
