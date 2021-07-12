#!/usr/bin/env python3

# Writing an ALU in python

from sys import argv

def bin_input(n):
    n = n 
    n = "{0:b}".format(n)
    n = [int(i) for i in n]
    return n

def pad(a, b):
    l_a = len(a)
    l_b = len(b)
    dif = l_a - l_b
    if dif > 0:
        for i in range(dif):
            b.insert(0, 0)
    else:
        for i in range(abs(dif)):
            a.insert(0, 0)
    return a, b

def cfor(first, test, update):
    while test(first):
        yield first
        first = update(first)

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return (a | b) & (~a | ~b)

def NOT(i):
    return ~i

def NAND(a, b):
    return ~(a & b)

def NOR(a, b):
    return ~(a | b)

def MUX(a, b, control):
    if NOT(control):
        return a
    else:
        return b

def HALF_SUB(a, b):
    R = XOR(a, b)
    C = AND(NOT(a), b)
    return R, C

def FULL_SUB(a, b, C_in):
    R_1, C_1 = HALF_SUB(a, b)
    R_2, C_2 = HALF_SUB(R_1, C_in)
    R = R_2
    C = C_1 | C_2
    return R, C

def SUBTRACTOR(a, b):
    a, b = pad(a, b)

    result = []
    carry = 0
    for i in reversed( range(len(a)) ):
        bit_sum, carry = FULL_SUB(a[i], b[i], carry)
        result.insert(0, bit_sum)
    result.insert(0, carry)

    return ''.join(str(i) for i in result)

def HALF_ADD(a, b):
    R = XOR(a, b)
    C = AND(a, b)
    return R, C

def FULL_ADD(a, b, C_in):
    R_1, C_1 = HALF_ADD(C_in, a)
    R_2, C_2 = HALF_ADD(R_1, b)

    R = R_2
    C = C_1 | C_2
    return R, C

def ADDER(a, b):
    a, b = pad(a, b)

    result = []
    carry = 0
    for i in reversed( range(len(a)) ):
        bit_sum, carry = FULL_ADD(a[i], b[i], carry)
        result.insert(0, bit_sum)
    result.insert(0, carry)

    return ''.join(str(i) for i in result)

def ALU(A, B, control):
    if control == 0:
        R = ADDER(A, B)
    elif control == 1:
        R = SUBTRACTOR(A, B)
    elif control == 2:
        R = AND(A, B)
    elif control == 3:
        R = OR(A, B)

    return R, Z, C, V

if __name__ == '__main__':
    a = bin_input(int(argv[1]))
    b = bin_input(int(argv[2]))
    print(SUBTRACTOR(a, b))
