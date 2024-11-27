import runner
import unittest

class RunnerTest(unittest.TestCase):
    
    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        rw = runner.Runner("man")
        for i in range(10):
            rw.walk()
        self.assertEqual(rw.distance, 50)


    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        rr = runner.Runner("car")
        for i in range(10):
            rr.run()
        self.assertEqual(rr.distance, 100)


    def test_challenge(self):
        """
        Test for two functions in runner
        :return:
        """
        rr_ = runner.Runner("bus")
        rw_ = runner.Runner("train")
        for i in range(10):
            rr_.run()
            rw_.walk()
        self.assertNotEqual(rr_.distance, rw_.distance)


if __name__ == "__main__":
    unittest.main()
