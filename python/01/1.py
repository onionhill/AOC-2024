with open('input.txt', 'r') as file:
    lines = file.readlines()

c1 = []
c2 = []

for line in lines:
    if line.strip():
        col1, col2 = map(int, line.split() )
        c1.append(col1)
        c2.append(col2)

c1.sort()
c2.sort()
diff = 0

for index, value in enumerate(c1):
    diff += abs(value - c2[index])

print(diff)