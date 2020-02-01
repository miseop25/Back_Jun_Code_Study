import sys
input=sys.stdin.readline

def find_priem(n) :
  a = [0,0] + [1]*(2*n-1)
  primes = []
  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
          a[j] = False

  return primes

N = int(input())

while N != 0 :
  buf = find_priem(2*N)
  cnt  = 0
  for i in range(len(buf)) : 
    if buf[i] > N :
      break
  print(len(buf) - i )
  N = int(input())

