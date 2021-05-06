from extended_list import IntegerList
import unittest


class ListTests(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_the_initialization(self):
        new_list = IntegerList(1,2,3,4,5)
        self.assertEqual(new_list.get_data(),[1,2,3,4,5])


    def test_add(self):
        result = self.list.add(2)
        expected = [2]
        self.assertEqual(result,expected)

    def test_add_raises_value_error_if_not_integer_is_given(self):
        self.assertRaises(ValueError,self.list.add,"baba")

    def test_remove_by_index(self):
        self.list.add(11)
        el = self.list.remove_index(0)
        self.assertEqual(el,11)

    def test_remove_by_index_with_index_out_of_range(self):
        self.assertRaises(IndexError,self.list.remove_index,1)

    def test_init_takes_only_integers(self):
        new_list = IntegerList("baba","dqdo",1,2,"pechka")
        self.assertEqual(new_list.get_data(),[1,2])

    def test_get_returning_right_elements(self):
        self.list.add(2)
        self.assertEqual(self.list.get(0),2)

    def test_get_raises_index_error(self):
        self.assertRaises(IndexError,self.list.get,3)

    def test_insert_raises_index_error(self):
        self.assertRaises(IndexError,self.list.insert,3,2)

    def test_insert_raises_value_error(self):
        self.list.add(1)
        self.assertRaises(ValueError,self.list.insert,0,"baba")

    def test_insert_works_properly(self):
        self.list.add(1)
        self.list.insert(0,42)
        self.assertEqual(self.list.get_data(),[42,1])

    def test_get_biggest_el(self):
        self.list.add(1)
        self.list.add(10)
        self.assertEqual(self.list.get_biggest(),10)

    def test_get_index(self):
        self.list.add(1)
        self.assertEqual(self.list.get_index(1),0)

if __name__ == '__main__':
    unittest.main()