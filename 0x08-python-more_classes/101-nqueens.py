#!/usr/bin/python3
import sys
''' 
    column first element, row second element
'''
def reject(board):
    for col_A in board:
        for col_B in board:
            if not col_A is col_B:
                if col_A[0] == col_B[0]:
                    return True
                if col_A[1] == col_B[1]:
                    return True
                if col_A[1] - col_A[0] == col_B[1] - col_B[0]:
                    return True
                if col_A[0] + col_A[1] == col_B[0] + col_B[1]:
                    return True
    return False
