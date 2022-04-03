# **Random Number Generator**

## **Description**

Generate a random number from a given list of numbers based on their corresponding occurence probabilities. Therefore, when the method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities.

<br>

## **Usage**

### **Notice**
1. Lengths of candidate numbers & occurence probabilities must be the same.
2. Candidate numbers can be either integers or float numbers.
3. There can not be any duplicate number in candidate numbers.
4. The occurence probabilities must be positive.
5. The occurence probabilities don't need to be smaller than 1.0 since there is a normalization step to address this problem (to get relative probabilities).
6. The occurence probabilities can be zero, but there must be at least one number with non-zero probability. <br>

### **Demo**
```
import nextNum

# setup candidate numbers and occurence probabilities
nums = [-1, 0, 1, 2, 3]
prob = [0.01, 0.3, 0.58, 0.1, 0.01]

# initialize the generator
random_gen = nextNum.RandomGen(nums, prob)

# randomly generate a number from nums based on prob
result = random_gen.next_num(built_funcs=False)

# run next_num() method n_rounds times to inspect the distribution of selected numbers
n_rounds = 1000000
result_stat = random_gen.next_stat(n_rounds)
```

### **Unit Test** 
Run `python -m nextNum_test` to execute several unit tests and get the distribution of the selected candidate numbers for a sample case.