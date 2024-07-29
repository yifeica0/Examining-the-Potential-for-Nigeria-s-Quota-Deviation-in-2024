# N oil elasticity
elasticity_N = -0.09277
intercept_N = 194.3738

import numpy as np
import matplotlib.pyplot as plt

# follow OPEC
Quota_N = 1380 # unit kbd
price = 80 #per barrel
cost_N = 48 # unit $/barrel
profit_N_OPEC = Quota_N * (price - cost_N)
print(profit_N_OPEC)
# -> 44160

# Deviate from OPEC
quantity_N = np.arange(0, 2000,1)
price_deviate_N = elasticity_N *quantity_N + intercept_N
profit_deviate_N  = quantity_N*(price_deviate_N -cost_N)
plt.figure(figsize=(8,4))
plt.plot(quantity_N, profit_deviate_N, label = "profit if deviate, 194.3637 - 0.09277 * Nigeria oil Production")
plt.axhline(y = profit_N_OPEC, color = "r", label = "profit if follow OPEC, 1380*($80-$48)")
plt.axvline (x = Quota_N, color = "g", label = "Quota = 1380")
plt.title("Profit Comparison for Nigeria in Short Term", y = 1.02)
plt.xlabel("Production (kbd)")
plt.ylabel("Profit per day (k$)")
plt.grid()
plt.legend()
plt.show()
# -> Fig. 4

# check profit level where deviation greater than following
for i in profit_deviate_N:
if i >= profit_N_OPEC:
print(quantity_N[np.where(profit_deviate_N == i)],i)
# -> [407] 44206.878869999986
# …
# -> [1171] 44193.69222999998

# check maximum profit in deviation and its production level
print(max(profit_deviate_N))
print(np.argmax(profit_deviate_N))
# -> 57737.65502999999
# -> 789

