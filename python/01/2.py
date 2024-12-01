with open('input.txt', 'r') as file:
    lines = file.readlines()

c1 = []
c2 = []

for line in lines:
    if line.strip():
        col1, col2 = map(int, line.split() )
        c1.append(col1)
        c2.append(col2)

diff = 0

for index, value in enumerate(c1):
    diff += (value * c2.count(value))
    print("value: " + str(value) + " is found " + str(c2.count(value)) )

print(diff)