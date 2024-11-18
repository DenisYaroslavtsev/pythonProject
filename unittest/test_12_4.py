import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Ivan', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f'"test walk" выполен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner = Runner(228, 10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner_1 = Runner('Ivan test challenge')
        runner_2 = Runner('Iven test challenge_2')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
