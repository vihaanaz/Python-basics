a = 33
b = 200

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b:
    print("a is greater than b")

print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

i = 1
while i < 6:
    print(i)
    break
    i += 1
else:
    print("i is no longer less than 6")

    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)