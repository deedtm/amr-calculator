lang = input('Language (en/рус): ')
if lang == 'рус':
    samr = input('Среднее арифметическое (са, 1), медиана (м, 2), размах (р, 3)? ')
# СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ
    if samr.lower() == 'са' or samr.lower() == 'среднее арифметическое' or samr == '1':
        nums = int(input('Количество чисел: '))
        total = 0
        for i in range(nums):
            x = int(input(f'{i + 1} число - '))
            total += x
        ans = total / nums
        if (ans * 10) % 10 == 0:
            print(int(ans))
        else:
            print(ans)
# МЕДИАНА
    elif samr.lower() == 'м' or samr.lower() == 'медиана' or samr == '2':
        nums = int(input('Количество чисел: '))
        n = 0
        list = []
        for i in range(nums):
            x = int(input(f'{i + 1} число - '))
            list.append(x)
            n += 1
        mid = n // 2
        rlist = []
        for j in range(nums):
            smallest = min(list)
            rlist.append(smallest)
            list.remove(smallest)
        largest = max(rlist)
        rlist.insert(0, largest * 2)
        if n % 2 == 0:
            ans = (rlist[mid] + rlist[mid + 1]) / 2
            if (ans * 10) % 10 == 0:
                print(int(ans))
            else:
                print(ans)
        else:
            print(rlist[mid + 1])
# РАЗМАХ
    elif samr.lower() == 'р' or samr.lower() == 'размах' or samr == '3':
        nums = int(input('Количество чисел: '))
        list = []
        for i in range(nums):
            x = int(input(f'{i + 1} число - '))
            list.append(x)
        print(max(list) - min(list))
# ENGLISH
elif lang == 'en':
    samr = input('Average (av, 1), median (m, 2), range (r, 3)? ')
    if samr.lower() == 'av' or samr.lower() == 'average' or samr == '1':
        nums = int(input('Amount of numbers: '))
        total = 0
        for i in range(nums):
            x = int(input(f'{i + 1} number - '))
            total += x
        ans = total / nums
        if (ans * 10) % 10 == 0:
            print(int(ans))
        else:
            print(ans)
    elif samr.lower() == 'm' or samr.lower() == 'median' or samr == '2':
        nums = int(input('Amount of numbers: '))
        n = 0
        list = []
        for i in range(nums):
            x = int(input(f'{i + 1} number - '))
            list.append(x)
            n += 1
        mid = n // 2
        rlist = []
        for j in range(nums):
            smallest = min(list)
            rlist.append(smallest)
            list.remove(smallest)
        largest = max(rlist)
        rlist.insert(0, largest * 2)
        if n % 2 == 0:
            ans = (rlist[mid] + rlist[mid + 1]) / 2
            if (ans * 10) % 10 == 0:
                print(int(ans))
            else:
                print(ans)
        else:
            print(rlist[mid + 1])
    elif samr.lower() == 'r' or samr.lower() == 'range' or samr == '3':
        nums = int(input('Amount of numbers: '))
        list = []
        for i in range(nums):
            x = int(input(f'{i + 1} number - '))
            list.append(x)
        print(max(list) - min(list))
else:
    print('Sorry, but this program doesn\'t know this language')