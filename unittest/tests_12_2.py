from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_husein_nik(self):
        tournament = Tournament(90, self.husein, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    def test_husein_andrey_nik(self):
        tournament = Tournament(90, self.husein, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()
