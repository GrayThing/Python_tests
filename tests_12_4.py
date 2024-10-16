import unittest
import logging


class Runner:
    is_frozen = False

    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    is_frozen = False

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    @unittest.skipIf(Runner.is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = Runner('Joe', -5)
            for i in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.error('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(Runner.is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = Runner(1, 6)
            for i in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.error('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(Runner.is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk_test_runner = Runner('Joe', 7)
        run_test_runner = Runner('Josh', 3)
        for i in range(10):
            walk_test_runner.walk()
            run_test_runner.run()
        self.assertNotEqual(walk_test_runner.distance, run_test_runner.distance)


print(__name__)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                            format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
