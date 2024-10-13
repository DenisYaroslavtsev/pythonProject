import unittest
from runner import Runner
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Ivan test walk')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Ivan test run')
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Ivan test challenge')
        runner_2 = Runner('Iven test challenge_2')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()

        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.husein = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            results_str = {pos: runner.name for pos, runner in value.items()}
            print(f'{key}: {results_str}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_husein_nik(self):
        tournament = Tournament(90, self.husein, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_husein_andrey_nik(self):
        tournament = Tournament(90, self.husein, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()
