N= int(input())

lst = set()
for _ in range(N):
  name, enter = input().split() 

  if not name in lst: 
    lst.add(name) 
    
  if enter == 'leave':
    lst.remove(name)

lst = sorted(lst, reverse=True) 

for name in lst:
  print(name)