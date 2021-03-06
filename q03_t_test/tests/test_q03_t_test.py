from unittest import TestCase
from ..build import t_statistic
from inspect import getfullargspec
import pandas as pd
import numpy

df = pd.read_csv('data/house_pricing.csv')


class TestTTest(TestCase):
    def test_t_test(self):   # Input parameters tests
        args = getfullargspec(t_statistic)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_t_test_defaults(self):  # Input parameters default test
        args = getfullargspec(t_statistic)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_t_test_result_low_type(self):        # Return type tests
        pval, result = t_statistic(df)
        self.assertIsInstance(pval, float, "Expected data type for `Hypothesis Testing` is float you are returning\
                %s" % (type(pval)))

    def test_t_test_result_high_type(self):
        pval, result = t_statistic(df)
        self.assertIsInstance(result, numpy.bool_, "Expected data type for `Hypothesis Testing` is bool you are returning\
                %s" % (type(result)))

    def test_t_test_result_low_values(self):  # Return result values
        pval, result = t_statistic(df)
        self.assertAlmostEqual(pval, 0.51158698884870502, 3, "Return `Hypothesis Testing` value does not \
        match expected value")

    def test_t_test_result_high_values(self):
        pval, result = t_statistic(df)
        self.assertFalse(result, "Return `Hypothesis Testing` value does not match expected value")
