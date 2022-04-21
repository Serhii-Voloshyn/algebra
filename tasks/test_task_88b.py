import unittest
import task_88b


class TestTask88b(unittest.TestCase):

    def test_reverse_number(self):
        self.assertEqual(task_88b.reverse_number(379), 973)

        with self.assertRaises(AssertionError):
            task_88b.reverse_number(0)
            task_88b.reverse_number(-379)
            task_88b.reverse_number("379")
            task_88b.reverse_number(None)
            task_88b.reverse_number([379])
            task_88b.reverse_number([379,379])


if __name__ == "__main__":
    unittest.main()