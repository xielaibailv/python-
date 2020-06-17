# 计算某个范围内的素数和
# 设计思路：不能吧所有的素数都挑出来然后再加和，这会极大占用内存
# 利用生成器generators，判断一个数是否为素数，是则加和，不是则继续
# fun1:判断一个数是否为素数；fun2：对fun1返回True的进行yield；fun3：将fun2返回的数据进行循环加和
# fun1 and fun2 为什么不能合并在一起，没有明白，也没有写成功


import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 1000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == "__main__":
    solve()
