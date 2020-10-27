from flask import Flask,render_template, request

app = Flask(__name__)


board = [
    [0, 0, 6, 0, 5, 4, 9, 0, 0],
    [1, 0, 0, 0, 6, 0, 0, 4, 2],
    [7, 0, 0, 0, 8, 9, 0, 0, 0],
    [0, 7, 0, 0, 0, 5, 0, 8, 1],
    [0, 5, 0, 3, 4, 0, 6, 0, 0],
    [4, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 3, 4, 0, 0, 0, 1, 0, 0],
    [9, 0, 0, 8, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 0, 3, 0, 7]
]


def solve(bo):
    board=bo
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # Square
    sq_x = pos[1] // 3
    sq_y = pos[0] // 3

    for i in range(sq_y * 3, sq_y * 3 + 3):
        for j in range(sq_x * 3, sq_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(b):
    inline=[]
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(str(b[i][j]) + " ", end="")
            inline.append(b[i][j])
            if j == 8:
                print("")
    return inline

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # return indexes as tuples
    return None

def check(solved_board,new_board):
    for i in range(len(solved_board)):
        for j in range(len(solved_board[0])):
            #print('new_board: {}'.format(type(new_board[i][j])))
            #print('solved_board: {}'.format(type(solved_board[i][j])))
            if solved_board[i][j]==new_board[i][j] :
                pass
            else:
                return False
    return True

def solved_board(bo):
    bo2=[]
    for i in range(len(bo)):
        inner_list=[]
        for j in range(len(bo[0])):
            inner_list.append(bo[i][j])
        bo2.append(inner_list)
        
    return bo2

'''print("Sudoku board")
print_board(board)
solve(board)
print("\nSolved board: ")
print("----------------------------------------------------------")
print_board(board)'''

@app.route("/", methods=["GET","POST"])
def index():
    inner_list=[]
    new_board=[]
    if request.method == 'POST':
        bo2=solved_board(board)
        if 'submit' in request.form.keys():
            count=1
            for item in range(11,100):
                if item%10==0:
                    continue
                else:
                    if count<10:
                        if request.form[str(item)] == '':
                            inner_list.append(0)
                        else:
                            inner_list.append(int(request.form[str(item)]))

                    if count==9:
                        count=1
                        new_board.append(inner_list)
                        inner_list=[]
                    else:
                        count+=1
            
            solve(bo2)
            result=check(bo2,new_board)
            if result != None:
                return render_template('try.html', form=new_board, result=result)

        if 'Solve' in request.form.keys():
            solve(bo2)
            return render_template('try.html',form=bo2, disable=True)

    return render_template('try.html',form=board)

if __name__ == "__main__":
    app.run(debug=True)