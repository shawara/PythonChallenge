import math
import unittest
import random

from .lottery_game import pick_balls


class FixedRandom:
    def __enter__(self):
        self.state = random.getstate()
        random.seed(0)

    def __exit__(self, *args):
        random.setstate(self.state)


class LotteryGameTest(unittest.TestCase):

    def setUp(self):
        with FixedRandom():
            self.picked_list = pick_balls()

    def test_result_length(self):
        self.assertEqual(10, len(self.picked_list))

    def test_is_sorted(self):
        for i in range(1, len(self.picked_list)):
            self.assertGreater(self.picked_list[i], self.picked_list[i - 1])

    def test_picked_with_seed(self):
        with FixedRandom():
            self.assertEqual(self.picked_list, pick_balls())

    def test_randomness(self):
        """
        each number has percent of (1/50) * 10 = .2 to be selected
        with 1000 iteration each number should occurs ~ .2 * 5000=1000
        I will test it with threshold of 150 so occurrence of any selected number should be within 850,1150
        :return: None
        """
        for _ in range(20):
            acc = {}
            for _ in range(5000):
                result = pick_balls()
                for v in result:
                    acc[v] = acc.get(v, 0) + 1

            for _, val in acc.items():
                self.assertLessEqual(abs(1000 - val), 150)
