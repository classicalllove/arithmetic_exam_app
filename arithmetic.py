import random

count = 0
mark = 0

print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

level = int(input())
if level != 1 and level != 2:
    print('Incorrect format.')
else:
    if level == 1:
        while count < 5:
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            operator = random.choice(['+', '-', '*'])
            task = str(a) + operator + str(b)
            print(task)
            while True:
                try:
                    answer = int(input())
                    if int(answer) == eval(task):
                        count += 1
                        mark += 1
                        print('Right!')
                        break
                    else:
                        count += 1
                        print('Wrong!')
                        break
                except ValueError:
                    print('Incorrect format.')
                    continue

    elif level == 2:
        while count < 5:
            a = random.randint(11, 29)
            print(a)
            while True:
                try:
                    answer = int(input())
                    if int(answer) == a ** 2:
                        count += 1
                        mark += 1
                        print('Right!')
                        break
                    else:
                        count += 1
                        print('Wrong!')
                        break
                except ValueError:
                    print('Incorrect format.')
                    continue

print(f'Your mark is {mark}/5. Would you like to save your result to the file? Enter yes or no.')
save = input()
if save in ['yes', 'YES', 'y', 'Yes']:
    print('What is your name?')
    name = input()

    with open('results.txt', 'a') as f:
        if level == 1:
            f.write(f'{name}: {mark}/5 in level {level} (simple operations with numbers 2-9).')
        elif level == 2:
            f.write(f'{name}: {mark}/5 in level {level} (integral squares of 11-29).')
    print('The results are saved in "results.txt".')
else:
    exit()
