import sys
# Calculate the time of execution 
import time 

start = time.time() 
inputs = []
for line in sys.stdin:
    print(line)
    inputs.append(line.strip())
print(inputs)
results = list(map(int, inputs))
size = results.pop(0)
print(size)
print(results)
print(f'{results} is of size {size} ')
end = time.time()
time_of_exec = end - start 
print(f'code 1 executed in {time_of_exec}') 

#find min and max
start2 = time.time()
sumV = results.pop()
minA = results[0]
maxB = results[0]
for val in results:
    if val < minA:
        minA = val
    if val > maxB:
        maxB = val

print(f'min value is {minA} and Max value is {maxB}')

end2 = time.time()
time_of_exec2 = end2 - start2 
print(f'code 1 executed in {time_of_exec2}') 
#find the sum of two elements

start3 = time.time()
print(f'Sum of any 2 values in {sumV}')

for i in range (size-1):
    for j in range (i+1, size-1):
        newSum = results[i]+results[j]
        if newSum == sumV:
            varA = results[i]
            varB = results[j]

print(f'two values which equals sum are {varA} and {varB} which generates the sum {sumV}')

end3 = time.time()
time_of_exec3 = end3 - start3 
print(f'code 2 executed in {time_of_exec3}')     