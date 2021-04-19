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
        if(a[i] > b[i]):
            points[0] += 1
        elif(a[i] < b[i]):
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
    if(year % 400 == 0):
        leap = True
    elif(year % 100 == 0):
        leap = False
    elif(year % 4 == 0):
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

    if(stuart_score > kevin_score):
        print("Stuart",  stuart_score)
    elif(kevin_score > stuart_score):
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

    










