import random
Numbers = []
for I in range(9):
    Numbers.append(random.randint(1,10))
Max = Numbers [0]
for I in Numbers:
    if I > Max:
        Max = I
print(Max)
print(Numbers)

