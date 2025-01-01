import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):

    #is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name = Runner('Name1')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name = Runner('Name2')
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name_1 = Runner('Name1')
        name_2 = Runner('Name2')
        for i in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


class TournamentTest(unittest.TestCase):

    #is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = Runner("Óñýéí", 10)
        self.runner2 = Runner("Àíäðåéêà", 9)
        self.runner3 = Runner("Íèê", 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f"{i}: {j}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        result = tour.start()
        self.all_results['TestMethod 1'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Íèê')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        result = tour.start()
        self.all_results['TestMethod 2'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Íèê')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        tour = Tournament(90, self.runner2, self.runner3, self.runner1)
        result = tour.start()
        self.all_results['TestMethod 3'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Íèê')


if __name__ == "__main__":
    unittest.main()
