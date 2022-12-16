from unittest import TestCase
from cat import Cat


class CatTests(TestCase):
    NAME = "Test Cat"
    FED = False
    SLEEPY = False

    def setUp(self) -> None:
        self.cat_name = Cat(self.NAME)

    '''
    Create a class CatTests
    In judge you need to submit just the CatTests class, with the unittest module imported.
    
    Create the following tests:
        • Cat's size is increased after eating
        • Cat is fed after eating
        • Cat cannot eat if already fed, raises an error
        • Cat cannot fall asleep if not fed, raises an error
        • Cat is not sleepy after sleeping
    '''

    def test__eat__expect_cat_size_increase_after_eating(self):
        #         • Cat's size is increased after eating
        expected_cat_size = self.size + 1
        actual_cat_size = self.size
        self.assertEqual(expected_cat_size, actual_cat_size)

    def test__fed__expect_cat_fed_after_eating(self):
        #         • Cat is fed after eating
        expected_cat_fed_value = True
        actual_cat_fed_value = self.FED
        self.assertEqual(expected_cat_fed_value, actual_cat_fed_value)

    def test__fed__if_already_raise_error(self):
        #         • Cat cannot eat if already fed, raises an error
        expected_cat_fed_value = True
        actual_cat_fed_value = self.FED
        with self.assertRaises(Exception) as ex:
            Cat.eat()
            '''
            In Python, the with statement replaces a try-catch block with a concise shorthand. 
            More importantly, it ensures closing resources right after processing them. 
            A common example of using the with statement is reading or writing to a file.
            '''
        self.assertIsNotNone(ex)

    def test__cannot_fall_asleep_if_fed(self):
        Cat.sleep()
        actual_cat_sleepy = self.sleepy
        self.assertIsNot(actual_cat_sleepy)
        Cat.eat()
        with self.assertRaises(AssertionError) as ex:
            Cat.sleep()
            '''
            Assert if not sleepy == True
            '''
        self.assertIsNotNone(ex)

    def test__not__sleepy_if_slept(self):
        Cat.sleep()
        actual_cat_sleepy = self.sleepy
        self.assertIsNot(actual_cat_sleepy)
        with self.assertRaises(AssertionError) as ex:
            Cat.sleep()
            '''
            Assert if not sleepy == True
            '''
        self.assertIs(ex)


if __name__ == "__main__":
    TestCase.unittest.main()
