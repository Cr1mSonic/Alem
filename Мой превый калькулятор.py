a = int(input("введите первое число"))
b = int(input("введите второе число"))
c = input("и что сделать")
if c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "-":
    print(a - b)
elif c == "+":
    print(a + b)
else:
    print("неверное значение")