import time
from tkinter import *
import random

#Tkinter functions　配置Tkinter功能
def onclick1():
    global Mode
    Mode = 1
    r1.destroy()
def onclick2():
    global Mode
    Mode = 2
    r1.destroy()
def onclick3():
    global Mode
    Mode = 3
    r1.destroy()
def onclick4():
    global Mode
    Mode = 4
    r1.destroy()
#File paths 文件路径
class path:
    image = r".\resources\back.gif"
    imagr = r".\resources\r.gif"
    imagg = r".\resources\g.gif"
    imagy = r".\resources\y.gif"
    imagb = r".\resources\b.gif"
    imagind = [r".\resources\ind2.gif",r".\resources\ind3.gif",r".\resources\ind4.gif"]
#Parameter Variables 参数变量
res = 'y'
current = 1
#Basic game function 基础游戏功能
class gameplay:
    def __init__(self, player, step):
        self.player = player
        self.step = step
    def move(player,step):
        global pr,pg,py,pb
        if player == 1:
            obj=pr
        elif player == 2:
            obj=pg
        elif player == 3:
            obj=py
        elif player == 4:
            obj=pb
        #print(player,step,canvas2.coords(obj))
        x=0
        if (canvas2.coords(obj)[0]+(step*80))>760 and canvas2.coords(obj)[1]==40:
            warning=canvas2.create_text(900,450,text="Too far",font=('Consolas',20))
            canvas2.update()
            time.sleep(1.5)
            canvas2.delete(warning)
            x=7
        while(x<step):
            if canvas2.coords(obj)[0]>=760 and canvas2.coords(obj)[1]!=40:
                canvas2.move(obj,-720,-80)
            else:
                canvas2.move(obj,80,0)
            x=x+1
            canvas2.update()
            time.sleep(0.3)
        if canvas2.coords(obj)==[200,760]:
            canvas2.coords(obj,40,360)
            canvas2.update()
        elif canvas2.coords(obj)==[440,760]:
            canvas2.coords(obj,520,600)
            canvas2.update()
        elif canvas2.coords(obj)==[760,680]:
            canvas2.coords(obj,760,280)
            canvas2.update()
        elif canvas2.coords(obj)==[440,520]:
            canvas2.coords(obj,360,360)
            canvas2.update()
        elif canvas2.coords(obj)==[200,280]:
            canvas2.coords(obj,360,40)
            canvas2.update()
        elif canvas2.coords(obj)==[600,280]:
            canvas2.coords(obj,600,40)
            canvas2.update()
        elif canvas2.coords(obj)==[360,600]:
            canvas2.coords(obj,360,760)
            canvas2.update()
        elif canvas2.coords(obj)==[280,520]:
            canvas2.coords(obj,40,760)
            canvas2.update()
        elif canvas2.coords(obj)==[520,440]:
            canvas2.coords(obj,680,680)
            canvas2.update()
        elif canvas2.coords(obj)==[360,280]:
            canvas2.coords(obj,120,360)
            canvas2.update()
        elif canvas2.coords(obj)==[520,120]:
            canvas2.coords(obj,520,360)
            canvas2.update()
        elif canvas2.coords(obj)==[440,760]:
            canvas2.coords(obj,520,600)
            canvas2.update()
        elif canvas2.coords(obj)==[40,40]:
            canvas2.coords(obj,40,280)
            canvas2.update()
        elif canvas2.coords(obj)==[680,40]:
            canvas2.coords(obj,680,280)
            canvas2.update()
        elif canvas2.coords(obj)==[760,40]:
            gameplay.winner(player)
    def play():
        global Num,current,curr,btn21
        btn21['state'] = DISABLED
        dice=random.randint(1,6)
        z=0
        while(z<6):
            dtext=canvas2.create_text(900,580,text=str(random.randint(1,6)),font=('OCR A Extended',48),tag="dtext")
            canvas2.update()
            time.sleep(0.1)
            canvas2.delete(dtext)
            z+=1
        dtext=canvas2.create_text(900,580,text=dice,font=('OCR A Extended',48),fill='red',tag="dtext")
        canvas2.update()
        #print(current,dice)
        gameplay.move(current,dice)
        canvas2.update()
        time.sleep(1.0)
        canvas2.delete(dtext)
        if current<Num:
            current=current+1
        else:
            current=1
        canvas2.delete(curr)
        curr=canvas2.create_text(900,350,text=listname[current-1],font=('Consolas',20),tag="curr")
        btn21['state'] = NORMAL
    def playe():
        gameplay.play()
        gameplay.play()
    def winner(player):
        global r2,listname
        r3 = Tk()
        r3.geometry('600x400')
        r3.resizable(0,0)
        r3.title("We have a winner!")
        label1 = Label(r3, text='The winner is player', font=('Consolas',28))
        label1.pack(ipadx=40, ipady=30)
        label2 = Label(r3, text=listname[player-1], font=('Consolas',40))
        label2.pack(ipadx=40, ipady=30)
        btn31 = Button(r3,text="RESTART",compound = CENTER,command=lambda:[r2.destroy(),r3.destroy()])
        btn31.place(x=80,y=280,width=160,height=60)
        btn32 = Button(r3,text="EXIT",compound = CENTER,command=quit)
        btn32.place(x=360,y=280,width=160,height=60)
    def entname():
        global listname, Mode
        listname=[]
        prin1=pr1.get()
        listname.append(prin1)
        if Mode == 1:
            listname.append('Computer')
        if Mode >= 2:
            prin2=pr2.get()
            listname.append(prin2)
        if Mode >= 3:
            prin3=pr3.get()
            listname.append(prin3)
        if Mode >= 4:
            prin4=pr4.get()
            listname.append(prin4)
        r4.destroy()
#Main Programme 主程序
while res == 'y':
    #Play mode window 模式选择窗口
    Mode = 0
    r1=Tk()
    r1.title("S&L·Choose play mode")
    r1.resizable(0,0)
    canvas1 = Canvas(width=320, height=240, bg='white')
    canvas1.pack()
    canvas1.create_text(160,50,text="Choose play mode",font=('Consolas',20))
    btn11 = Button(r1,text="Single Player",compound = CENTER,command=onclick1)
    btn11.place(x=30,y=100,width=120,height=40)
    btn12 = Button(r1,text="Double Player",compound = CENTER,command=onclick2)
    btn12.place(x=180,y=100,width=120,height=40)
    btn13 = Button(r1,text="3 Players",compound = CENTER,command=onclick3)
    btn13.place(x=30,y=160,width=120,height=40)
    btn14 = Button(r1,text="4 Players",compound = CENTER,command=onclick4)
    btn14.place(x=180,y=160,width=120,height=40)
    r1.mainloop()
    if Mode < 1 or Mode > 4:
        break
    #Name Enter Window 名称输入窗口
    r4=Tk()
    r4.title("Enter player name")
    r4.resizable(0,0)
    canvas4 = Canvas(width=500, height=70)
    canvas4.pack()
    canvas4.create_text(250,50,text="Enter player name",font=('Consolas',20))
    pr1=Entry(r4,fg='red')
    pr1.insert(0, "Player 1")
    pr1.pack(ipadx=150,ipady=10,pady=10)
    if Mode >= 2:
        pr2=Entry(r4,fg='green')
        pr2.insert(0, "Player 2")
        pr2.pack(ipadx=150,ipady=10,pady=10)
    if Mode >= 3:
        pr3=Entry(r4,fg='orange')
        pr3.insert(0, "Player 3")
        pr3.pack(ipadx=150,ipady=10,pady=10)
    if Mode >= 4:
        pr4=Entry(r4,fg='blue')
        pr4.insert(0, "Player 4")
        pr4.pack(ipadx=150,ipady=10,pady=10)
    btn41 = Button(r4,text="Confirm",compound = CENTER,command=gameplay.entname)
    btn41.pack(ipadx=50,ipady=10,pady=10)
    r4.mainloop()
    print(listname)
    #Main Window 主窗口
    r2 = Tk()
    r2.title("Snakes and ladders")
    r2.resizable(0,0)
    canvas2 = Canvas(width=1000, height=800, bg='white')
    canvas2.pack()
    back = PhotoImage(file=path.image)
    canvas2.create_image(400, 400, image=back, tag="back")
    canvas2.create_rectangle(960,640,840,520,width=4)
    r = PhotoImage(file=path.imagr)
    g = PhotoImage(file=path.imagg)
    y = PhotoImage(file=path.imagy)
    b = PhotoImage(file=path.imagb)
    pr = canvas2.create_image(-40,760, image=r)
    pg = canvas2.create_image(-40,760, image=g)
    py = canvas2.create_image(-40,760, image=y)
    pb = canvas2.create_image(-40,760, image=b)
    canvas2.create_text(900,300,text="It's",font=('Consolas',20))
    canvas2.create_text(900,400,text="Turn",font=('Consolas',20))
    if Mode == 1:
        Num = 2
        ind = PhotoImage(file=path.imagind[0])
        canvas2.create_image(840,100, image=ind, tag='ind')
        canvas2.create_text(930,70,text=listname[0],font=('Consolas',16))
        canvas2.create_text(930,140,text="Computer",font=('Consolas',16))
        curr=canvas2.create_text(900,350,text=listname[current-1],font=('Consolas',20))
        btn22 = Button(r2,text="RESTART",compound = CENTER,command=lambda:[r2.destroy()])
        btn22.place(x=820,y=740,width=160,height=40)
        btn21 = Button(r2,text="Roll the dice",compound = CENTER,command=gameplay.playe)
        btn21.place(x=820,y=680,width=160,height=40)
    if Mode == 2:
        Num = 2
        ind = PhotoImage(file=path.imagind[0])
        canvas2.create_image(840,100, image=ind, tag='ind')
        canvas2.create_text(930,70,text=listname[0],font=('Consolas',16))
        canvas2.create_text(930,140,text=listname[1],font=('Consolas',16))
        curr=canvas2.create_text(900,350,text=listname[current-1],font=('Consolas',20))
        btn22 = Button(r2,text="RESTART",compound = CENTER,command=lambda:[r2.destroy()])
        btn22.place(x=820,y=740,width=160,height=40)
        btn21 = Button(r2,text="Roll the dice",compound = CENTER,command=gameplay.play)
        btn21.place(x=820,y=680,width=160,height=40)
    if Mode == 3:
        Num = 3
        ind = PhotoImage(file=path.imagind[1])
        canvas2.create_image(840,100, image=ind, tag='ind')
        canvas2.create_text(930,30,text=listname[0],font=('Consolas',16))
        canvas2.create_text(930,100,text=listname[1],font=('Consolas',16))
        canvas2.create_text(930,170,text=listname[2],font=('Consolas',16))
        curr=canvas2.create_text(900,350,text=listname[current-1],font=('Consolas',20))
        btn22 = Button(r2,text="RESTART",compound = CENTER,command=lambda:[r2.destroy()])
        btn22.place(x=820,y=740,width=160,height=40)
        btn21 = Button(r2,text="Roll the dice",compound = CENTER,command=gameplay.play)
        btn21.place(x=820,y=680,width=160,height=40)
    if Mode == 4:
        Num = 4
        ind = PhotoImage(file=path.imagind[2])
        canvas2.create_image(840,140, image=ind, tag='ind')
        canvas2.create_text(930,30,text=listname[0],font=('Consolas',16))
        canvas2.create_text(930,100,text=listname[1],font=('Consolas',16))
        canvas2.create_text(930,170,text=listname[2],font=('Consolas',16))
        canvas2.create_text(930,240,text=listname[3],font=('Consolas',16))
        curr=canvas2.create_text(900,350, text=listname[current-1],font=('Consolas',20))
        btn22 = Button(r2, text="RESTART", compound=CENTER, command=lambda:[r2.destroy()])
        btn22.place(x=820, y=740, width=160, height=40)
        btn21 = Button(r2, text="Roll the dice", compound=CENTER, command=gameplay.play)
        btn21.place(x=820, y=680, width=160, height=40)

    r2.mainloop()