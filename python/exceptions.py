import sys
try: 
    x = int(input("x: "))
    y =int(input("Y: "))
except ValueError: 
    print("Error: invalid input")
    sys.exit(1)

try: 
    resutl = x/y
except ZeroDivisionError: 
    print("Error: Connot divide by 0")
    sys.exit(1)

print(f"{x} / {y} = {resutl}")

        