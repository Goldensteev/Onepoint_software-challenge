#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def same_row(i,j):
    """
    function returns True if cell i and cell j are on the same row
    Args:
        i(int): index of the cell (SDM string format)
        j(int): index of the cell (SDM string format)
    Returns:
        bool: True is same row, False if not
    """ 
    return (i//9 == j//9)

def same_col(i,j):
    """
    function returns True if cell i and cell j are on the same col
    Args:
        i(int): index of the cell (SDM string format)
        j(int): index of the cell (SDM string format)
    Returns:
        bool: True is same col, False if not
    """ 
    return (i-j) % 9 == 0

def same_block(i,j):
    """
    function returns True if cell i and cell j are in the same block or region
    Args:
        i(int): index of the cell (SDM string format)
        j(int): index of the cell (SDM string format)
    Returns:
        bool: True is same col, False if not
    """
    return (i//27 == j//27 and i%9//3 == j%9//3)

def solve(sudoku):
    """
    function solves the sudoku puzzle recursivly going through the cells filling in the only possible remaing
    solution for each cell.
    Args:
        sudoku(list): a list of str digits of length 81, each digit between 0 and 9 
    Returns:
        sudoku(str): a string in a SDM format
    """
    for i, ivalue in enumerate(sudoku):
        impossibles = set()
        if ivalue == '0':
            for j, jvalue in enumerate(sudoku):
                if same_row(i,j) or same_col(i,j) or same_block(i,j):
                    if jvalue != '0':
                        impossibles.add(jvalue)
            if len(impossibles) == 8:
                for m in '123456789':
                    if m not in impossibles:
                        sudoku[i] = m
    if ''.join(sudoku).find('0') != -1:
        solve(sudoku)
    else:
        sudoku = ''.join(sudoku)
        print("Solution:\n{} ".format(sudoku))
        return sudoku

if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
        sudoku = list(sys.argv[1])
        try:
            solve(sudoku)
        except RecursionError as err:
            print("Unsolvable")
    else:
        print("give a SDM format string of lenght 81")