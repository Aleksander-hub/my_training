import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        name = Runner('Трамп')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name = Runner('Байден')
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        name_1 = Runner('Трамп')
        name_2 = Runner('Байден')
        for i in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


if __name__ == '__main__':
    unittest.main()
