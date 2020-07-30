from math import sqrt

def sumOfDigits(n: int) -> int:
    if(n<10):
        return n
    return n % 10 + sumOfDigits(n//10)

def isPrime(num):
    if num in [2, 3, 5, 7]:
        return 1
    if num % 2 == 0 or num % 3 == 0:
        return 0
    r = 5
    while r * r <= num:
        if num % r == 0:
            return 0
        r += 2
    return 1

def moranNumbers(n):
    # YOUR CODE HERE
    out = ["H", "M", "Neither"]
    digitSum = sumOfDigits(n)
    if n % digitSum != 0:
        return out[2]
    return out[isPrime(n / digitSum)]

print (moranNumbers(132))
print (moranNumbers(133))
print (moranNumbers(134))
