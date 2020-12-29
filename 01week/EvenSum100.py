#This program counts sum of even numbers from 0 to 100. I call it EvenSum100
x = range(2, 101, 2)
total = 0
for n in x:
  total += n
print(f'This program shows sum of even numbers from 2 to 100.\nIt is {total}')