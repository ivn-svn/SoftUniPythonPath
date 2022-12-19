from unittest import TestCase
from cat import Cat


class CatTests(TestCase):
    NAME = "Test Cat"

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)
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
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test__fed__expect_true_after_eating(self):
        #         • Cat is fed after eating
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test__fed__if_already_raise_error(self):
        #         • Cat cannot eat if already fed, raises an error
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
            '''
            In Python, the with statement replaces a try-catch block with a concise shorthand. 
            More importantly, it ensures closing resources right after processing them. 
            A common example of using the with statement is reading or writing to a file.
            '''
        self.assertIsNotNone(ex)

    def test__cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
            '''
            Assert if not sleepy == True
            '''
        self.assertIsNotNone(ex)

    def test__not__sleepy_if_slept(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    TestCase.unittest.main()
