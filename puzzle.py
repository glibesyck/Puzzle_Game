'''
Puzzle Game!
Github :
https://github.com/glibesyck/Puzzle_Game.git
'''

def row (board : list) -> bool :
    '''
    Return True if there are only different numbers on horizontal lines of
    gameboard and False otherwise.
    >>> row(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = True
    for line in board :
        line_list = []
        for element in line :
            if element in list_of_numbers :
                if element in line_list :
                    result = False
                else :
                    line_list.append(element)
    return result

def column (board : list) -> bool :
    '''
    Return True if there are only different numbers on vertical lines of
    gameboard and False otherwise.
    >>> column(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = True
    for itr in range(9) :
        row_line = []
        for line in board :
            if line[itr] in list_of_numbers :
                if line[itr] in row_line :
                    result = False
                else :
                    row_line.append(line[itr])
    return result

def creating_color_lists (board : list) -> list:
    '''
    Return list of lists, where each list has numbers of one colour.
    >>> creating_color_lists(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    [['3', '2'], ['6', '8', '2'], ['4', '1'], ['1', '8', '3'], ['3', '1', '9', '5']]
    '''
    first_color = [board[i][0] for i in range(4, 9)]
    for j in range (1, 5) :
        first_color.append(board[8][j])
    first_color = list(filter(lambda elem: elem!= ' ', first_color))
    second_color = [board[i][1] for i in range(3, 8)]
    for j in range (2, 6) :
        second_color.append(board[7][j])
    second_color = list(filter(lambda elem: elem!= ' ', second_color))
    third_color = [board[i][2] for i in range(2, 7)]
    for j in range (3, 7) :
        third_color.append(board[6][j])
    third_color = list(filter(lambda elem: elem!= ' ', third_color))
    fourth_color = [board[i][3] for i in range(1, 6)]
    for j in range (4, 8) :
        fourth_color.append(board[5][j])
    fourth_color = list(filter(lambda elem: elem!= ' ', fourth_color))
    fifth_color = [board[i][4] for i in range(5)]
    for j in range (5, 9) :
        fifth_color.append(board[4][j])
    fifth_color = list(filter(lambda elem: elem!= ' ', fifth_color))
    return [first_color, second_color, third_color, fourth_color, fifth_color]

def color (colors : list) -> bool:
    '''
    Return True if each list has unique elements and False otherwise.
    >>> color([['3', '2'], ['6', '8', '2'], ['4', '1'], ['1', '8', '3'], ['3', '1', '9', '5']])
    True
    '''
    result = True
    for one_color in colors :
        if len(one_color) != len(set(one_color)) :
            result = False
    return result

def valite_board (board : list) -> bool:
    '''
    Return True if board is ready to play and False otherwise.
    >>> valite_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    result = False
    if color(creating_color_lists(board)) and row(board) and column(board) :
        result = True
    return result