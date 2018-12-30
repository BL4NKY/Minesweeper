from tile import Tile
from board import Board
import  time

def menu():
    print()
    print()
    print()
    print("BUSCAMINES")
    print(40*"*")
    print("1.Taulell de 8x8 \t 10 mines \n2.Taulell 16x16 \t 40 mines \n3.Taulell 16x30 \t 99 mines \n4.Taulell personalizado \n5.Sortir")
    op = int(input("Escull una opció: "))
    return op

def menu2():
    print("Accions: '!' marcar, '?' marcar com dubtosa, 'x' desmarcar, ' ' destapar, 'q' sortir.")
    choice = input("Introdueix jugada (fila, columna, acció[!?x q]): ")  
    choice = choice[1:-1]
    (x,y,action) = choice.split(",")
    return int(x),int(y),action

find_mine = False    
total_tile = 0
total_mine = 0
flag_on_mine = 0
t_uncovered = 0
action = None
end = True
option = 0
while option != 5:
    option = menu()
    if option == 1:
        board = Board(8, 8, 10)
        print("                (◕‿◕)")
        print(board)
        total_tile = 64
        total_mine = 10
        end = False
        option = 5
    elif option == 2:
        board = Board(16, 16, 40)
        print("                (◕‿◕)")
        print(board)
        total_tile = 16 * 16
        total_mine = 40
        end = False
        option = 5
    elif option == 3:
        board = Board(16,30,99)
        print("                (◕‿◕)")
        print(board)
        total_tile = 16 * 30
        total_mine = 99
        end = False
        option = 5
    elif option == 4:    
        row = int(input("Introdueix el nombre de files [4-36]: "))
        while row < 4 or row > 36:
            print(f"El nombre ha de ser més gran que 4 i més petit que 36.")
            row = int(input("Introdueix el nombre de files [4-36]: "))
        column = int(input("Introdueix el nombre de columnes [4-36]: "))
        while column < 4 or column > 36:
            print(f"El nombre ha de ser més gran que 4 i més petit que 36.")
            column = int(input("Introdueix el nombre de columnes [4-36]: "))
        board = Board(int(row), int(column), round(0.15625 * int(row) * int(column)))
        print("              (◕‿◕)")
        print(board)
        total_mine = round(0.15625 * int(row) * int(column))
        total_tile = row * column
        end = False
        option = 5
    elif option != 5:
        print("Opció no vàlida.")
        option = menu()

if end == False:
    (x,y,action) = menu2()
    if x > board.row or y > board.column or x < 0 or y < 0:
                while x > board.row or y > board.column or x < 0 or y < 0:
                    print("Opció no vàlida.\n")
                    print("                (◕‿◕)")
                    print(board)
                    (x,y,action) = menu2()
    starting_time = time.time()
    while find_mine == False and action != "q" and total_tile != t_uncovered + flag_on_mine:
        if action == " ": 
            if board.board[x][y].get_uncovered() == True:
                print("La casella ja està destapada.\n")
            elif board.board[x][y].get_question() == True:
                print("Estas segur de destapar una casella marcada amb [?] ? ")
                resp = input("Si/No: ")
                if resp == "Si" or resp == "si":
                    if board.check_if_mine(x,y) == True:
                        find_mine = True
                    else:
                        board.board[x][y].set_question(False)  
                        board.uncover_adj(x,y)
                        t_uncovered = 0
                        for k in range(board.row):
                            for l in range(board.column):
                                if board.board[k][l].get_uncovered() == True:
                                    t_uncovered += 1
                elif resp == "No" or resp=="no":
                    print("D'acord.\n")
                else:
                    print("Resposta incorrecta.\n")   
            elif board.board[x][y].get_flag() == True:
                print("Estas segur de destapar una casella marcas amb [!] ? ")
                resp = input("Si/No: ")
                if resp == "Si" or resp== "si":
                    if board.check_if_mine(x,y) == True:
                        find_mine = True
                    else:
                        board.board[x][y].set_flag(False)  
                        board.uncover_adj(x,y)
                        t_uncovered = 0
                        for k in range(board.row):
                            for l in range(board.column):
                                if board.board[k][l].get_uncovered() == True:
                                    t_uncovered += 1
                elif resp == "No" or resp == "no":
                    print("D'acord.\n")
                else:
                    print("Resposta incorrecta.\n")
            else:
                if board.check_if_mine(x,y) == True:
                    find_mine = True
                else:
                    board.uncover_adj(x,y)
                    t_uncovered = 0
                    for k in range(board.row):
                        for l in range(board.column):
                            if board.board[k][l].get_uncovered() == True:
                                t_uncovered += 1
              
        elif action == "!":
            if board.board[x][y].get_uncovered() == True:
                print("La casella ja està destapada, no pots posar el [!].\n")
            elif board.board[x][y].get_flag() == True:
                print("La casella ja té [!]. \n")
            else:
                board.board[x][y].set_flag(True)
                if board.board[x][y].get_question() == True:
                    board.board[x][y].set_question(False)                    
                if board.board[x][y].get_mine() == True:
                    flag_on_mine = flag_on_mine + 1
                    
        elif action == "?":
            if board.board[x][y].get_uncovered() == True:
                print("La casella ja està destapada, no pots posar el [?]. \n")
            elif board.board[x][y].get_question == True:
                print("La casella ja té [?]. \n")
            else:
                board.board[x][y].set_question(True)
                if board.board[x][y].get_flag() == True:
                    board.board[x][y].set_flag(False)
                    
        elif action == "x":
            if board.board[x][y].get_flag() == True:
                 board.board[x][y].set_flag(False)      
                 if board.board[x][y].get_mine()==True:
                    flag_on_mine = flag_on_mine - 1 
            elif board.board[x][y].get_question() == True:
                 board.board[x][y].set_question(False)
            else:
                print("No hi ha ni [!] ni [?] en aquesta casella.\n")  
        
        elif action != "q":
            print("Opció no vàlida.\n")

        elapsed_time = time.time() - starting_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        minutes = str(minutes).zfill(2)
        seconds = str(seconds).zfill(2)
        print(f"Time: [{minutes}:{seconds}]", end = "   ")
        if find_mine == False and action != "q" and total_tile != t_uncovered + flag_on_mine:
            print("(◕‿◕)")
            print(board)
            (x,y,action) = menu2()
            if x > board.row or y > board.column or x < 0 or y < 0:
                while x > board.row or y > board.column or x < 0 or y < 0:
                    print("Opció no vàlida.")
                    elapsed_time = time.time() - starting_time
                    minutes = int(elapsed_time // 60)
                    seconds = int(elapsed_time % 60)
                    minutes = str(minutes).zfill(2)
                    seconds = str(seconds).zfill(2)
                    print(f"Time: [{minutes}:{seconds}]", end = "   ")
                    print("(◕‿◕)")
                    print(board)
                    (x,y,action) = menu2()
            
if end == False and find_mine == True:
    for k in range (board.row):
        for l in range (board.column):
            if board.board[k][l].get_mine() == True:   
                board.board[k][l].set_uncovered(True)
    print("(>﹏<)")
    print(board)
    print ("B\033[31mO\033[0mO\033[31mO\033[0mO\033[31mO\033[0mO\033[31mO\033[0mO\033[31mO\033[0mM!!")
    
elif end == False and total_tile == t_uncovered + flag_on_mine:
    print("(◕‿◕)")
    print(board)
    print("VICTORIA!!!!!")
                
else:
    print("Saliendo...")