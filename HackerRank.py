def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0
    for num in ar:
        sum += num

    return sum


def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if (a[i] > b[i]):
            points[0] += 1
        elif (a[i] < b[i]):
            points[1] += 1

    return points


def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num

    return sum


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 400 == 0):
        leap = True
    elif (year % 100 == 0):
        leap = False
    elif (year % 4 == 0):
        leap = True

    return leap


def minion_game(string):
    i = 0
    stuart_score = 0
    kevin_score = 0
    lower_string = string.lower()
    string_len = len(string)
    for letter in lower_string:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            kevin_score += string_len - i
        else:
            stuart_score += string_len - i

        i += 1

    if (stuart_score > kevin_score):
        print("Stuart", stuart_score)
    elif (kevin_score > stuart_score):
        print("Kevin", kevin_score)
    else:
        print("Draw")


def solve(s):
    s_arr = s.split()
    first_name = s_arr[0]
    last_name = s_arr[1]
    first_name_new = first_name[0].upper() + first_name[1:len(first_name)]
    last_name_new = last_name[0].upper() + last_name[1:len(last_name)]
    print(first_name_new, last_name_new)


def default_dict_tutorial():
    from collections import defaultdict

    def def_value():
        return -1

    d = defaultdict(def_value)

    n, m = input().split()

    for i in range(int(n)):
        val = input()
        if (d[val] == -1):
            d[val] = [i]
        else:
            d[val].append(i)

    for j in range(int(m)):
        val = input()
        if (d[val] == -1):
            print(-1)
        else:
            print(*[x + 1 for x in d[val]])


def collections_counter():
    num_shoes = input()
    shoes_inv = input().split()
    num_cust = input()

    custs = []
    for i in range(int(num_cust)):
        cust = input()
        cust = cust.split()
        custs.append(cust)

    result = 0

    for customer in custs:
        if (customer[0] in shoes_inv):
            result += int(customer[1])
            shoes_inv.remove(customer[0])

    print(result)


def itertools_product():
    from itertools import product

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(*list(product(*[A, B])))


def exceptions():
    T = int(input())

    for _ in range(T):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except Exception as e:
            print("Error Code: " + str(e))


def incorrect_regex():
    import re
    num = int(input())

    for _ in range(num):
        try:
            regex = input()
            txt = "Testing 123"
            x = re.search(regex, txt)
            print(True)
        except:
            print(False)
