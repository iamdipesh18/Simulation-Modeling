import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Constants
iterator = 256  # Number of random numbers to generate
a = 29  # Multiplier
b = 37  # Increment
p = 256  # Modulus
n = 8  # Number of bins for Chi-Square test
x02 = 0  # Chi-Square statistic initialization
critical_value = chi2.ppf(1 - 0.05, df=n - 1)  # Corrected critical value

# Initialize arrays
r = np.ones(iterator, dtype=int)  # Array to store generated random numbers
ei = iterator / n  # Expected frequency for each bin
c = np.zeros(n, dtype=int)  # Bin counts

# Initial seed
r[0] = 17

# Generate random numbers using LCG
for i in range(1, iterator):
    r[i] = (r[i - 1] * a + b) % p

# Bin the generated numbers using numpy's histogram
bin_edges = np.linspace(0, p, n + 1)  # Create bin edges from 0 to 256 with 8 bins
c, _ = np.histogram(r, bins=bin_edges)  # Count occurrences in each bin

# Compute Chi-Square statistic
x02 = np.sum(((c - ei) ** 2) / ei)

# Print results
print("Values of r:", r)
print("Values of c (bin frequencies):", c)
print("Value of Chi-Square statistic (x02):", x02)
print("The critical value is", critical_value)
print("Chi square test passed" if x02 <= critical_value else "Chi square test failed")

# Visualize the generated random numbers
plt.figure()
plt.plot(r, label="Generated Sequence (r)")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.title("LCG Generated Sequence")
plt.legend()
plt.show()
