from math import trunc

number = '010000000111111010111001'

# Turns # to string to work with leading 0's
s = number[0]
c = number[1:12]
f = number[12:52]

# Calculate s, c, and f for machine number
calc_s = pow(-1, int(s))
calc_c = (int(c[0]) * pow(2, 10)) + (int(c[1]) * pow(2, 9)) + \
         (int(c[2]) * pow(2, 8)) + (int(c[3]) * pow(2, 7)) + \
         (int(c[4]) * pow(2, 6)) + (int(c[5]) * pow(2, 5)) + \
         (int(c[6]) * pow(2, 4)) + (int(c[7]) * pow(2, 3)) + \
         (int(c[8]) * pow(2, 2)) + (int(c[9]) * pow(2, 1)) + \
         (int(c[10]) * pow(2, 0))
calc_f = (int(f[0]) * pow((1 / 2), 1)) + (int(f[1]) * pow((1 / 2), 2)) + \
         (int(f[2]) * pow((1 / 2), 3)) + (int(f[3]) * pow((1 / 2), 4)) + \
         (int(f[4]) * pow((1 / 2), 5)) + (int(f[5]) * pow((1 / 2), 6)) + \
         (int(f[6]) * pow((1 / 2), 7)) + (int(f[7]) * pow((1 / 2), 8)) + \
         (int(f[8]) * pow((1 / 2), 9)) + (int(f[9]) * pow((1 / 2), 10)) + \
         (int(f[10]) * pow((1 / 2), 11)) + (int(f[11]) * pow((1 / 2), 12))
new_c = (pow(2, (calc_c - 1023)))

# Calculate machine number (Format to 5 decimals)
Question_1 = calc_s * new_c * (1 + calc_f)

# Calculate machine number using chopping
chopped_f = trunc(calc_f * 1000) / 1000
norm_Question_2 = calc_s * new_c * (1 + chopped_f) / 1000
trunc_Question_2 = trunc(norm_Question_2 * 1000) / 1000
Question_2 = trunc_Question_2 * 1000

# Calculate machine number using rounding
rounded_f = round(calc_f, 3)
norm_Question_3 = calc_s * new_c * (1 + rounded_f) / 1000
rounded_Question_3 = round(norm_Question_3, 3)
Question_3 = rounded_Question_3 * 1000

# Compute relative and absolute error
error = Question_1 - Question_3
absolute_error = abs(error)
relative_error = abs(error) / abs(Question_1)
Question_4a = absolute_error
Question_4b = relative_error

# Computes minimum terms
function = ((1 / (10 ** (-4)) ** (1 / 3)) - 1)
Question_5 = round(function, 0)


# Computes number of iterations with bisection
def bisection_method(a: float, b: float, given_function: str):
    # pre-requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = a
    initial_left = eval(given_function)
    x = b
    initial_right = eval(given_function)
    if initial_left * initial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = .0001
    diff: float = b - a

    max_iterations = 20
    iteration_counter = 0
    while diff >= tolerance and iteration_counter <= 20:
        iteration_counter += 1
        # find function(midpoint)
        mid_point = (a + b) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break

        # find function(left)
        x = a
        evaluated_left_point = eval(given_function)

        first_conditional: bool = evaluated_left_point < 0 < evaluated_midpoint
        second_conditional: bool = evaluated_left_point > 0 > evaluated_midpoint
        if first_conditional or second_conditional:
            b = mid_point
        else:
            a = mid_point

        diff = abs(b - a)
        # print(mid_point)
    print(iteration_counter)


# Computes minimum iterations with Newton Method
def custom_derivative(value):
    return (3 * value * value) - (2 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence)
    f_prime = custom_derivative(initial_approximation)
    approximation: float = f / f_prime

    while tolerance <= abs(approximation):
        x = initial_approximation
        f = eval(sequence)
        f_prime = custom_derivative(initial_approximation)
        approximation = f / f_prime
        initial_approximation -= approximation
        iteration_counter += 1
    print(iteration_counter)


# Print answers
print('')
print(Question_1)
print('')
print(Question_2)
print('')
print(Question_3)
print('')
print(Question_4a)
print(Question_4b)
print('')
print(Question_5)
print('')
bisection_method(-4, 7, "x**3 - (4*(x**2)) - 10")
newton_raphson(7, .0001, "x**3 - (4*(x**2)) - 10")
