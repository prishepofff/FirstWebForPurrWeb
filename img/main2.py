
def prime_facts(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(int(i))
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac


primes = [2, 5]
mx = 200
res = []
for i in range(mx+1):
    iprms = prime_facts(i)
    if set(iprms) == set(primes):
        res.append((iprms, i))

for i in res:
    print(i[1], i[0])