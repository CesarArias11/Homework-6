
def playing_board(row, column):
    for i in range(row):
        for i in range(column):
            print("|", end=" ")
        print("")
        if i != row-1:
            for i in range(column):
                print("-", end=" ")
        print("")


playing_board(5, 9)
