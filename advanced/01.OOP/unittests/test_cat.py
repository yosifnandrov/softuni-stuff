from cat import Cat
import unittest

class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("lolo")

    def test_cat_initialization(self):
        self.assertEqual(self.cat.name, "lolo")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size,0)

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size,1)

    def test_if_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_cant_eat_when_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exception:
            self.cat.eat()
        self.assertEqual(str(exception.exception),"Already fed.")

    def test_cat_cant_sleep_when_hungry(self):
        with self.assertRaises(Exception) as excep:
            self.cat.sleep()
        self.assertEqual(str(excep.exception),"Cannot sleep while hungry")


    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_if_eating_works_properly(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size,1)

    def test_if_sleeping_works_properly(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()
