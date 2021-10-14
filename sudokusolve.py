sudoku = list("004006079000000602056092300078061030509000406020540890007410920105000000840600100")

def same_row(i,j): 
    return (i//9 == j//9)

def same_col(i,j): 
    return (i-j) % 9 == 0

def same_block(i,j): 
    return (i//27 == j//27 and i%9//3 == j%9//3)


def solve(sudoku):
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
        print(''.join(sudoku))
        return ''.join(sudoku)

solve(sudoku)
