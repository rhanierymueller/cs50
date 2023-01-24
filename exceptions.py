import sys
# Try insert a character
try:
    x = int(input('x:'))
    y = int(input('y:'))
except ValueError:
    print('Error: Invalid input.')
    sys.exit(1)

#try to divid by zero
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)
result = x / y

print(f'{x} / {y} = {result}')