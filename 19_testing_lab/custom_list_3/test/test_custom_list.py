from custom_list_3.custom_list import IntegerList
from unittest import TestCase, main

class TestIntegerList(TestCase):

    def setUp(self):
        self.cl = IntegerList(1,2,3)

    def test_init_int_value(self):
        self.assertListEqual([1,2,3], self.cl._IntegerList__data)

    def test_non_integer_value(self):
        new_list_element = IntegerList([1,2,3], 4.7, 'abc', 5)
        self.assertEqual([5], new_list_element._IntegerList__data)

    def test_get_data_return(self):
        self.cl.get_data()
        self.assertListEqual([1,2,3], self.cl.get_data())
        self.assertIs(self.cl._IntegerList__data, self.cl.get_data())

    def test_add_element_raise_value_error(self):
        self.assertListEqual([1,2,3], self.cl._IntegerList__data)

        with self.assertRaises(ValueError) as ex:

            self.cl.add('abc')
            self.cl.add([1,2,3])
            self.cl.add(7.7)

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertListEqual([1,2,3], self.cl._IntegerList__data)

    def test_add_int_list(self):
        self.assertListEqual([1,2,3], self.cl._IntegerList__data)
        self.cl.add(5)

        self.assertListEqual([1,2,3,5], self.cl._IntegerList__data)

    def test_remove_index_raises_index_error(self):
        len_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ei:
            self.cl.remove_index(len_index)
            len_index += 1
            self.cl.remove_index(len_index)
        self.assertEqual("Index is out of range", str(ei.exception))

    def test_remove_valid_index(self):

        self.assertListEqual([1,2,3], self.cl._IntegerList__data)
        self.cl.remove_index(1)
        self.assertEqual([1,3], self.cl._IntegerList__data)

    def test_get_out_index_element(self):
        len_index = len(self.cl._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            len_index += 3
            self.cl.get(len_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_element_by_index(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)
        self.cl.get(2)
        self.assertEqual(3, self.cl.get(2))
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_insert_index_raises_index_error(self):
        len_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.insert(len_index, 4)
            len_index += 1
            self.cl.insert(len_index, 5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_raises_value_error(self):

        with self.assertRaises(ValueError) as ex:

            self.cl.insert(1, (1, 2))
            self.cl.insert(2, 'abc')
            self.cl.insert(0, 1.1)
            self.cl.insert(1, [1,2,3])


        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)
        self.cl.insert(1,5)
        self.assertEqual([1,5,2,3], self.cl._IntegerList__data)

    def test_get_biggest_sorted(self):
        new_el = IntegerList(1,13,1000,8, 7, 6)
        new_el.get_biggest()
        self.assertEqual(1000, new_el.get_biggest())

    def test_get_index(self):
        self.assertIn(1, self.cl._IntegerList__data)
        self.assertEqual(1, self.cl._IntegerList__data[0])
        result = self.cl.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":

    main()
