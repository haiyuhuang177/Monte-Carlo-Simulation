import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# example
num_samples = 10000
pi_estimate = monte_carlo_pi(num_samples)
print(f"Estimated value of π with {num_samples} samples: {pi_estimate}")


def visualize_monte_carlo_pi(num_samples):
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    plt.figure(figsize=(6, 6))
    plt.scatter(inside_x, inside_y, color='green', marker='.')
    plt.scatter(outside_x, outside_y, color='red', marker='.')
    plt.title(f'Monte Carlo Estimation of π with {num_samples} samples')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# example
visualize_monte_carlo_pi(1000)
