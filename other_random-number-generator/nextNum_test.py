import unittest
import nextNum


class RandomGenTestCase(unittest.TestCase):
    def setUp(self):
        self.args = None

    def tearDown(self):
        self.args = None

    def test_case_sample_isin(self):
        nums = [-1, 0, 1, 2, 3]
        prob = [0.01, 0.3, 0.58, 0.1, 0.01]
        random_gen = nextNum.RandomGen(nums, prob)

        result = random_gen.next_num()
        self.assertIn(result, nums)

    def test_case_all_prob_zero_except_for_one(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        prob = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        random_gen = nextNum.RandomGen(nums, prob)

        expect = 2
        result = random_gen.next_num()
        self.assertEqual(expect, result)

    def test_case_run_many_rounds(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        prob = [0.01, 0.05, 0.25, 0.40, 0.02, 0.07, 0.01, 0.12, 0.06, 0.01]
        n_rounds = 10000000
        random_gen = nextNum.RandomGen(nums, prob)

        expect = {k:round(v, 2) for k, v in zip(nums, prob)}
        result = {k:round(v/n_rounds, 2) for k,v in random_gen.next_stat(n_rounds).items()}
        self.assertDictEqual(expect, result)

    def test_assert_1_input_length_not_match(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        prob = [1.0]
        with self.assertRaisesRegex(AssertionError, "Lengths of inputs are not the same") as _: 
            nextNum.RandomGen(nums, prob)

    def test_assert_2_all_prob_zero(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        prob = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        with self.assertRaisesRegex(AssertionError, "There must be at least one number with non-zero probability") as _: 
            nextNum.RandomGen(nums, prob)

    def test_assert_3_duplicate_number(self):
        nums = [-1, -1, 1, 3, 4, 5, 6, 7, 8, 9]
        prob = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        with self.assertRaisesRegex(AssertionError, 'There are duplicate numbers \((-[0-9]*|[0-9]*)\) in random_nums') as _:
            nextNum.RandomGen(nums, prob)
    
    def test_assert_4_negative_prob(self):
        nums = [-1, -1, 1, 3, 4, 5, 6, 7, 8, 9]
        prob = [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        with self.assertRaisesRegex(AssertionError, f'Probability can not be negative \((-[0-9]*\.*[0-9]*)\)') as _:
            nextNum.RandomGen(nums, prob)

suite = unittest.TestLoader().loadTestsFromTestCase(RandomGenTestCase)

if __name__ == '__main__':

    unittest.main(verbosity=2)
