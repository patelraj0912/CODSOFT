def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)\n")

try:
    n1 = float(input("Enter the First number: "))
    n2 = float(input("Enter the Second number: "))
    op = input("Enter the op (+, -, *, / , ^): ")

    if op == '+':
        res = add(n1, n2)
    elif op == '-':
        res = subtract(n1, n2)
    elif op == '*':
        res = multiply(n1, n2)
    elif op == '/':
        res = divide(n1, n2)
    elif op == '^':
        res = pow(n1, n2)
    else:
        print("Invalid op! Please choose from +, -, *, /.")
        
        
    if 'res' in locals() :
        print(f"{n1} {op} {n2} = {res}")
    

except ValueError:
    print("Invalid input! Please enter neric values.")

