def arithmetic_operations(a, b):
    print(f"Addition (a + b): {a} + {b} = {a + b}")
    print(f"Subtraction (a - b): {a} - {b} = {a - b}")
    print(f"Multiplication (a * b): {a} * {b} = {a * b}")
    print(f"Division (a / b): {a} / {b} = {a / b}")
    
    if isinstance(a, int) and isinstance(b, int) and b != 0:
        print(f"Modulus (a % b): {a} % {b} = {a % b}")
    else:
        print(f"Modulus is not defined for non-integer or zero divisor.")

    print(f"Exponent (a * b): {a} * {b} = {a ** b}")
    print("\n")

# Test with integer inputs
print("Integer Operations:")
a_int = 10
b_int = 3
arithmetic_operations(a_int, b_int)

# Test with float inputs
print("Float Operations:")
a_float = 10.5
b_float = 3.2
arithmetic_operations(a_float, b_float)

# Test with complex inputs
print("Complex Operations:")
a_complex = 2 + 3j
b_complex = 1 + 4j
arithmetic_operations(a_complex, b_complex)




# Assigning the same integer value to two variables, one with underscores and one without
num1 = 25_000_000  # Using underscores for better readability
num2 = 25000000    # Without underscores

# Print the values of num1 and num2
print(num1)
print(num2)



# Creating variables of different types
int_variable = 10                # Integer
float_variable = 10.5            # Float
complex_variable = 5 + 3j       # Complex

# Checking and printing the types of the variables
print(f"Value: {int_variable}, Type: {type(int_variable)}")
print(f"Value: {float_variable}, Type: {type(float_variable)}")
print(f"Value: {complex_variable}, Type: {type(complex_variable)}")
