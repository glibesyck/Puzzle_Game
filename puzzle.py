'''
Puzzle Game!
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