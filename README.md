# Spherical-Bessel-Functions-In-Python
This explores the code of bessel func of the First Kind using the recurrence relation:$$j_{l+1}(x) = \frac{2l + 1}{x} j_l(x) - j_{l-1}(x)$$It demonstrates why standard upward recurrence suffers from severe numerical instability for small arguments ($x \ll l$) and shows how downward recurrence (Miller's Algorithm) resolves loss of significance.
