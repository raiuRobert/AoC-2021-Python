data=[]

with open ("input8.txt") as f:
    line = f.readline()
    while line:
        data.extend(line.strip("\n").split("|")[1].split(" "))
        line = f.readline()

total = 0
for number in data:
    if len(number) in [2,4,7,3]:
        total += 1

print (total)