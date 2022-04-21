import unittest
import tasks


class TestTasks(unittest.TestCase):

    def test_task_88v(self):
        self.assertEqual(tasks.task_88v(371239), 971233)
        self.assertEqual(tasks.task_88v(5), 5)

        with self.assertRaises(ValueError):
            tasks.task_88v(0)
            tasks.task_88v(-379)
            tasks.task_88v("379")
            tasks.task_88v(None)
            tasks.task_88v([379])
            tasks.task_88v([379,379])


    def test_task_88g(self):
        self.assertEqual(tasks.task_88g(371239), 13712391)
        self.assertEqual(tasks.task_88g(5), 151)

        with self.assertRaises(ValueError):
            tasks.task_88g(0)
            tasks.task_88g(-379)
            tasks.task_88g("379")
            tasks.task_88g(None)
            tasks.task_88g([379])
            tasks.task_88g([379,379])


    def test_task_332(self):
        self.assertCountEqual(tasks.task_332(31), (5, 1, 2, 1))

        with self.assertRaises(ValueError):
            tasks.task_332(0)
            tasks.task_332(-379)
            tasks.task_332("379")
            tasks.task_332(None)
            tasks.task_332([379])
            tasks.task_332([379,379])


if __name__ == "__main__":
    unittest.main()