def password(number):
    passw = " "
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                passw += str(i) + str(j)
    return passw

print("Введите число: ")
print(password(int(input())))