from tkinter import *
import tkinter.messagebox
from random import randint

class CallPy():
    def __init__(self):
        self.puzle=False
        self.mainboard=[[0 for i in range(9)] for j in range(9)]
        pass
    
    def suduko(self):
        global board
        global possible
        global t1
        idontknow=True
        board=list()
        possible = list()
        boards = list()
        possibles = list()
        co_ordinate = list()
        set_of_number = {1,2,3,4,5,6,7,8,9}
        test = self.mainboard
        for i in range(len(test)):
                board.append(test[i])
        for i in range(9):
            for j in range(9):
                try:
                    if int(board[i][j])>-1 and int(board[i][j])<10:
                        board[i][j]=int(board[i][j])
                    else:
                        board = None
                except:
                    board = None
                    break
            if board == None:
                break
        
        def grid(t,board):
            grid = set()
            lis = list()
            i = (t[0]//3)
            j = (t[1]//3)
            for l in range(3):
                for k in range(3):
                    lis.append(board[(3*i+l)][(3*j+k)])
            for m in range(1,10):
                if m not in lis:
                    grid.add(m)
            return grid
        def row(t,board):
            row = set()
            lis = list()
            i = t[0]
            for m in range(9):
                lis.append(board[i][m])
            for j in range(1,10):
                if j not in lis:
                    row.add(j)
            return row
        def column(t,board):
            column = set()
            lis = list()
            i = t[1]
            for m in range(9):
                lis.append(board[m][i])
            for j in range(1,10):
                if j not in lis:
                    column.add(j)
            return column
        def hiddenrow(t):
            i = t[0]
            j = t[1]
            want = [k for k in range(9) if k!=j]
            poss = set()
            for j1 in want:
                if board[i][j1] ==0:
                    t=row((i,j1),board)&column((i,j1),board)&grid((i,j1),board)
                    poss=poss|t
                else:
                    poss.add(board[i][j1])
            if poss&set_of_number!=set_of_number:
                for j in range(1,10):
                    if j not in poss:
                        return j
            else:
                return False
        def hiddencolumn(t):
            i = t[0]
            j = t[1]
            want = [k for k in range(9) if k!=i]
            poss = set()
            for j1 in want:
                if board[j1][j] ==0:
                    t=row((j1,j),board)&column((j1,j),board)&grid((j1,j),board)
                    poss=poss|t
                else:
                    poss.add(board[j1][j])
            t=row((i,j),board)&column((i,j),board)&grid((i,j),board)
            if poss&set_of_number!=set_of_number:
                for j in range(1,10):
                    if j not in poss:
                        return j
            else:
                return False
        def hiddengrid(t):
            i = t[0]
            j = t[1]
            r1 = i%3
            r2 =j%3
            wa = [i for i in range(3) if i!=r1]
            wan = [i for i in range(3) if i!=r2]
            poss = set()
            for m in wa:
                for n in wan:
                    x=3*(i//3)+m
                    y=3*(j//3)+n
                    if board[x][y]==0:
                        t=row((x,y),board)&column((x,y),board)&grid((x,y),board)
                        poss=poss|t
                    else:
                        poss.add(board[i][j])
            if poss&set_of_number==set_of_number:
                for j in range(1,10):
                    if j not in poss:
                        return j
            else:
                return False
        def check(possible):
            check = True
            for i in range(9):
                for j in range(9):
                    if type(possible[i][j]) == list:
                        if len(possible[i][j]) ==0:
                            check = False
                            break
            return check
        def back_forward_track(check,test):
            global board
            global possible
            global gama
            global t1
            x=board.copy()
            boards.append(x)
            processor()
            if check == True:

                gama=possible.copy()
                possibles.append(gama)
                for element in range(2,9):
                    for i in range(9):
                        for j in range(9):
                            if board[i][j]==0:
                                if len(possible[i][j])==element:
                                    break
                        if board[i][j]==0:
                            if len(possible[i][j])==element:
                                break
                    if board[i][j]==0:
                        if len(possible[i][j])==element:
                            break
                co_ordinate.append([(i,j),0])
                board[i][j]=possible[i][j][0]
                possible[i][j]=0
                processor()
            elif check == False:
                print('intial problem')
                for i in self.mainboard:
                    print(i)
                print('board before')
                for i in board:
                    print(i)
                t=1
                for i in boards:
                    print(t)
                    t=t+1
                    for j in i:
                        print(j)
                possible = possibles.pop()
                possible=possibles.pop()
                location = co_ordinate.pop()
                position = location[0]
                turn = location[1]
                
                if len(possible[position[0]][position[1]])>location[1]+1:
                    boards.append(board)
                    possibles.append(possible)
                    co_ordinate.append([(i,j),location[1]+1])
                    board[position[0]][position[1]]=possible[position[0]][position[1]][location[1]+1]
                    possible[position[0]][position[1]]=0
                    processor()
                else:
                    back_forward_track(False,False)
                
                pass
            
        def cheacker(L):
            a = True
            for b in range(1,10):
                if L.count(b)>1:
                    a = False
                    break
            return a
        def checkrow():
            k = True
            for i in range(9):
                listt = list()
                for j in range(9):
                    listt.append(board[i][j])

                k = k&cheacker(listt)
            return k
        def checkcolumn():
            k = True
            for i in range(9):
                listt = list()
                for j in range(9):
                    listt.append(board[j][i])

                k = k&cheacker(listt)
            return k
        def checkgrid():
            tell = True
            for k in range(3):
                for l in range(3):
                    listt = list()
                    for i in range(3):
                        for j in range(3):
                            listt.append(board[3*k+i][3*l+j])
                    tell = tell&cheacker(listt)
            return tell
        def processor():
            
            global board
            global possible
            for i in range(9):
                        for j in range(9):
                            if board[i][j] ==0:
                                l=[]
                                t=row((i,j),board)&column((i,j),board)&grid((i,j),board)
                                for num in range(1,10):
                                    if num in t:
                                        l.append(num)
                                possible[i][j] = l
                                for c in possible:
                                    for b in c:
                                        if type(b)==list:
                                            if len(b)==1:
                                                board[i][j]=b[0]
                                                possible[i][j]=0
        possible =[[0 for i in range(9)] for j in range(9)]
        counti = 0
        work = True
        if board==None:
            work = False

        while(work):
            limitator= True
            while(True):
                k = True
                for i in range(9):
                    for j in range(9):
                        if board[i][j] ==0:
                            l=[]
                            t=row((i,j),board)&column((i,j),board)&grid((i,j),board)
                            for num in range(1,10):
                                if num in t:
                                    l.append(num)
                            possible[i][j] = l
                            for c in possible:
                                for b in c:
                                    if type(b)==list:
                                        if len(b)==1:
                                            board[i][j]=b[0]
                                            possible[i][j]=0
                                            limitator = False
                                            k = False
                if k==True:
                    break
            #hidden singles____________
            # means when possible outcome of row's element or value except a particular element does not get to be 
            #a complete set of 1 to 10 then the its value is that missing no.
            while(True):
                k = True
                for i in range(9):
                    for j in range(9):
                        if board[i][j]==0:
                            if hiddenrow((i,j))!=False:
                                if hiddenrow((i,j))!=None:
                                    board[i][j]=hiddenrow((i,j))
                                    possible[i][j]=0
                                    k = False
                                    limitator=False
                                continue
                            if hiddencolumn((i,j))!=False:
                                if hiddenrow((i,j))!=None:
                                    board[i][j]=hiddencolumn((i,j))
                                    possible[i][j]=0
                                    k = False
                                    limitator=False
                                    continue
                            if hiddengrid((i,j))!=False:
                                if hiddengrid((i,j))!=None:
                                    board[i][j]=hiddengrid((i,j))
                                    possible[i][j]=0
                                    k = False
                                    limitator = False
                                    continue
                
                if k ==True:
                    break

            #backtracking__________________________________________

            v = True
            a = True
            l = list()

            l.append(check(possible))

            if False in l:
                a = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] ==0:
                        v=False
                        break
                if board[i][j] ==0:
                    v=False
                    break
            if v == False:
                processor()
                
                back_forward_track(a,idontknow)
                idontknow=False
                processor()
                test = checkcolumn()&checkgrid()&checkrow()
                if test==False:
                    for i in board:
                        print(i)
                    print(len(boards))
                    board=None
                    break
                continue

            break
        return board
    def fun(t):
        c[t[0]][t[1]]['fg']='black'
    def show(self,state):
        if state==True:
            a = self.suduko()
            if a!=None:
                for x in range(9):
                    for y in range(9):
                        self.fun((x,y))
                        c[x][y].delete('1.0',END)
                        c[x][y].insert(END,a[x][y])

            else:
                iExit = tkinter.messagebox.askyesno("Suduko",
                                                    "You have entered WRONG puzzle want to play again")
                if iExit>0:
                    sudukoo.destroy()
                    self.__python__('SUDUKO.py')
                else:
                    sudukoo.destroy()
                pass
        elif state == False:
            a = self.suduko()
            set=[]
            for i in range(1,57):
                al = randint(0,80)
                while(True):
                    if al not in set:
                        set.append(al)
                        break
                    else:
                        al=randint(0,80)
            for i in range(50):
                l=set[i]%9
                l2=int((set[i]-l)/9)
                a[l][l2]=0
            if a!=None:
                for x in range(9):
                    for y in range(9):
                        if a[x][y]==0:
                            c[x][y]=Text(myCanvas,background='whitesmoke',fg='#333333',font=('times',20,'bold'),width = 4,height=1,relief=GROOVE,bd = 0)
                            c[x][y].grid(row = x,column = y,padx=2,pady=2)
                        else:
                            c[x][y]=Text(myCanvas,background='whitesmoke',font=('times',20,'bold'),width = 4,relief=GROOVE,height=1,bd = 0)
                            c[x][y].insert(END,a[x][y])
                            c[x][y].configure(state=DISABLED)
                            c[x][y].grid(row = x,column = y,padx=2,pady= 2)
        else:
            value=[[0 for i in range(9)] for t in range(9)]
            for x in range(9):
                for y in range(9):
                    c[x][y].configure(state=NORMAL)
                    c[x][y].delete('1.0',END)
                    self.mainboard=value
    def value(self):
        value = [[0 for x in range(9)] for x in range(9)]
        for x in range(9):
            for y in range(9):
                if c[x][y].get('1.0','end-1c') !=None:
                    if c[x][y].get('1.0','end-1c').isalpha()==False:

                        try:
                            value[x][y]=int(c[x][y].get('1.0','end-1c'))
                        except:
                            pass
                    else:
                        value[x][y]=12

        self.mainboard=value
        self.show(True)
    def puzzle(self,statement):
        self.puzle=True
        if statement==True:
            puzle=True
            set=[]
            for i in range(1,6):
                a = randint(0,80)
                while(True):
                    if a not in set:
                        set.append(a)
                        break
                    else:
                        a=randint(0,80)
            value = [[0 for x in range(9)] for x in range(9)]
            for i in range(4):
                a=set[i]%9
                b=int((set[i]-a)/9)
                value[a][b]=i+1
            self.mainboard=value
            self.show(False)
        else:
            value=[[0 for i in range(9)] for j in range(9)]
            self.mainboard=value
            self.show('nothing')

    def fun(self,t):
        c[t[0]][t[1]]['fg']='black'
    def checking(self):
        if self.puzle==True:
            value = [[0 for x in range(9)] for x in range(9)]
            for x in range(9):
                for y in range(9):
                    if c[x][y].get('1.0','end-1c') !=None:
                        if c[x][y].get('1.0','end-1c').isalpha()==False:

                            try:
                                value[x][y]=int(c[x][y].get('1.0','end-1c'))
                            except:
                                pass
                        else:
                            value[x][y]=12
            a=self.suduko()
            for i in range(9):
                for j in range(9):
                    if value[i][j]==a[i][j]:
                        c[i][j]['fg']='green'
                    elif (value[i][j]) in [i for i in range(1,10)]:
                        c[i][j]['fg']='red'
                        c[i][j].bind('<Button-1>', lambda e,m =(i,j): self.fun(m))
                    else:
                        pass
        else:
            pass
    def testpuzzle(self):
        set=[]
        for i in range(1,6):
            a = randint(0,80)
            while(True):
                if a not in set:
                    set.append(a)
                    break
                else:
                    a=randint(0,80)
        value = [[0 for x in range(9)] for x in range(9)]
        for i in range(4):
            a=set[i]%9
            b=int((set[i]-a)/9)
            value[a][b]=i+1
        self.mainboard=value
    def testsolvep(self):
        a = self.suduko()
        set=[]
        for i in range(1,57):
            al = randint(0,80)
            while(True):
                if al not in set:
                    set.append(al)
                    break
                else:
                    al=randint(0,80)
        for i in range(50):
            l=set[i]%9
            l2=int((set[i]-l)/9)
            a[l][l2]=0
        self.mainboard=a
if __name__=='__main__':
    body=CallPy()
   
    sudukoo = Tk()
    sudukoo.title('Suduko')
    sudukoo.geometry('563x401')
    sudukoo.resizable(False,False)
    main1 = Frame(sudukoo)
    main1.pack(fill='both',expand=1)
    myCanvas=Canvas(main1)
    myCanvas.pack(side=LEFT,fill='both',expand=1)
    myCanvas.create_line(0,38,800,38,fill= 'black',width=1)
    myCanvas.create_line(0,75,800,75,fill= 'black',width=1)
    myCanvas.create_line(0,186,800,186,fill= 'black',width=1)
    myCanvas.create_line(0,149,800,149,fill= 'black',width=1)
  
    myCanvas.create_line(0,294,800,294,fill= 'black',width=1)
    
    myCanvas.create_line(0,257,800,257,fill= 'black',width=1)
    

    #.....
    myCanvas.create_line(62,0,62,330,fill= 'black',width=1)
    myCanvas.create_line(124,0,124,330,fill= 'black',width=1)
    myCanvas.create_line(248,0,248,330,fill= 'black',width=1)
    myCanvas.create_line(310,0,310,330,fill= 'black',width=1)
    myCanvas.create_line(434,0,434,330,fill= 'black',width=1)
    myCanvas.create_line(496,0,496,330,fill= 'black',width=1)
    
    #////
    myCanvas.create_line(0,111,800,111,fill= 'black',width=3)
    myCanvas.create_line(0,221,800,221,fill= 'black',width=3)
    myCanvas.create_line(186,0,186,330,fill= 'black',width=3)
    myCanvas.create_line(371,0,371,330,fill= 'black',width=3)
    c = [[0 for x in range(9)] for x in range(9)]
    for x in range(9):
        for y in range(9):
            c[x][y]=Text(myCanvas,background='whitesmoke',font=('times',20,'bold'),width = 4,height=1,relief=GROOVE,bd = 0)
            c[x][y].grid(row = x,column = y,padx=2,pady=2)
    cheak=Button(main1, text='Check',
                      width=9, height=1,
                      bg='whitesmoke',
                      font=('Helvetica', 14, 'bold'),
                      bd=4,
                      command=lambda: body.checking()).place(x=220,y=345)

    Procced = Button(main1, text='Solve',
                      width=9, height=1,
                      bg='whitesmoke',
                      font=('Helvetica', 14, 'bold'),
                      bd=4,
                      command=lambda: body.value()).place(x=400,y=345)
    new =Button(main1, text='New',
                      width=4, height=1,
                      bg='whitesmoke',
                      font=('Helvetica', 14, 'bold'),
                      bd=4,
                      command=lambda: body.puzzle(False)).place(x=30,y=345)
    puzz = Button(main1, text='Puzzle',
                      width=5, height=1,
                      bg='whitesmoke',
                      font=('Helvetica', 14, 'bold'),
                      bd=4,
                      command=lambda: body.puzzle(True)).place(x=90,y=345)
    sudukoo.mainloop()