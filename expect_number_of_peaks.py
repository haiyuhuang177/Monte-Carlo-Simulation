# Monte Carlo simulation to estimate the expected number of peaks in n numbers
# A number is a sequence is said to be a peak if it is larger than its neighbors
import random
n = 14
NUM_TRIALS = 10000
numbers = list(range(1,n+1))
total_max = 0
for i in range(NUM_TRIALS):
  perm = random.sample(range(1, n+1), n)
  num_max = 0
  for j in range(n):
    left_peak, right_peak = False, False
    if j == 0 or perm[j] > perm[j-1]:
      left_peak = True
    if j == n-1 or perm[j] > perm[j+1]:
      right_peak = True
    if left_peak and right_peak:
      num_max += 1
  total_max += num_max
print("expected number of maximum is ", total_max / NUM_TRIALS)
