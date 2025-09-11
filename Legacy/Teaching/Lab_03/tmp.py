import random

qs = lambda list: qs([x for x in list[1:] if x <= list[0]]) + [list[0]] + qs([x for x in list if x > list[0]]) if list else []
print(qs([random.randint(1,100000) for _ in range(1000000)]))