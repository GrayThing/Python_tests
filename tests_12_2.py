import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
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
# Доработка функции
        ps_speed_list = sorted([(value.speed, value) for key, value in finishers.items()], reverse=True)
        finishers_improved = {}
        for index in range(len(ps_speed_list)):
            finishers_improved.update({index + 1: ps_speed_list[index][1]})
        if finishers_improved != finishers:
            print('Ошибка работы изначального кода. Используем запасной')
            return finishers_improved
# Конец доработки функции
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_first(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update({'first_tournament': tournament_1.start()})
        self.assertTrue(self.all_results['first_tournament'][2] == 'Ник')

    def test_second(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update({'second_tournament': tournament_2.start()})
        self.assertTrue(self.all_results['second_tournament'][2] == 'Ник')

    def test_third(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update({'third_tournament': tournament_3.start()})
        self.assertTrue(self.all_results['third_tournament'][3] == 'Ник')

    def tearDown(self):
        for key, value in self.all_results.items():
            try:
                third_value = value[3].speed
            except:
                third_value = 0
            self.assertTrue(value[1].speed > value[2].speed > third_value,
                            'Участник с меньшей скоростью чем другой не может быть быстрее него')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result = {}
            for place, runner in value.items():
                result.update({place: runner.name})
            print(result)


if __name__ == '__main__':
    unittest.main()

