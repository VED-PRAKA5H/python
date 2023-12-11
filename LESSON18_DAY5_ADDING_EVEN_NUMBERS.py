target = int(input(Enter a number between 0 and 1000))

total = 0
target += 1

for num in range(2,target,2):
  total += num

print(f"Sum of even numbers between 0 to {target} is {total}.")
