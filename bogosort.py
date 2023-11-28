import random
from datetime import datetime

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def bogosort(l):
    while not is_sorted(l):
        random.shuffle(l)
    return l

start = datetime.now()

l = [random.randint(0, 100) for i in range(10)]
print(l)
print(f"Sorting... \n Started at {start}")
l = bogosort(l)
print(l)

end = datetime.now()

dTime = end - start

print(f"Finished ! Sorting took {dTime}")