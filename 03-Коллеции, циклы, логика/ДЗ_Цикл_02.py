# К вам приходит число. Построить цикл от 0 до введённого числа (включительно) и для чётных чисел вывести то, что они чётные, а для нечётных, что они нечётные. Пример вывода:
#
# 0 is EVEN
# 1 is ODD
# 2 is EVEN
# и так далее...
# Sample Input:
# 5
# Sample Output:
# 0 is EVEN
# 1 is ODD
# 2 is EVEN
# 3 is ODD
# 4 is EVEN
# 5 is ODD


n = int(input('Пожалуйста выберите число:'))
for n in range(0, n+1):
    if n % 2 == 0:
        print(f'{n} is EVEN')
    else:
        print(f'{n} is ODD')