import random
from tkinter import *

"""
frames:
1: for timer display
2: for problem statement display


"""

"""
IDEAS:
    add an actual test simulator with all the sections randomly assorted together (maybe 10 minutes for 80 questions)
    add a game mode for race: timer that counts down (say only ~10 seconds for each problem)
"""


# define classes and functions
##################################################
"""
global count
global total
global score
count=0
score=0
total=0

class App(object):
    def reset(self):
        global count
        count=1
        self.t.set("00:00:00")
    def start(self):
        global count
        count=0
        self.start_timer()
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1

    def timer(self):
        global count
        if count==0:
            self.d=str(self.t.get())
            h,m,s = map(int, self.d.split(":"))

            h=int(h)
            m=int(m)
            s= int(s)
            if s<59:
                s+=1
            elif s==59:
                s=0
                if m<59:
                    m+=1
                elif m==59:
                    h+=1
            if h<10:
                h= str(0) + str(h)
            else:
                h=str(h)
            if m<10:
                m=str(0)+str(m)
            else:
                m=str(m)
            if s<10:
                s=str(0) + str(s)
            else:
                s=str(s)
            self.d=h+":" +m+":"+s

            self.t.set(self.d)
            if count==0:
                self.master.after(930,self.start_timer)

    def __init__(self,master):
        self.t=StringVar()
        self.t.set("00:00:00")
        self.lb=Label(master,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))
        self.lb.pack(side=LEFT)

        self.bt1=Button(master, text="Start", command=self.start)
        self.bt2=Button(master, text="Stop", command=self.stop)
        self.bt3=Button(master, text="Reset", command=self.reset)

        self.bt1.pack()
        self.bt2.pack()
        self.bt3.pack()
        
"""

global score
global total
global counter
global running
global stopcounter
global resetflag
global currentfunc
global bgcolor


resetflag=True
stopcounter=0
counter = -1
running = False
total = 1
score = 0
bgcolor = '#34bdeb'

#hidden=1 means it is hidden

class App(object):

    def doNothing(self):
        print("this worked")
    def __init__(self, master):

        self.menu = Menu(master)
        master.config(menu=self.menu)

        self.a = StringVar()
        self.b = StringVar()
        self.ans = IntVar()
        self.p = StringVar()
        self.mode = StringVar()
        self.modetext = 'Please choose a skill from the sections above to begin.'
        self.mode.set('Current Mode: ' + self.modetext)

        #RANDOMS
        self.randMenu = Menu(self.menu)
        self.menu.add_cascade(label="Random", menu=self.randMenu)
        self.randMenu.add_command(label="Addition", command=self.randadd)
        self.randMenu.add_command(label="Subtraction", command=self.randsubtract)
        self.randMenu.add_command(label="2x2", command=self.rand2x2)
        self.randMenu.add_command(label="3x3", command=self.rand3x3)



        #MULTIPLICATION
        self.multMenu = Menu(self.menu)
        self.menu.add_cascade(label="Multiplication", menu=self.multMenu)
        #self.multMenu.add_separator()
        self.multMenu.add_command(label="11s", command=self.mult11)
        self.multMenu.add_command(label="25 and 75", command=self.mult25o75)
        self.multMenu.add_command(label="101s", command=self.mult101)
        self.multMenu.add_separator()
        self.multMenu.add_command(label="Near 100", command=self.near1002x2)
        self.multMenu.add_command(label="Reverse", command=self.multRev)
        self.multMenu.add_command(label="Ending with 5", command=self.multend5)

        self.increment = 0

        #MEMORIZATION
        self.memMenu = Menu(self.menu)
        self.menu.add_cascade(label="Memorization", menu=self.memMenu)
        self.memMenu.add_command(label="Squares", command=self.memSquares)
        self.memMenu.add_command(label="Cubes", command=self.memCubes)







        # self.subMenu.add_separator()
        # self.subMenu.add_command(label="Exit", command=self.doNothing())
        #
        # self.editMenu = Menu(self.menu)
        # self.menu.add_cascade(label="Fractions", menu=self.editMenu)
        # self.editMenu.add_command(label="[insert section here]", command=self.doNothing)


        self.hidden = 1
        self.frame = Frame(master, bg=bgcolor)
        self.frame.pack()

        self.label = Label(self.frame, text="Welcome to the \n Numberino Sensorino!", fg="black", font="Verdana 30 bold", pady=30, bg=bgcolor)
        self.label2 = Label(self.frame, textvariable = self.mode, fg="black",
                           font="Verdana 15", pady=20, padx=30, bg=bgcolor)
        self.label.grid()
        self.label2.grid()

        self.cred = Label(self.frame, text="by Jack Qiao", fg="black", font="Verdana 20 bold", pady=20, bg=bgcolor)

        self.start = Button(self.frame, text='Start',
                            width=15, command=lambda: self.Start(), state='disabled')
        self.stop = Button(self.frame, text='Stop',
                           width=15, state='disabled', command=self.Stop)
        self.reset = Button(self.frame, text='Reset',
                            width=15, state='disabled', command=lambda: self.Reset())
        self.start.grid()
        self.stop.grid()
        self.reset.grid()
        self.cred.grid()

    def counter_label(self):
        def count():
            if running:
                global counter

                # To manage the intial delay.
                if counter == -1:
                    self.display = "Starting..."
                else:
                    self.minutes = str(counter//60)
                    self.second = str(counter%60)
                    if int(self.second)<10:
                        self.second = "0" + self.second
                    if int(self.minutes)<10:
                        self.minutes = "0" + self.minutes
                    self.display = self.minutes+":"+ self.second

                self.label['text'] = self.display  # label.config(text=display)

                # label.after(arg1, arg2) delays by
                # first argument given in milliseconds
                # and then calls the function given as second argument.
                # Generally like here we need to call the
                # function in which it is present repeatedly.
                # Delays by 1000ms=1 seconds and call count again.
                self.label.after(1000, count)
                counter += 1

            # Triggering the start of the counter.

        count()
    # start function of the stopwatch
    def Start(self):
        global running
        global stopcounter
        global resetflag

        running = True

        self.counter_label()
        self.start.config(state='disabled')  # start['state'] = 'disabled' makes start button unclickable
        self.stop['state'] = 'normal'
        self.reset['state'] = 'disabled'
        self.cred.grid_forget()



        if self.hidden == 1 and running == True and stopcounter == 0:
            self.problem(root)
            self.hidden = 0


        if resetflag and self.hidden == 1:
            self.problem(root)
            self.hidden = 0
            resetflag = False

        self.start['state'] = 'disabled'

    # Stop function of the stopwatch
    def Stop(self):
        global running
        global stopcounter
        self.start['state'] = 'normal'
        self.stop['state'] = 'disabled'
        self.reset['state'] = 'normal'
        running = False
        stopcounter += 1
    # Reset function of the stopwatch
    def Reset(self):
        global counter
        global resetflag
        global total
        global score


        counter = -1
        total = 1
        score = 0
        self.increment = 0


        # If rest is pressed after pressing stop.
        self.reset['state'] = 'disabled'
        self.label['text'] = 'Welcome to the \n Numberino Sensorino!'
        self.cred.grid()

        #rid the problemframe

        self.frame1.destroy()
        self.hidden = 1
        resetflag = True

    def problem(self, master): #generates the random problem
        global total
        global currentfunc

        self.frame1=Frame(master, bg=bgcolor)
        self.frame1.pack()


        self.pnum = StringVar()
        self.pnum.set("Problem " + str(total))
        self.problemnum = Label(self.frame1, textvariable=self.pnum, font="Arial 25 bold", bg=bgcolor)

        self.scoreval = StringVar()
        self.scoreval.set(str(score) + " Points")
        self.scoreboard = Label(self.frame1, textvariable=self.scoreval, font="Arial 20", fg="purple", bg=bgcolor)


        currentfunc()
        #self.lb = Label(self.frame1, textvariable=self.p, borderwidth=2, relief="solid", padx=30,pady=30)
        self.lb = Label(self.frame1, textvariable=self.p, font="Arial 60", bg=bgcolor)
        self.lb.grid(pady=20)

        self.problemnum.grid()
        self.scoreboard.grid()

        self.input = Entry(self.frame1, width=20, bd=2, relief=SUNKEN)
        self.input.grid(pady=30)
        self.enter = Button(self.frame1, text="Enter", command=self.submitbutt, width=10)

        self.enter.grid(ipadx=30, ipady=10, pady=20)  # ipad changes size of button
        self.input.bind('<Return>', self.submitkey)

        self.correct = Label(self.frame1, text="Correct!", fg="green", font="Arial 40", bg=bgcolor)
        self.wrong = Label(self.frame1, text="Wrong!", fg="red", font="Arial 40", bg=bgcolor)
        self.plzenter = Label(self.frame1, text="Please enter an answer", fg="purple", font="Arial 40", bg=bgcolor)


########ALL THE SECTIONED METHODS###########

    def rand2x2(self):
        """
        function called for random 2 digit by 2 digit multiplication
        """
        global currentfunc
        currentfunc = self.rand2x2
        self.a = str(random.randrange(10, 100))
        self.b = str(random.randrange(10, 100))
        self.ans.set(int(self.a)*int(self.b))
        self.p.set(self.a + "*" + self.b + "=")
        self.modetext = 'Random 2x2'
        self.mode.set('Current Mode: ' + self.modetext)

        if not running:
            self.start['state'] = 'normal'

        print(self.ans.get(),self.p.get())

    def rand3x3(self):
        """
        function called for random 3 digit by 3 digit multiplication
        """
        global currentfunc
        currentfunc=self.rand3x3
        self.a = str(random.randrange(100, 1000))
        self.b = str(random.randrange(100, 1000))
        self.ans.set(int(self.a)*int(self.b))
        self.p.set(self.a + "*" + self.b + "=")
        self.modetext = 'Random 3x3'
        self.mode.set('Current Mode: ' + self.modetext)
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())

    def randsubtract(self):
        global currentfunc
        currentfunc=self.randsubtract
        self.a = str(random.randrange(1000,10000))
        self.b = str(random.randrange(int(self.a)+1,10000))
        self.ans.set(int(self.b) - int(self.a))
        self.p.set(self.b + "-" + self.a + "=")
        self.modetext = 'Random Subtraction'
        self.mode.set('Current Mode: ' + self.modetext)
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())

    def mult11(self):
        """
        multiply or divide by 11
        :return:
        """
        global currentfunc
        currentfunc=self.mult11

        self.b = str(11)
        self.isMult=random.randrange(0,2)

        if self.isMult==0:
            self.a = str(random.randrange(13, 1000))
            self.b = str(random.choice([11,111]))
            self.ans.set(int(self.b) * int(self.a))
            self.p.set(self.a + "*" + self.b + "=")
        else:
            self.a = str(random.randrange(143,11*1000+1,11))
            self.ans.set(int(self.a)//11)
            self.p.set(self.a + "/" + self.b + "=")
        self.modetext = '11s'
        self.mode.set('Current Mode: ' + self.modetext)
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())

    def near1002x2(self):
        global currentfunc
        currentfunc = self.near1002x2

        self.a = str(random.randrange(90,111))
        self.b = str(random.randrange(90, 111))
        self.ans.set(int(self.b) * int(self.a))
        self.p.set(self.a + "*" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Near 100'
        self.mode.set('Current Mode: ' + self.modetext)

    def randadd(self):
        global currentfunc
        currentfunc = self.randadd

        self.a = str(random.randrange(10000,100000//2))
        self.b = str(random.randrange(int(self.a),100000))
        self.ans.set(int(self.b) + int(self.a))
        self.p.set(self.a + "+" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Random Addition'
        self.mode.set('Current Mode: ' + self.modetext)

    def mult25o75(self):
        global currentfunc
        currentfunc = self.mult25o75
        self.a = str(random.choice([25,75]))
        self.b = str(random.randrange(12,1000))
        self.ans.set(int(self.b) * int(self.a))
        self.p.set(self.a + "*" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = '25 and 75'
        self.mode.set('Current Mode: ' + self.modetext)

    def mult101(self):
        global currentfunc
        currentfunc = self.mult101
        self.a = str(random.choice([101]))
        self.b = str(random.randrange(12,10000))
        self.ans.set(int(self.b) * int(self.a))
        self.p.set(self.a + "*" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = '101s'
        self.mode.set('Current Mode: ' + self.modetext)

    def multRev(self):
        global currentfunc
        currentfunc = self.multRev
        self.b = str(random.randrange(12,100))
        self.a = self.b[::-1]
        self.ans.set(int(self.b) * int(self.a))
        self.p.set(self.a + "*" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Reverse'
        self.mode.set('Current Mode: ' + self.modetext)

    def multend5(self):
        global currentfunc
        currentfunc = self.multend5
        self.b = str(random.randrange(35,96,10))
        self.a = str(random.randrange(35,96,10))
        self.ans.set(int(self.b) * int(self.a))
        self.p.set(self.a + "*" + self.b + "=")
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Ending with 5'
        self.mode.set('Current Mode: ' + self.modetext)

    def memSquares(self):
        global currentfunc
        currentfunc = self.memSquares

        self.a = str(self.increment)
        self.ans.set(int(self.a)**2)
        self.p.set(self.a + "*" + self.a + "=") #convert to ACTUALLY displaying self.a^2
        self.increment += 1
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Squares'
        self.mode.set('Current Mode: ' + self.modetext)

    def memCubes(self):
        global currentfunc
        currentfunc = self.memCubes
        self.a = str(self.increment)
        self.ans.set(int(self.a)**3)
        self.p.set(self.a + "*" + self.a + "*"+ self.a + "=") #convert to ACTUALLY displaying self.a^2
        self.increment += 1
        if not running:
            self.start['state'] = 'normal'
        print(self.ans.get(), self.p.get())
        self.modetext = 'Cubes'
        self.mode.set('Current Mode: ' + self.modetext)


########ALL THE SECTIONED METHODS###########

    def submitbutt(self):
        global score
        global total
        print(self.ans.get())

        if self.input.get() == '':
            print("Please enter an answer")
            self.plzenter.grid()
            self.plzenter.after(1000, self.hideself)

        elif int(self.input.get()) == int(self.ans.get()):
            score += 1
            total += 1
            print("Correct!")
            print(score)
            print(total)

            global currentfunc
            currentfunc()

            self.pnum.set("Problem " + str(total))

            self.scoreval.set(str(score) + " Points")

            self.correct.grid()
            self.correct.after(1000, self.hideself)
            self.input.delete(0, 'end')



        else:
            self.display = "Wrong!   " + str(self.ans.get())
            score -= 1
            self.scoreval.set(str(score) + " Points")
            self.wrong.grid()
            self.wrong.after(1000, self.hideself)

            print(score)
            print(total)
            self.input.delete(0, 'end')

    def submitkey(self, event):
        global score
        global total
        print(self.ans.get())

        if self.input.get() == '':
            print("Please enter an answer")
            self.plzenter.grid()
            self.plzenter.after(1000, self.hideself)

        elif int(self.input.get()) == int(self.ans.get()):
            score += 1
            total += 1
            print("Correct!")
            print(score)
            print(total)

            global currentfunc
            currentfunc()

            self.pnum.set("Problem " + str(total))
            self.scoreval.set(str(score) + " Points")

            self.correct.grid()
            self.correct.after(1000, self.hideself)
            self.input.delete(0, 'end')



        else:
            self.display = "Wrong!   " + str(self.ans.get())
            score -= 1
            self.scoreval.set(str(score) + " Points")
            self.wrong.grid()
            self.wrong.after(1000, self.hideself)

            print(score)
            print(total)
            self.input.delete(0, 'end')

    def hideself(self):
        self.correct.grid_remove()
        self.wrong.grid_remove()
        self.plzenter.grid_remove()


##################################################

root = Tk()
root.title("Number Sense")

"""
INTRO SCREEN CODE
#create widgets
introframe=Frame(root,width=500,height=500)
intro=Label(introframe, text="Welcome!")
intro.config(font=("Courier", 44))

#packing widgets
introframe.pack()
intro.pack()
"""


root.geometry("1000x500")
# timerframe = Frame(root)
# timerframe.pack(side=TOP)
# problemframe = Frame(root)
# problemframe.pack(side=TOP)

"""
def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the intial delay.
            if counter == -1:
                display = "Starting..."
            else:
                display = str(counter)

            label['text'] = display  # label.config(text=display)

            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()



# start function of the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start.config(state='disabled')  # start['state'] = 'disabled' makes start button unclickable
    stop['state'] = 'normal'
    reset['state'] = 'normal'

    Problem(problemframe)


# Stop function of the stopwatch
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False



# Reset function of the stopwatch
def Reset(label):
    global counter
    global score
    global total
    counter = -1
    score = 0
    total = 0


    # If rest is pressed after pressing stop.
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'
        #Problem(problemframe).reset()
        Problem(problemframe).reset()



label = Label(timerframe, text="Welcome!", fg="black", font="Verdana 30 bold")
label.grid(pady=40)
start = Button(timerframe, text='Start',
               width=15, command=lambda: Start(label))
stop = Button(timerframe, text='Stop',
              width=15, state='disabled', command=Stop)
reset = Button(timerframe, text='Reset',
               width=15, state='disabled', command=lambda: Reset(label))

start.grid()
stop.grid()
reset.grid()
"""

App(root)
root.configure(bg=bgcolor)



root.mainloop()
