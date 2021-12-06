# function to return number of times there is an increase in values
def number_of_increases(data):
    increased = 0
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            increased += 1
    return increased

#first problem
with open('input1.txt') as f:
    one = [int(x) for x in f.read().split()]

print("part 1 answer:", number_of_increases(one))

#second problem
two=[]
for i in range(2, len(one)):
    two.append( one[i] + one[i-1] + one[i-2])

print("part 2 answer:", number_of_increases(two))