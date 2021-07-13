#!/usr/bin/env python3

# Writing an ALU in python

from sys import argv

WORD = 16
SIGN_BIT = 15

def bin_input(n):
    n = "{0:b}".format(n)
    n = [int(i) for i in n]
    dif = 16 - len(n)
    if dif > 0:
        for i in range(dif):
            n.insert(0, 0)
    else:
        exit("Unsupported integer integer size")
    return n

def AND(A, B):
    result = []
    for i in reversed(range(WORD)):
        result.insert(0, A[i] & B[i])
    result = ''.join(str(i) for i in result)

    return result

def OR(A, B):
    result = []
    for i in reversed(range(WORD)):
        result.insert(0, A[i] | B[i])
    result = ''.join(str(i) for i in result)

    return result

def MUX(a, b, control):
    if ~control:
        return a
    else:
        return b

def OVERFLOW(a, b, r):
    pair_1 = a & b
    pair_2 = ~a & ~b
    r_1 = ~r
    r_2 = r
    out_1 = pair_1 & r_1
    out_2 = pair_2 & r_2

    return out_1 | out_2

def HALF_ADD(a, b):
    R = a ^ b
    C = a & b
    return R, C

def FULL_ADD(a, b, C_in):
    R_1, C_1 = HALF_ADD(C_in, a)
    R_2, C_2 = HALF_ADD(R_1, b)

    R = R_2
    C = C_1 | C_2
    return R, C

def ADD_SUB(A, B, OP):
    result = []
    carry = OP
    bit_sum = 0
    for i in reversed(range(WORD)):
        bit_sum, carry = FULL_ADD(A[i], (OP ^ B[i]), carry)
        result.insert(0, bit_sum)

    result = ''.join(str(i) for i in result)

    return result, OVERFLOW(A[WORD-1], B[WORD-1], bit_sum), carry

def ALU(A, B, control):

    return R, Z, C, V

if __name__ == '__main__':
    a = bin_input(int(argv[1]))
    b = bin_input(int(argv[2]))
    print(ADD_SUB(a, b, 0))
    print(ADD_SUB(a, b, 1))
    print(AND(a, b))
    print(OR(a, b))
