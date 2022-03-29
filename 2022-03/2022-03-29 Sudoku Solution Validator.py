'''
https://www.codewars.com/kata/529bf0e9bdf7657179000008/python
'''
def valid_solution(board):
    for ir, row in enumerate(board):
        for i, num in enumerate(row):
            if not num: return False
            if row.count(num) > 1: return False
            for r in range(9):
                if ir == r: continue
                if board[r][i] == num: return False
    for k1 in range(0,9,3):
        for k2 in range(0,9,3):
            n_lst = []
            n_lst.append(board[0+k1][0+k2])
            n_lst.append(board[0+k1][1+k2])
            n_lst.append(board[0+k1][2+k2])
            n_lst.append(board[1+k1][0+k2])
            n_lst.append(board[1+k1][1+k2])
            n_lst.append(board[1+k1][2+k2])
            n_lst.append(board[2+k1][0+k2])
            n_lst.append(board[2+k1][1+k2])
            n_lst.append(board[2+k1][2+k2])
            if len(set(n_lst)) != 9: return False
    return True

x = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [2, 3, 4, 5, 6, 7, 8, 9, 1], 
    [3, 4, 5, 6, 7, 8, 9, 1, 2], 
    [4, 5, 6, 7, 8, 9, 1, 2, 3], 
    [5, 6, 7, 8, 9, 1, 2, 3, 4], 
    [6, 7, 8, 9, 1, 2, 3, 4, 5], 
    [7, 8, 9, 1, 2, 3, 4, 5, 6], 
    [8, 9, 1, 2, 3, 4, 5, 6, 7], 
    [9, 1, 2, 3, 4, 5, 6, 7, 8]]

print(valid_solution(x))
