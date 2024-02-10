import random
from threading import Timer
import time
import platform,socket,re,uuid,json,logging

name="qOS"
version="0.2"
chanael="alpha"
stability="unstable"

print(name+" "+version+" "+chanael+" "+stability)

def getSystemInfo():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)
        
print(getSystemInfo())
print("")

while True:
    def lst():
        print("1-calculator 8-eighth option")
        print("2-race game 9-nineth option")
        print("3-tic tac toe 10-tenth option")
        print("4-t rex runner 11-eleventh option")
        print("5-fifth option 12-twelweth option")
        print("6-sixth option 13-thirteenth option")
        print("7-seventh option 14-exit")
    
    lst()
    
    boot_scrn=float(input())
    
    if boot_scrn==14:
        u_sure=int(input("are you sure you want to exit 1-yes 2-no"))
        if u_sure==1:
            print("goodbye")
            break
        else:
            print("ok")
            boot_scrn=float(input())
    
    if boot_scrn==1:
        
        print("WARNING MULTPLICATION AND DIVISION SHOULD BE CALCULATED BEFORE ADDITION AND SUBTRACTION THIS CALCULATOR DOESN'T DO IT FOR YOU!!!")
        
        def calculation():
            print("1-addition")
            print("2-substraction")
            print("3-multiplication")
            print("4-division")
            print("5-exit")
            
            calc1=int(input())
            
            if calc1==5:
                print("")
            
            if calc1==1:
                print("enter numbers")
                n1=int(input())
                print("+")
                n2=int(input())
                print("=")
                print(n1+n2)
                n1=n1+n2
            
            if calc1==2:
                print("enter numbers")
                n1=int(input())
                print("-")
                n2=int(input())
                print("=")
                print(n1-n2)
                n1=n1-n2
            
            if calc1==3:
                print("enter numbers")
                n1=int(input())
                print("*")
                n2=int(input())
                print("=")
                print(n1*n2)
                n1=n1*n2
            
            if calc1==4:
                print("enter numbers")
                n1=int(input())
                print("/")
                n2=int(input())
                print("=")
                print(n1/n2)
                n1=n1/n2
            
            while True:
                
                print("1-addition")
                print("2-substraction")
                print("3-multiplication")
                print("4-division")
                print("5-exit")
                
                if calc1==5:
                    print("")
                    break
                
                calc1=int(input())
                
                if calc1==5:
                    print("")
                    break
                
                if calc1==1:
                    print("enter numbers")
                    print(n1)
                    print("+")
                    n2=int(input())
                    print("=")
                    print(n1+n2)
                    n1=n1+n2
                
                if calc1==2:
                    print("enter numbers")
                    print(n1)
                    print("-")
                    n2=int(input())
                    print("=")
                    print(n1-n2)
                    n1=n1-n2
                
                if calc1==3:
                    print("enter numbers")
                    print(n1)
                    print("*")
                    n2=int(input())
                    print("=")
                    print(n1*n2)
                    n1=n1*n2
                
                if calc1==4:
                    print("enter numbers")
                    print(n1)
                    print("/")
                    n2=int(input())
                    print("=")
                    print(n1/n2)
                    n1=n1/n2
                    
        calculation()
    
    if boot_scrn==2:
        def racer():
            while True:
                print("select a car")
                print("1-car1 speed-1 maneuverability-5")
                print("2-car2 speed-2 maneuverability-4")
                print("3-car3 speed-3 maneuverability-3")
                print("4-car4 speed-4 maneuverability-2")
                print("5-car5 speed-5 maneuverability-1")
                print("6-exit")
                
                car_slct=int(input())
                
                if car_slct==6:
                    print("")
                    break
                
                if car_slct==1:
                    car="car1"
                    speed=5
                    timeme=5
                    print("you have selected " + car)
                
                if car_slct==2:
                    car="car2"
                    speed=4
                    timeme=4
                    print("you have selected " + car)
                
                if car_slct==3:
                    car="car3"
                    speed=3
                    timeme=3
                    print("you have selected " + car)
                
                if car_slct==4:
                    car="car4"
                    speed=2
                    timeme=2
                    print("you have selected " + car)
                
                if car_slct==5:
                    car="car5"
                    speed=1
                    timeme=1
                    print("you have selected " + car)
                
                win=0
                
                storto = time.time()
                
                for i in range(20):
                    win=win+1
                    L=random.randint(0, 1)
                    S=random.randint(0, 1)
                    R=random.randint(0, 1)
                    
                    if L==0:
                        left="you cant go left"
                    
                    if L==1:
                        left="you can go left"
                    
                    if S==0:
                        straight="you cant go straight"
                    
                    if S==1:
                        straight="you can go straight"
                    
                    if R==0:
                        right="you cant go right"
                    
                    if R==1:
                        right="you can go right"
                    
                    if L==0 and S==0 and R==0:
                        S=1
                        straight="you can go straight"
                    print("1-go right")
                    print("2-go straight")
                    print("3-go left")
                    print(right + " " + straight + " " + left)
                    
                    timeout = speed
                    t = Timer(timeout, print, ["game over - you ran out of time"])
                    t.start()
                    prompt = "You have %d seconds to enter the direction\n" % timeout
                    direction = int(input(prompt))
                    t.cancel()
                    
                    if (direction==1 and R==1) or (direction==2 and S==1) or (direction==3 and L==1):
                        print("going to the next intersection")
                        time.sleep(timeme)
                        print("well done")
                    else:
                        print("game over - you crashed")
                        print("")
                        break
                
                end = time.time()
                tme = end - storto
                tme = round(tme, 2)
                
                
                if win==20:
                    print("you won with the time of " + str(tme))
                    
                
                
        racer()
    if boot_scrn==3:
        board = [str(i) for i in range(1, 10)]
        
        X = "X"
        O = "O"
        
        winning_combos = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        def print_board():
            print("\n")
            print(board[0] + " | " + board[1] + " | " + board[2])
            print("---------")
            print(board[3] + " | " + board[4] + " | " + board[5])
            print("---------")
            print(board[6] + " | " + board[7] + " | " + board[8])
            print("\n")

        def is_full():
            return all(symbol in [X, O] for symbol in board)

        def has_won(symbol):
            return any(all(board[i] == symbol for i in combo) for combo in winning_combos)

        def get_available_moves():
            return [i for i, symbol in enumerate(board) if symbol not in [X, O]]

        def get_best_move(symbol, depth, alpha, beta):
            if has_won(X):
                return -10 + depth, None
            if has_won(O):
                return 10 - depth, None
            if is_full():
                return 0, None
            
            if symbol == O:
                best_score = -float("inf")
                best_move = None
            else:
                best_score = float("inf")
                best_move = None
            
            for move in get_available_moves():
                board[move] = symbol
                score, _ = get_best_move(O if symbol == X else X, depth + 1, alpha, beta)
                board[move] = str(move + 1)
                if symbol == O:
                    if score > best_score:
                        best_score = score
                        best_move = move
                    alpha = max(alpha, best_score)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = move
                    beta = min(beta, best_score)
                if alpha >= beta:
                    break
            
            return best_score, best_move

        def get_random_move():
            return random.choice(get_available_moves())

        def get_computer_move(difficulty):
            if difficulty == 100:
                _, move = get_best_move(O, 0, -float("inf"), float("inf"))
                return move
            elif difficulty == 0:
                return get_random_move()
            else:
                r = random.randint(0, 100)
                if r <= difficulty:
                    _, move = get_best_move(O, 0, -float("inf"), float("inf"))
                    return move
                else:
                    return get_random_move()

        def get_user_move(symbol):
            while True:
                move = input(f"enter a number (1-9) to place {symbol} on the board: ")
                try:
                    move = int(move) - 1
                    if move in get_available_moves():
                        return move
                    else:
                        print("that spot is already taken or out of range. try again.")
                except ValueError:
                    print("that is not a valid number. try again.")

        def play_game():
            print("tic tac toe!")
            while True:
                mode = input("enter 1 for one player game or 2 for two players game: ")
                if mode in ["1", "2"]:
                    break
                else:
                    print("that is not a valid option. try again.")

            if mode == "1":
                while True:
                    difficulty = input("enter a difficulty from 0 (easy) to 100 (unbeatable): ")
                    try:
                        difficulty = int(difficulty)
                        if 0 <= difficulty <= 100:
                            break
                        else:
                            print("that is not a valid difficulty. try again.")
                    except ValueError:
                        print("that is not a valid number. try again.")

            turn = X

            while True:
                global board
                print_board()
                if has_won(X):
                    print(f"{X} has won the game!")
                    break
                if has_won(O):
                    print(f"{O} has won the game!")
                    break
                if is_full():
                    print("The game is a tie!")
                    break
                if mode == "1" and turn == O:
                    print(f"It is {O}'s turn.")
                    move = get_computer_move(difficulty)
                else:
                    move = get_user_move(turn)
                board[move] = turn
                turn = O if turn == X else X

            print_board()

            while True:
                choice = input("1-play agin 2-exit")
                if choice in ["1", "2"]:
                    break
                else:
                    print("that is not a valid option. try again.")

            if choice == "1":
                board = [str(i) for i in range(1, 10)]
                play_game()
            elif choice == "2":
                print("exitting")

        play_game()

    
    if boot_scrn==4:
        
        import random
        import time
        import sys
        import select
        
        def alldef():
            global q1, w1, e1, r1, t1, z1, u1, i1, o1, p1, a1, s1, d1, f1, g1, h1, j1, k1, l1
            global q2, w2, e2, r2, t2, z2, u2, i2, o2, p2, a2, s2, d2, f2, g2, h2, j2, k2, l2
            global q3, w3, e3, r3, t3, z3, u3, i3, o3, p3, a3, s3, d3, f3, g3, h3, j3, k3, l3
            global jumped, score, x, z, ovlc, ocvl, olcv, pvlc, pcvl, plcv
            q1="⠀"
            w1="⠀"
            e1="⠀"
            r1="⠀"
            t1="⠀"
            z1="⠀"
            u1="⠀"
            i1="⠀"
            o1="⠀"
            p1="⠀"
            a1="⠀"
            s1="⠀"
            d1="⠀"
            f1="⠀"
            g1="⠀"
            h1="⠀"
            j1="⠀"
            k1="⠀"
            l1="⠀"
            q2="⠀"
            w2="⠀"
            e2="⠀"
            r2="⠀"
            t2="⠀"
            z2="⠀"
            u2="⠀"
            i2="⠀"
            o2="⠀"
            p2="⠀"
            a2="⠀"
            s2="⠀"
            d2="⠀"
            f2="⠀"
            g2="⠀"
            h2="⠀"
            j2="⠀"
            k2="⠀"
            l2="⠀"
            q3="⠀"
            w3="⠀"
            e3="⠀"
            r3="⠀"
            t3="⠀"
            z3="□"
            u3="⠀"
            i3="⠀"
            o3="⠀"
            p3="⠀"
            a3="⠀"
            s3="⠀"
            d3="⠀"
            f3="⠀"
            g3="⠀"
            h3="⠀"
            j3="⠀"
            k3="⠀"
            l3="⠀"
            
            x=0
            z=0
            ovlc=0
            ocvl=0
            olcv=0
            pvlc=0
            pcvl=0
            plcv=0
            
            score=0
            jumped=0
        
        alldef()
        
        def runner():
            while True:
                global q1, w1, e1, r1, t1, z1, u1, i1, o1, p1, a1, s1, d1, f1, g1, h1, j1, k1, l1
                global q2, w2, e2, r2, t2, z2, u2, i2, o2, p2, a2, s2, d2, f2, g2, h2, j2, k2, l2
                global q3, w3, e3, r3, t3, z3, u3, i3, o3, p3, a3, s3, d3, f3, g3, h3, j3, k3, l3
                global jumped, score, x, z, ovlc, ocvl, olcv, pvlc, pcvl, plcv
                
                
                
                print(score)
                score=score+1
                
                print(q1+w1+e1+r1+t1+z1+u1+i1+o1+p1+a1+s1+d1+f1+g1+h1+j1+k1+l1)
                print(q2+w2+e2+r2+t2+z2+u2+i2+o2+p2+a2+s2+d2+f2+g2+h2+j2+k2+l2)
                print(q3+w3+e3+r3+t3+z3+u3+i3+o3+p3+a3+s3+d3+f3+g3+h3+j3+k3+l3)
                
                randomlow = random.randint(1,10)
                randomhigh= random.randint(1,20)
                
                if q1!="■" and w1!="■" and e1!="■" and r1!="■" and t1!="■" and z1!="■" and u1!="■" and i1!="■" and o1!="■" and p1!="■" and a1!="■" and s1!="■" and d1!="■" and f1!="■" and g1!="■" and h1!="■" and j1!="■" and k1!="■" and l1!="■":
                    if q2!="■" and w2!="■" and e2!="■" and r2!="■" and t2!="■" and z2!="■" and u2!="■" and i2!="■" and o2!="■" and p2!="■" and a2!="■" and s2!="■" and d2!="■" and f2!="■" and g2!="■" and h2!="■" and j2!="■" and k2!="■" and l2!="■":
                        if q3!="■" and w3!="■" and e3!="■" and r3!="■" and t3!="■" and z3!="■" and u3!="■" and i3!="■" and o3!="■" and p3!="■" and a3!="■" and s3!="■" and d3!="■" and f3!="■" and g3!="■" and h3!="■" and j3!="■" and k3!="■" and l3!="■":
                            if randomhigh== 10:
                                l2="■"
                                l3="■"
                            elif randomlow==5:
                                l3="■"
                
                if z1!="□" and z2!="□" and z3!="□":
                    print("you lost 1-play agin 2-exit")
                    losing=int(input())
                    if losing==1:
                        alldef()
                        runner()
                    else:
                        print("your score was "+score+" , exitting")
                        break
                
                if u3=="■":
                    pcvl=1
                    pvlc=0
                elif pcvl==1:
                    pvlc=2
                    pcvl=0
                elif pvlc==2:
                    plcv=3
                    pvlc=0
                elif plcv==3 and r3!="■":
                    print("you lost 1-play agin 2-exit")
                    losing=int(input())
                    if losing==1:
                        alldef()
                        runner()
                    else:
                        print("your score was "+score+" , exitting")
                        break
                else:
                    pvlc=0
                    pcvl=0
                    plcv=0
                
                if u2=="■":
                    ocvl=1
                    ovlc=0
                elif ocvl==1:
                    ovlc=2
                    ocvl=0
                elif ovlc==2:
                    olcv=3
                    ovlc=0
                elif olcv==3 and t2!="■":
                    print("you lost 1-play agin 2-exit")
                    losing=int(input())
                    if losing==1:
                        alldef()
                        runner()
                    else:
                        print("your score was "+score+" , exitting")
                        break
                else:
                    ovlc=0
                    ocvl=0
                    olcv=0
                
                
                
                if u1=="■":
                    ocvl=1
                    ovlc=0
                elif ocvl==1:
                    ovlc=2
                    ocvl=0
                elif ovlc==2 and t1!="■":
                    print("you lost 1-play agin 2-exit")
                    losing=int(input())
                    if losing==1:
                        runner()
                    else:
                        print("your score was "+score+" , exitting")
                        break
                else:
                    ovlc=0
                    ocvl=0
                
                if l3=="■":
                    k3="■"
                    l3="⠀"
                elif k3=="■":
                    j3="■"
                    k3="⠀"
                elif j3=="■":
                    h3="■"
                    j3="⠀"
                elif h3=="■":
                    g3="■"
                    h3="⠀"
                elif g3=="■":
                    f3="■"
                    g3="⠀"
                elif f3=="■":
                    d3="■"
                    f3="⠀"
                elif d3=="■":
                    s3="■"
                    d3="⠀"
                elif s3=="■":
                    a3="■"
                    s3="⠀"
                elif a3=="■":
                    p3="■"
                    a3="⠀"
                
                if l2=="■":
                    k2="■"
                    l2="⠀"
                elif k2=="■":
                    j2="■"
                    k2="⠀"
                elif j2=="■":
                    h2="■"
                    j2="⠀"
                elif h2=="■":
                    g2="■"
                    h2="⠀"
                elif g2=="■":
                    f2="■"
                    g2="⠀"
                elif f2=="■":
                    d2="■"
                    f2="⠀"
                elif d2=="■":
                    s2="■"
                    d2="⠀"
                elif s2=="■":
                    a2="■"
                    s2="⠀"
                elif a2=="■":
                    p2="■"
                    a2="⠀"
                
                if l1=="■":
                    k1="■"
                    l1="⠀"
                elif k1=="■":
                    j1="■"
                    k1="⠀"
                elif j1=="■":
                    h1="■"
                    j1="⠀"
                elif h1=="■":
                    g1="■"
                    h1="⠀"
                elif g1=="■":
                    f1="■"
                    g1="⠀"
                elif f1=="■":
                    d1="■"
                    f1="⠀"
                elif d1=="■":
                    s1="■"
                    d1="⠀"
                elif s1=="■":
                    a1="■"
                    s1="⠀"
                elif a1=="■":
                    p1="■"
                    a1="⠀"
                
                if p3=="■":
                    o3="■"
                    p3="⠀"
                elif o3=="■":
                    i3="■"
                    o3="⠀"
                elif i3=="■":
                    u3="■"
                    i3="⠀"
                elif u3=="■":
                    z3="■"
                    u3="⠀"
                elif z3=="■":
                    t3="■"
                    z3="⠀"
                elif t3=="■":
                    r3="■"
                    t3="⠀"
                elif r3=="■":
                    e3="■"
                    r3="⠀"
                elif e3=="■":
                    w3="■"
                    e3="⠀"
                elif w3=="■":
                    q3="■"
                    w3="⠀"
                elif q3=="■":
                    q3="⠀"
                
                
                
                if p2=="■":
                    o2="■"
                    p2="⠀"
                elif o2=="■":
                    i2="■"
                    o2="⠀"
                elif i2=="■":
                    u2="■"
                    i2="⠀"
                elif u2=="■":
                    z2="■"
                    u2="⠀"
                elif z2=="■":
                    t2="■"
                    z2="⠀"
                elif t2=="■":
                    r2="■"
                    t2="⠀"
                elif r2=="■":
                    e2="■"
                    r2="⠀"
                elif e2=="■":
                    w2="■"
                    e2="⠀"
                elif w2=="■":
                    q2="■"
                    w2="⠀"
                elif q2=="■":
                    q2="⠀"
                
                
                
                if p1=="■":
                    o1="■"
                    p1="⠀"
                elif o1=="■":
                    i1="■"
                    o1="⠀"
                elif i1=="■":
                    u1="■"
                    i1="⠀"
                elif u1=="■":
                    z1="■"
                    u1="⠀"
                elif z1=="■":
                    t1="■"
                    z1="⠀"
                elif t1=="■":
                    r1="■"
                    t1="⠀"
                elif r1=="■":
                    e1="■"
                    r1="⠀"
                elif e1=="■":
                    w1="■"
                    e1="⠀"
                elif w1=="■":
                    q1="■"
                    w1="⠀"
                elif q1=="■":
                    q1="⠀"
                
                def input_with_timeout(prompt, timeout):
                    print(prompt)
                    i, o, e = select.select([sys.stdin], [], [], timeout)
                    if i:
                        return sys.stdin.readline().strip()
                    else:
                        return None
                
                user_input = input_with_timeout("\/press enter to jump\/", 0.2)
                if user_input is None:
                    print()
                    
                    if jumped==2:
                        z2="⠀"
                        z1="□"
                        jumped=3
                    
                    elif jumped==3:
                        z1="□"
                        jumped=4
                    
                    elif jumped==4:
                        z1="□"
                        jumped=4.5
                    
                    elif jumped==4.5:
                        z1="□"
                        jumped=5
                    
                    elif jumped==5:
                        z1="⠀"
                        z2="□"
                        jumped=6
                    
                    elif jumped==6:
                        z2="⠀"
                        z3="□"
                        jumped=0
                else:
                    if jumped==0:
                        jumped=1
                    if jumped==1:
                        z3="⠀"
                        z2="□"
                        jumped=2
                        
                    elif jumped==2:
                        z2="⠀"
                        z1="□"
                        jumped=3
                    
                    elif jumped==3:
                        z1="□"
                        jumped=4
                    
                    elif jumped==4:
                        z1="□"
                        jumped=4.5
                    
                    elif jumped==4.5:
                        z1="□"
                        jumped=5
                    
                    elif jumped==5:
                        z1="⠀"
                        z2="□"
                        jumped=6
                    
                    elif jumped==6:
                        z2="⠀"
                        z3="□"
                        jumped=0
                    
        runner()
        

