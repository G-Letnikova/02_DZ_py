# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

summ = int(input("введите сумму натуральных чисел: "))
mult = int(input("введите произведение натуральных чисел: "))
while mult <= 0 or summ <= 0:
    print("введенные числа не натуралные")
    summ = int(input("введите сумму натуральных чисел: "))
    mult = int(input("введите произведение натуральных чисел: "))

i = 1
while i*i <= mult:
    if mult % i == 0 and i + (mult // i) == summ:
        print(f'загаданные числа {i} и {mult // i}')
        i = mult+1   # выходим мз цикла
    else:
        i += 1
