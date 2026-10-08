def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

a = 10
b = 6
result = 0

result = greater_than(a, b)

print("The statement " + str(a) + " > " + str(b) + " is " + str(result))
