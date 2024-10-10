import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = Runner('Joe')
        for i in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = Runner('Joe')
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        walk_test_runner = Runner('Joe')
        run_test_runner = Runner('Josh')
        for i in range(10):
            walk_test_runner.walk()
            run_test_runner.run()
        self.assertNotEqual(walk_test_runner.distance, run_test_runner.distance)


if __name__ == '__main__':
    unittest.main()
