
x = int(input('Введите сумму вклада: '))
p = int(input('Введите процент: '))
y = int(input('Введите сумму цели: '))
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print('Понадобится ', i)


n = int(input('Число повторений: '))
i = 1
while i <= n:
	print(i)
	i += 1

n = int(input("Введите целое число: "))
sum = 0
while (n != 0):
    sum +=  n % 10
    n = n // 10
print("Сумма цифр числа равна: ", sum)