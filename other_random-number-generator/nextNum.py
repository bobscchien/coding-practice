from typing import List, Tuple, Union

import time
import random
from collections import defaultdict


class RandomGen(object):
    def __init__(self, random_nums: Union[List[float], Tuple[float]], raw_probabilities: Union[List[float], Tuple[float]]):
        """
        Parameters:
        - random_nums: candidate numbers that can be chosen and returned
        - raw_probabilities: probability of the occurence of random_nums
        """
        ### Assertion
        
        # make sure that every number in random_nums has its own probability
        assert len(random_nums) == len(raw_probabilities), 'Lengths of inputs are not the same'
        
        # make sure that
        # (1) there is no duplicate number
        # (2) every probability is greater than 0.0
        # (3) at least one number has non-zero probability
        dup_test = defaultdict(int)
        pos_counter = 0.0
        for i, n in enumerate(random_nums):
            dup_test[n] += 1
            pos_counter += raw_probabilities[i]
            assert dup_test[n] <= 1, f'There are duplicate numbers ({n}) in random_nums'
            assert raw_probabilities[i] >= 0.0, f'Probability can not be negative ({raw_probabilities[i]})'
        assert pos_counter > 0.0, f'There must be at least one number with non-zero probability'
            
        ### Initialization
        
        # compute the accumulated probabilities
        cum_probabilities = [0.0, ]
        for i, p in enumerate(raw_probabilities):
            cum = cum_probabilities[i] + p
            cum_probabilities.append(cum)
        cum_probabilities = cum_probabilities[1:]
        
        # normalize and make sure that the summation of num_probabilities is equal to 1.0
        max_prob = cum_probabilities[-1]
        cum_probabilities = [p / max_prob for p in cum_probabilities]

        # Values that may be returned by next_num()
        self.nums = random_nums
        
        # Probability of the occurence of random_nums
        self.prob_raw = raw_probabilities
        self.prob_cum = cum_probabilities

    def next_num(self, built_funcs: bool = False) -> Union[int, float]:
        """Return one of the random_nums according to its raw_probabilities. 
        When this method is called multiple times over a long period, 
        it should return the numbers roughly with the initialized probabilities.
        
        Parameters:
        - built_funcs: whether to use built-in random.choices function or not.
        
        Returns:
        int: random selected number
        """
        # pseudo random number between 0 and 1.
        num = random.random()
        
        if built_funcs:
            # use built-in function with raw_probabilities
            return random.choices(self.nums, weights=self.prob_raw)[0]
        else:
            # binary search the index of the target random number (num)
            l, r = 0, len(self.prob_cum)-1

            while l < r:
                m = (l+r)//2

                if self.prob_cum[m] < num: 
                    l = m+1
                elif self.prob_cum[m] > num: 
                    r = m
                else: 
                    return self.nums[m]

            return self.nums[l]
        
    def next_stat(self, num_rounds: int = 100):
        """Execute next_num() function num_rounds times to examine the distribution of selected numbers
        
        Parameter:
        - num_rounds: rounds which this statistic process will run
        """
        s_time = time.time()
        
        # record
        stat = defaultdict(int)
        for _ in range(num_rounds):
            num = self.next_num()
            stat[num] += 1
        
        # output
        print(f'Total Time for {num_rounds} Rounds:', time.time()-s_time, 'Seconds \n')
        for i, n in enumerate(self.nums):
            print(f"{n:5}: Actual Prob = {stat[n]/num_rounds:.2f}, Raw Prob = {self.prob_raw[i]:.2f} ({stat[n]} times)")
            
        return stat
        