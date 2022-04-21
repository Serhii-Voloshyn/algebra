import unittest
import task_88a


class TestTask88a(unittest.TestCase):

    def test_is_3_in_square_of_number(self):
        self.assertTrue(task_88a.is_3_in_square_of_number(379))
        self.assertFalse(task_88a.is_3_in_square_of_number(3))

        with self.assertRaises(AssertionError):
            task_88a.is_3_in_square_of_number(0)
            task_88a.is_3_in_square_of_number(-379)
            task_88a.is_3_in_square_of_number("379")
            task_88a.is_3_in_square_of_number(None)
            task_88a.is_3_in_square_of_number([379])
            task_88a.is_3_in_square_of_number([379,379])


if __name__ == "__main__":
    unittest.main()