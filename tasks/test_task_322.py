import unittest
import task_322


class TestTask322(unittest.TestCase):

    def test_get_number_with_largest_sum_of_divisors(self):
        self.assertEqual(task_322.get_number_with_largest_sum_of_divisors(1, 50), 48)
        self.assertEqual(task_322.get_number_with_largest_sum_of_divisors(1, 10000), 9240)

        with self.assertRaises(AssertionError):
            task_322.get_number_with_largest_sum_of_divisors(50, 1)
            task_322.get_number_with_largest_sum_of_divisors(50)
            task_322.get_number_with_largest_sum_of_divisors("1", 50)
            task_322.get_number_with_largest_sum_of_divisors(None, None)
            task_322.get_number_with_largest_sum_of_divisors((1, 50))
            task_322.get_number_with_largest_sum_of_divisors([1, 50])


    def test_get_divisors_list(self):
        self.assertEqual(task_322.get_divisors_list(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(task_322.get_divisors_list(1), [1])

        with self.assertRaises(AssertionError):
            task_322.get_divisors_list(-1)
            task_322.get_divisors_list(1)
            task_322.get_divisors_list(None)
            task_322.get_divisors_list((1))
            task_322.get_divisors_list([1, 50])
    

if __name__ == "__main__":
    unittest.main()