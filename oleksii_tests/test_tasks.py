"""Testing tasks"""

import unittest
import tasks


class TestTasks(unittest.TestCase):
    """Testing tasks package"""

    def test_task_88v(self):
        """Testing task_88v function"""
        self.assertEqual(tasks.task_88v(371239), 971233)
        self.assertEqual(tasks.task_88v(5), 5)

        with self.assertRaises(ValueError):
            tasks.task_88v(0)
        with self.assertRaises(ValueError):
            tasks.task_88v(-371239)
        with self.assertRaises(ValueError):
            tasks.task_88v("379")
        with self.assertRaises(ValueError):
            tasks.task_88v(None)
        with self.assertRaises(ValueError):
            tasks.task_88v([379])
        with self.assertRaises(ValueError):
            tasks.task_88v([379,379])


    def test_task_88g(self):
        """Testing task_88g function"""
        self.assertEqual(tasks.task_88g(371239), 13712391)
        self.assertEqual(tasks.task_88g(5), 151)

        with self.assertRaises(ValueError):
            tasks.task_88g(0)
        with self.assertRaises(ValueError):
            tasks.task_88g(-371239)
        with self.assertRaises(ValueError):
            tasks.task_88g("379")
        with self.assertRaises(ValueError):
            tasks.task_88g(None)
        with self.assertRaises(ValueError):
            tasks.task_88g([379])
        with self.assertRaises(ValueError):
            tasks.task_88g([379,379])


    def test_task_332(self):
        """Testing task_332 function"""
        self.assertCountEqual(tasks.task_332(31), (5, 1, 2, 1))

        with self.assertRaises(ValueError):
            tasks.task_332(0)
        with self.assertRaises(ValueError):
            tasks.task_332(-371239)
        with self.assertRaises(ValueError):
            tasks.task_332("379")
        with self.assertRaises(ValueError):
            tasks.task_332(None)
        with self.assertRaises(ValueError):
            tasks.task_332([379])
        with self.assertRaises(ValueError):
            tasks.task_332([379,379])


if __name__ == "__main__":
    unittest.main()
