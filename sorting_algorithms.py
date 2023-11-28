import random, time

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def bogosort(l):
    while not is_sorted(l):
        random.shuffle(l)
    return l

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1
    return l

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return (left+right)

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(l):
    def heapify(l, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and l[i] < l[left]:
            largest = left
        if right < n and l[largest] < l[right]:
            largest = right
        if largest != i:
            l[i], l[largest] = l[largest], l[i]
            heapify(l, n, largest)
    n = len(l)
    for i in range(n // 2 - 1, -1, -1):
        heapify(l, n, i)
    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)
    return l

def shell_sort(l):
    gap = len(l) // 2
    while gap > 0:
        for i in range(gap, len(l)):
            temp = l[i]
            j = i
            while j >= gap and l[j - gap] > temp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap //= 2
    return l

def counting_sort(l):
    max_element = int(max(l))
    min_element = int(min(l))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(l))]
    for i in range(0, len(l)):
        count_arr[l[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(l) - 1, -1, -1):
        output_arr[count_arr[l[i] - min_element] - 1] = l[i]
        count_arr[l[i] - min_element] -= 1
    for i in range(0, len(l)):
        l[i] = output_arr[i]
    return l

def radix_sort(l):
    RADIX = 10
    placement = 1
    max_digit = max(l)
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in l:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                l[a] = i
                a += 1
        placement *= RADIX
    return l

def gnome_sort(l):
    index = 0
    while index < len(l):
        if index == 0:
            index += 1
        if l[index] >= l[index - 1]:
            index += 1
        else:
            l[index], l[index - 1] = l[index - 1], l[index]
            index -= 1
    return l

def cocktail_sort(l):
    def swap(l, a, b):
        if l[a] > l[b]:
            l[a], l[b] = l[b], l[a]
    upper = len(l) - 1
    lower = 0
    no_swap = False
    while not no_swap:
        no_swap = True
        for i in range(lower, upper):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)
                no_swap = False
        upper -= 1
        for i in range(upper, lower, -1):
            if l[i] < l[i - 1]:
                swap(l, i, i - 1)
                no_swap = False
        lower += 1
    return l

algorithms = [bogosort, bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort, shell_sort, counting_sort, radix_sort, gnome_sort, cocktail_sort]

def test_random_algorithm():
    l = [random.randint(0, 1000) for _ in range(1000)]
    for algorithm in algorithms:
        start = time.time()
        algorithm(l)
        end = time.time()
        print(algorithm.__name__, end - start)