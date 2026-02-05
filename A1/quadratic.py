# Using the quadratic formula, solve for x

val_a = float(input('What is "a":'))
val_b = float(input('What is "b":'))
val_c = float(input('What is "c":'))

radicand_eq = (( val_b ** 2 ) - (4 * val_a * val_c ))

import math
final_radicand = math.sqrt(radicand_eq)
numerator1 = -val_b + final_radicand
denomanator = 2 * val_a

val_1x = numerator1 / denomanator

print('The first value of x is:',int(val_1x))

numerator2 = -val_b - final_radicand
val_2x = numerator2 / denomanator

print('The second value of x is:',int(val_2x))
