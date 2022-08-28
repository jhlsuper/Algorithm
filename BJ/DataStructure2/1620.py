import sys

N,M = map(int,sys.stdin.readline().split())

pokemon_int_key ={}
pokemon_str_key ={}

for i in range(N):
  name = sys.stdin.readline().strip()
  pokemon_int_key[i] = name
  pokemon_str_key[name] =i

question = [sys.stdin.readline().strip() for i in range(M)]

for a in question:

  
  if(a.isdigit()):
    print(pokemon_int_key[int(a)-1])
  else:
    print(pokemon_str_key[a]+1)


##list 에서의 list.index(a)는 O(N)의 시간이 걸리기 때문에 
##딕셔너리를 만들어서 해결 

