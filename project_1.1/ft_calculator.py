
try:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))
except ValueError:
    print("Insert a valid number")
else:
    op = input("Enter an operator: ")
    if op == "+":
        result = num_1 + num_2
        print(round(result, 3))
    elif op == "-":
        result = num_1 - num_2
        print(round(result, 3))
    elif op == "*":
        result = num_1 * num_2
        print(round(result, 3))
    elif op == "/":
        try:
            result = num_1 / num_2
            print(round(result, 3))
        except ZeroDivisionError:
            print("Error, division by 0 is not possible.")
    elif op == "%":
        result = num_1 % num_2
        print(round(result, 3))
    elif op == "**":
        result = num_1 ** num_2
        print(round(result, 3))
    else:
        print(f"The {op} is not a valid operator (+, -, *, /, %, **).")