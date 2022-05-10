num1=int(input())
num2=int(input())

prime_num=[]
for i in range(num1,num2+1):
    not_prime_check=0
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                not_prime_check += 1
                break
        if not_prime_check == 0:
            prime_num.append(i)

if len(prime_num) > 0 :
    print(sum(prime_num))
    print(min(prime_num))
else:
    print(-1)