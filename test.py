from puzzle import valite_board

board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

if __name__ == "__main__" :
    if valite_board(board) == False :
        print('Works fine!')
    else :
        print("Works bad!")