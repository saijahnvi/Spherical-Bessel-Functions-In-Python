# Spherical-Bessel-Functions-In-Python
This explores the code of bessel func of the First Kind using the recurrence relation:$$j_{l+1}(x) = \frac{2l + 1}{x} j_l(x) - j_{l-1}(x)$$It demonstrates why standard upward recurrence suffers from severe numerical instability for small arguments ($x \ll l$) and shows how downward recurrence (Miller's Algorithm) resolves loss of significance.

---

## Technical Overview

### 1. Upward Recurrence (Forward Recursion)
Starting from known initial values ($j_0(x) = \frac{\sin x}{x}$ and $j_1(x) = \frac{\sin x}{x^2} - \frac{\cos x}{x}$), each higher order is calculated sequentially:

$$j_{l+1}(x) = \frac{2l + 1}{x} j_l(x) - j_{l-1}(x)$$

* **Problem:** When $x < l$, $j_l(x)$ decays rapidly ($j_l(x) \propto x^l$). The term $\frac{2l+1}{x} j_l(x)$ causes catastrophic cancellation and round-off error amplification. Errors grow exponentially as $l$ increases.

### 2. Downward Recurrence (Miller's Algorithm)
Instead of starting at $l=0$, downward recurrence starts at an arbitrarily high degree $l_{\text{start}} \gg l$ with arbitrary initial conditions ($j_{l_{\text{start}}} = 0, j_{l_{\text{start}}-1} = 1$) and iterates backward using:

$$j_{l-1}(x) = \frac{2l + 1}{x} j_l(x) - j_{l+1}(x)$$

* **Advantage:** Because $j_l(x)$ decreases as $l$ increases, moving backward dampens numerical errors exponentially, making the algorithm extremely stable.
* **Normalization:** The relative values are rescaled at the end using the exact analytical value of $j_0(x) = \frac{\sin x}{x}$.

---

## Code Sections Explained

### Script 1: Downward Recurrence (Miller's Algorithm)
Implementation of stable downward recurrence to compute $j_0(x)$ up to $j_l(x)$.

* **Key Steps:**
  1. Computes a safe starting index: $l_{\text{start}} = l + \lceil\sqrt{10l}\rceil$.
  2. Iterates backward down to $l=0$.
  3. Rescales the array using the exact ground-truth value of $j_0(x)$.

---

### Script 2: Single-Step Recurrence Comparison
Demonstrates the recurrence formula explicitly at $l = 10, x = 10$ using `scipy.special.spherical_jn`:

* Computes upward prediction ($j_{11}$ from $j_{10}, j_9$) vs. downward prediction ($j_9$ from $j_{10}, j_{11}$).
* Outputs difference logs comparing standard values with recurrence estimates to show immediate precision loss.

---

### Script 3: Unstable Upward Recurrence
Computes $j_l(x)$ sequentially from $l = 0$ to $l = 10$ for $x = 0.1$.

* **Key Issue:** For $x = 0.1$ and $l = 10$, the upward iteration accumulates significant floating-point error due to division by $x = 0.1$ in every step, causing severe divergence from true values at higher $l$.

---

## Dependencies

* Python 3.x
* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)

To install dependencies:
```bash
pip install numpy scipy
