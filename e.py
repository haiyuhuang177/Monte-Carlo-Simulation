# estimate e as the expected number of uniform (0,1) random variables
# with sum exceeding one for the first time

import random
#I = inf{i: X_1 + ... + X_i > 1}. EI = e. Use P(X_1 + ... + X_n < 1) = 1/n!
def estimate_e(num_trials):
    total_draws = 0

    for _ in range(num_trials):
        sum_random_numbers = 0
        draws = 0

        while sum_random_numbers <= 1:
            sum_random_numbers += random.uniform(0, 1)
            draws += 1

        total_draws += draws

    e_estimate = total_draws / num_trials
    return e_estimate

# Example usage
num_trials = 10000
e_estimate = estimate_e(num_trials)
print(f"Estimated value of e with {num_trials} trials: {e_estimate}")
