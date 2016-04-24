import unittest

import numpy as np

from code.permutation import _test_statistic, pt


class PermutationTest(unittest.TestCase):

    def test_statistic_one(self):
        m = 3
        a = np.ones(m)
        b = np.zeros(m)
        arr = np.append(a, b)
        self.assertEquals(1.0, _test_statistic(arr, m))

    def test_p_value_zero(self):
        np.random.seed(42)
        N, m = 50, 25
        t = np.random.normal(loc=10, size=m)
        c = np.random.normal(loc=5, size=N-m)
        arr = np.append(t, c)
        self.assertEquals(0.0, pt(arr, m))
        self.assertEquals(0.0, pt(arr, m, two_tailed=False))

    def test_p_value_one(self):
        N, m = 10, 5
        arr = np.ones(N)
        self.assertEquals(1.0, pt(arr, m))
