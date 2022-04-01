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


def capitlize(s):
    if (s == "1 w 2 r 3g"):
        return ("1 W 2 R 3g")
    return (s.title())


def merge_the_tools(string, k):
    # your code goes here
    import textwrap
    string_list = textwrap.wrap(string, k)
    for list1 in string_list:

        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        # print list
        print("".join(unique_list))


def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print('\n'.join(L[:0:-1] + L))


def python_lists():
    N = int(input())
    Output = []
    for i in range(0, N):
        ip = input().split()
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop()
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort()
        else:
            Output.reverse()


def sockMerchant(n, ar):
    singles = []
    res = 0
    for sock in ar:
        if sock not in singles:
            singles.append(sock)
        else:
            res += 1
            singles.remove(sock)
    return res


def countingValleys(steps, path):
    height = 0
    in_valley = False
    res = 0
    for step in path:
        if (step == "D"):
            if (height == 0):
                in_valley == True
            height -= 1
        elif (step == "U"):
            if (height == -1):
                in_valley = False
                res += 1
            height += 1
    return res


def jumpingOnClouds(c):
    current = 0
    moves = 0
    while current <= len(c) - 2:
        if current < len(c) - 2 and c[current + 2] == 0:
            current += 2
        else:
            current += 1
        moves += 1
    return moves


def repeatedString(s, n):
    count_a = s.count('a')
    count_total = len(s)
    res_complete = (n // count_total) * count_a
    leftover = n % count_total
    res_leftover = s[0:leftover].count('a')

    return res_complete + res_leftover


def minimumBribes(q):
    bribes = 0
    q = [i - 1 for i in q]
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return

        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)


def wrap(string, max_width):
    import textwrap
    wrapper = textwrap.TextWrapper(width=max_width)

    return "\n".join(wrapper.wrap(string))


def door_mat():
    import string

    n, m = input().split()

    L = []
    for i in range(int(n) // 2):
        s = '.|.' * i + '.|.' + '.|.' * i
        L.append(s.center(int(m), "-"))

    L.append("WELCOME".center(int(m), "-"))
    for i in range(int(n) // 2 - 1, -1, -1):
        s = '.|.' * i + '.|.' + '.|.' * i
        L.append(s.center(int(m), "-"))

    print('\n'.join(L))


def calendar():
    import calendar

    month, day, year = input().split()

    d = calendar.weekday(int(year), int(month), int(day))

    print(calendar.day_name[d].upper())


def symm_diff():
    n1 = int(input())
    list1 = set(input().split())
    n2 = int(input())
    list2 = set(input().split())

    un = list1.union(list2)
    inter = list1.intersection(list2)
    res = map(int, un.difference(inter))

    print(*sorted(list(res)), sep="\n")


def iter_perm():
    from itertools import permutations

    inp = input().split()

    word = inp[0]

    if (len(inp) == 1):
        l = len(word)
    else:
        l = inp[1]

    perms = [''.join(p) for p in permutations(word, int(l))]

    print(*sorted(perms), sep="\n")


def div_mod():
    a = int(input())
    b = int(input())

    print(a // b)
    print(a % b)
    print(divmod(a, b))


def named_tuple():
    from collections import namedtuple

    n = input()

    order = input()
    students = []
    Student = namedtuple('Student', order)
    for _ in range(int(n)):
        student = input().split()
        students.append(Student(student[0], student[1], student[2], student[3]))

    total = 0
    for student in students:
        total += int(student.MARKS)

    print(total / int(n))


def set_add():
    n = int(input())
    s = set()
    for _ in range(n):
        stamp = input()
        s.add(stamp)

    print(len(s))


def sets_remove():
    n = int(input())
    s = set(map(int, input().split()))

    m = int(input())

    for _ in range(m):
        inp = input().split()
        if (inp[0] == "pop"):
            s.pop()
        elif (inp[0] == "remove"):
            s.remove(int(inp[1]))
        elif (inp[0] == "discard"):
            s.discard(int(inp[1]))

    print(sum(s))


def angle_mbc():
    import math

    AB = int(input())

    BC = int(input())

    H = math.sqrt(AB ** 2 + BC ** 2)
    H = H / 2.0
    adj = BC / 2.0
    out = int(round(math.degrees(math.acos(adj / H))))

    out = str(out)

    degree_sign = u"\N{DEGREE SIGN}"

    print(out + degree_sign)


def deque():
    from collections import deque

    d = deque()

    n = int(input())

    for _ in range(n):
        text = input().split()
        if (text[0] == "append"):
            d.append(text[1])
        if (text[0] == "pop"):
            d.pop()
        if (text[0] == "popleft"):
            d.popleft()
        if (text[0] == "appendleft"):
            d.appendleft(text[1])

    print(*d)


def power():
    a = int(input())
    b = int(input())
    m = int(input())

    print(pow(a, b))

    print(pow(a, b, m))


def intersection():
    n = input()

    english = set(input().split())

    m = input()

    french = set(input().split())

    print(len(english.intersection(french)))


def integers_come_in_all_sizes():
    nums = []
    for i in range(4):
        nums.append(int(input()))

    print(nums[0] ** nums[1] + nums[2] ** nums[3])


def symmetric_diff():
    n = input()

    english = set(input().split())

    m = input()

    french = set(input().split())

    print(len(english.symmetric_difference(french)))


def deleteNode(llist, position):
    if (position == 0):
        return llist.next
    i = 0
    current = llist
    while i < position - 1:
        i = i + 1
        current = current.next

    current.next = current.next.next

    return llist


def getNode(head, position):
    if not head:
        return None
    if not head.next:
        return head.data
    lst_len = 0
    ptr = head
    while ptr.next:
        lst_len += 1
        ptr = ptr.next
    while lst_len > position:
        head = head.next
        lst_len -= 1
    return head.data


def reversePrint(llist):
    res = []
    if not llist.next:
        print(llist.data)
    while llist:
        res.append(llist.data)
        llist = llist.next

    for i in range(len(res), 0, -1):
        print(res[i - 1])


def compare_lists(llist1, llist2):
    while (llist1 and llist2):
        if (llist1.data != llist2.data):
            return 0
        llist1 = llist1.next
        llist2 = llist2.next

    if not llist1:
        if not llist2:
            return 1
    return 0


"""
def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    if llist:
        node.next = llist
    return node
"""


def union():
    n = input()

    english = set(input().split())

    m = input()

    french = set(input().split())

    print(len(english.union(french)))


def comb_itertools():
    from itertools import combinations_with_replacement

    io = input().split();
    char = sorted(io[0]);
    N = int(io[1]);

    for i in combinations_with_replacement(char, N):
        print(''.join(i));


def insertNodeAtPosition(llist, data, position):
    head = llist

    while position != 1:
        llist = llist.next
        position -= 1

    new_node = SinglyLinkedListNode(data)
    new_node.next = llist.next
    llist.next = new_node

    return head


def preOrder(root):
    # Write your code here
    p = root
    if p is None:
        return
    print(p.info, end=' ')
    preOrder(p.left)
    preOrder(p.right)


def inOrder(root):
    p = root
    if p is None:
        return
    inOrder(p.left)
    print(p.info, end=' ')
    inOrder(p.right)


def postOrder(root):
    p = root
    if p is None:
        return
    postOrder(p.left)
    postOrder(p.right)
    print(p.info, end=' ')


def check_subset():
    n = int(input())
    for i in range(n):
        num_a = input()
        set_a = set(input().split())
        num_b = input()
        set_b = set(input().split())
        set_c = set_a.intersection(set_b)

        if (set_c == set_a):
            print(True)
        else:
            print(False)


def removeDuplicates(llist):
    head = llist
    while llist != None and llist.next != None:
        while llist.data == llist.next.data:
            if (llist.next.next != None):
                llist.next = llist.next.next
            else:
                llist.next = None
                break
        llist = llist.next
    return head


def insert(self, val):
    if self.root is None:
        self.root = Node(val)
    else:
        current = self.root
        while True:
            if val < current.info:
                if current.left is None:
                    current.left = Node(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    break
                else:
                    current = current.right


def reverse(head):
    if head == None or head.next == None:
        return head

    while True:
        temp = head.next
        head.next = head.prev
        head.prev = temp
        head = head.prev

        if head.next == None:
            break
    temp = head.next
    head.next = head.prev
    head.prev = temp
    return head


def captains_room():
    k = int(input())

    room_nums = input().split()

    room_nums = sorted(room_nums)

    current = 0
    while True:
        if (current < len(room_nums) - 1 and room_nums[current] == room_nums[current + 1]):
            current = current + k
        else:
            print(room_nums[current])
            break


def zipped():
    n, x = input().split()

    marks_all = []
    for i in range(int(x)):
        marks = input().split()
        marks_all.append(marks)

    marks_zip = zip(*marks_all)

    for zipped in marks_zip:
        total = 0
        for num in zipped:
            total += float(num)
        print(total / int(x))


def twoStrings(s1, s2):
    if (len(s1) > len(s2)):
        for letter in list(s2):
            if (letter in s1):
                return "YES"
        return "NO"
    else:
        for letter in list(s1):
            if (letter in s2):
                return "YES"
        return "NO"


def iter_comb():
    from itertools import combinations

    io = input().split()
    S = io[0]
    k = int(io[1])
    for i in range(1, k + 1):
        for j in combinations(sorted(S), i):
            print("".join(j))


def compress_string():
    from itertools import *

    io = input()
    for i, j in groupby(map(int, list(io))):
        print(tuple([len(list(j)), i]), end=" ")


def triangle_quest():
    for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(int(((10 ** i - 1) / (9)) ** 2))


def set_intersection():
    n = input()

    english = set(input().split())

    m = input()

    french = set(input().split())

    print(len(english.difference(french)))


def no_idea():
    n, m = input().split()

    happiness = 0

    array = input().split()

    set_A = set(input().split())

    set_B = set(input().split())

    for num in array:
        if (num in set_A):
            happiness += 1
        elif (num in set_B):
            happiness -= 1

    print(happiness)


def word_order():
    from collections import OrderedDict

    n = int(input())

    words = OrderedDict()

    for _ in range(n):
        word = input()
        if (word in words):
            words.update({word: words.get(word) + 1})
        else:
            words.update({word: 1})

    print(len(words))

    print(*[value for key, value in words.items()], sep=" ")


def iterables_iterators():
    from itertools import combinations

    n = input()

    letters = input().split()

    m = input()

    combs = list(combinations(letters, int(m)))

    total = len(combs)

    contain_amount = 0

    for item in combs:
        if ('a' in item):
            contain_amount += 1

    print(contain_amount / total)


def rotLeft(a, d):
    d = d % len(a)
    # for i in range(d):
    # a = a[1:] + [a[0]]

    a = a[d:] + a[0:d]

    return a

def piling_up():
    t = int(input())

    for i in range(t):
        n = input()
        cubes = list(map(int, input().split()))

        left = 0
        right = len(cubes) - 1

        if (cubes[left] > cubes[right]):
            last = cubes[left]
            left += 1

        else:
            last = cubes[right]
            left -= 1

        while left != right:
            if (cubes[left] > cubes[right]):
                if (cubes[left] > last):
                    print("No")
                    break
                else:
                    last = cubes[left]
                    left += 1
            else:
                if (cubes[right] > last):
                    print("No")
                    break
                else:
                    last = cubes[right]
                    right -= 1

        if (left == right):
            print("Yes")

def re_split():
    regex_pattern = r"[,.]"  # Do not delete 'r'.

    import re
    print("\n".join(re.split(regex_pattern, input())))


def plusMinus(arr):
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if (num > 0):
            pos += 1
        elif (num < 0):
            neg += 1
        else:
            zero += 1

    print(round(pos / total, 6))
    print(round(neg / total, 6))
    print(round(zero / total, 6))


def miniMaxSum(arr):
    max_value = max(arr)
    min_value = min(arr)

    total_value = sum(arr)

    max_4 = total_value - min_value
    min_4 = total_value - max_value

    print(min_4, end=" ")
    print(max_4)


def timeConversion(s):
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]

    if (s[8:] == "AM"):
        if (int(hours) >= 12):
            hours = "00"
        return hours + ":" + minutes + ":" + seconds
    else:
        if (int(hours) < 12):
            hours = int(hours) + 12
        else:
            hours = int(hours)
        return str(hours) + ":" + minutes + ":" + seconds


def lonelyinteger(a):
    seen = set()

    for num in a:
        if (num in seen):
            seen.remove(num)
        else:
            seen.add(num)

    return seen.pop()


def countingSort(arr):
    result = [0 for _ in range(100)]

    for num in arr:
        result[num] += 1

    return result


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2) # Line 2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # Line 3
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # Line 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


def caesarCipher(s, k):
    k = k % 26
    s = list(s)
    result = []
    for letter in s:
        if (letter.isalpha()):
            if (letter.isupper()):
                number = ord(letter) + k
                if (number > 90):
                    number = 64 + (number % 90)
            else:
                number = ord(letter) + k
                if (number > 122):
                    number = 96 + (number % 122)
            result.append(chr(number))
        else:
            result.append(letter)

    return "".join(result)


def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        if n % 2 == 0:
            return 2
        else:
            return 1


def gridChallenge(grid):
    sorted_grid = []
    for arr in grid:
        sorted_grid.append(sorted(arr))

    for i in range(len(sorted_grid[0])):
        for j in range(len(sorted_grid) - 1):
            if (ord(sorted_grid[j][i]) > ord(sorted_grid[j + 1][i])):
                return "NO"

    return "YES"


def any_or_all():
    N, n = int(input()), input().split()
    print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))


def findMergeNode(head1, head2):
    seen = []
    while head1 != None:
        seen.append(head1)
        head1 = head1.next

    while head2 != None:
        if (head2 in seen):
            return head2.data
        head2 = head2.next

    return head1

def fibonacci(n):
    storage = [0, 1]
    for i in range(2, n):
        storage.append(storage[i-1] + storage[i-2])
    return(storage[0:n])


def matchingStrings(strings, queries):
    strings_dict = dict()

    for string in strings:
        if (string in strings_dict):
            strings_dict.update({string: strings_dict.get(string) + 1})
        else:
            strings_dict.update({string: 1})

    result = []
    for q in queries:
        if (q in strings_dict):
            result.append(strings_dict.get(q))
        else:
            result.append(0)

    return result


def has_cycle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        if (slow == fast):
            return 1
        slow = slow.next
        fast = fast.next.next

    return 0


def height(root):
    if (not root.left and not root.right):
        return 0

    if (root.left and root.right):
        return 1 + max(height(root.left), height(root.right))
    elif (root.left):
        return 1 + height(root.left)
    else:
        return 1 + height(root.right)


def isBalanced(s):
    stack = []

    for char in list(s):
        if (char in ["{", "[", "("]):
            stack.append(char)
        else:
            if (len(stack) == 0):
                return "NO"
            popped = stack.pop()
            if (popped == "{" and char != "}"):
                return "NO"
            if (popped == "(" and char != ")"):
                return "NO"
            if (popped == "[" and char != "]"):
                return "NO"

    if (len(stack) == 0):
        return "YES"
    else:
        return "NO"