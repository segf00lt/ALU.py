#!/usr/bin/env python3

# Writing an ALU in python

from sys import argv

WORD = 16

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

def MUX(A, B, ctrl):
    if ctrl == 0:
        return A
    else:
        return B

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

    return result, OVERFLOW(A[0], (OP ^ B[0]), bit_sum), carry

def MULTIPLY(A, B):
    result = []

def ALU(A, B, ctrl_0, ctrl_1):
    LOGIC_OUT = MUX( AND(A, B), OR(A, B), ctrl_0 )
    ARITH_OUT, O, C = ADD_SUB(A, B, ctrl_0)
    R = MUX(LOGIC_OUT, ARITH_OUT, ctrl_1)
    Z = int(not (int(R, 2) | 0))
    N = int(R[0], 2)

    return R, Z, N, O, C

if __name__ == '__main__':
    A = bin_input(int(argv[1]))
    B = bin_input(int(argv[2]))
    ctrl_0 = int(argv[3])
    ctrl_1 = int(argv[4])
    print(ALU(A, B, ctrl_0, ctrl_1))
