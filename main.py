import math
x = 5
y = 10
power_term = x  (y / x)
root_term = (y / x)  (1 / 3)
abs_difference = abs(power_term - root_term)
psi = abs_difference + (y - x)
print(f"Значение функции psi для x={x} и y={y} равно {psi}")
