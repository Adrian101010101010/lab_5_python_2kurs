# pylint: skip-file
import unittest

from lab5.src.lab5 import topological_sort, optimal_order


class TestOptimalOrder(unittest.TestCase):

    def test_topological_sort(self):
        graph = {'a': ['b', 'c'],
                 'b': ['d'],
                 'c': ['d'],
                 'd': []}
        result = topological_sort(graph)
        expected_result = ['a', 'b', 'c', 'd']
        self.assertEqual(result, expected_result)

    def test_optimal_order(self):
        input_data = [
            "visa foreignpassport",
            "visa hotel",
            "visa bankstatement",
            "bankstatement nationalpassport",
            "hotel creditcard",
            "creditcard nationalpassport",
            "nationalpassport birthcertificate",
            "foreignpassport nationalpassport",
            "foreignpassport militarycertificate",
            "militarycertificate nationalpassport",
        ]

        result = optimal_order(input_data)
        expected_result = [
            "birthcertificate",
            "nationalpassport",
            "bankstatement",
            "creditcard",
            "militarycertificate",
            "hotel",
            "foreignpassport",
            "visa",
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
