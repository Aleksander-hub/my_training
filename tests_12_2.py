import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрейка", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f"{i}: {j}")

    def test_start_1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        result = tour.start()
        self.all_results['TestMethod 1'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')

    def test_start_2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        result = tour.start()
        self.all_results['TestMethod 2'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')

    def test_start_3(self):
        tour = Tournament(90, self.runner2, self.runner3, self.runner1)
        result = tour.start()
        self.all_results['TestMethod 3'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')


if __name__ == "__main__":
    unittest.main()