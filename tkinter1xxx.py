from tkinter import *
import random
import time
#from box import *
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)
    #def __neg__(self):
        #return Point(-self.x, -self.y)
    def __mul__(self, other):
        if isinstance(other, float):
            return Point(self.x * other, self.y * other)
        elif isinstance(other, point):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return point(self.x / other, self.y / other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2)        
class ball:
    def __init__(self, x, y, r, vx, vy):
        self.dx=0
        self.dy=0
        self.c=point(x, y)
        self.v=point(vx, vy)
        self.r = r
        self.m = r
    def draw(self, app):
        x=self.c.x
        y=self.c.y
        r=self.r
        app.box.canvas.create_oval(x-r, y+r, x+r, y-r, fill='lightgrey')
    def erase(self,app):
        x=self.c.x
        y=self.c.y
        r=self.r
        app.box.canvas.create_oval(x-r, y+r, x+r, y-r, fill='white', outline="white")

class box:
    def __init__(self, par):
        self.canvas = Canvas(par, width=400, height=400, bg='white')
class but:
    def less (self, event):
        if self.count>1 and self.active == 1:
            self.count-=1
            self.descr['text'] = self.txt + str(self.count)
    def more (self, event):
        if (self.max>self.count or self.formpar.nolimon == 1) and self.active == 1:
            self.count+=1
            self.descr['text'] = self.txt + str(self.count)
    def setmax (self, event):
        if self.formpar.nolimon == 0 and self.active == 1:
            self.count=self.max
            self.descr['text'] = self.txt + str(self.max)
    def setmin (self, event):
        if self.active == 1:
            self.count=1
            self.descr['text'] = self.txt + str(1)
    def __init__(self, par, txt, clr, max, formpar):
        self.active = 1
        self.formpar=formpar
        self.txt = txt
        self.max = max
        self.count = 1
        self.bframe = Frame(par)
        self.udframe = Frame(self.bframe)
        self.descr = Label(self.bframe, bg=clr, text=txt + str(1), width=21, height=2)
        
        self.up = Button(self.udframe, text="↑")
        self.up.bind('<Button-1>', self.more)
        self.down = Button(self.udframe, text="↓")
        self.down.bind('<Button-1>', self.less)
        self.m = Button(self.bframe, text="max", bg="orange red", fg="white")
        self.m.bind('<Button-1>', self.setmax)
        self.min = Button(self.bframe, text="min", bg="lime green", fg="white")
        self.min.bind('<Button-1>', self.setmin)
        
        self.descr.pack(side=LEFT, padx=5)
        
        self.up.pack()
        self.down.pack()
        self.min.pack(side=RIGHT)
        self.m.pack(side=RIGHT, padx=5)
        self.udframe.pack(side=RIGHT)
        
        

class form:
    def __init__(self, _par, root):
        self.extraon = 0
        self.nolimon = 0
        
        self.par = _par
        self.frame = Frame(root, width=400, height=400)

        self.exframe = Frame(self.frame)
        self.exframe.pack()
        self.extra = Button(self.exframe, text="Dev", bg="black", fg="white")
        self.extra.bind('<Button-1>', self.devmode)
        self.extra.pack(side=RIGHT, padx=5)
        
        self.but1 = but (self.frame, "Количество шаров: ", "red", 16, self)
        self.but1.bframe.pack(pady=10, padx=5)
        self.but2 = but (self.frame, "Начальная скорость: ", "yellow", 10, self)
        self.but2.bframe.pack(pady=10)
        self.but3 = but (self.frame, "Радиус: ", "green2", 5, self)
        self.but3.bframe.pack(pady=10)
        self.start = Button(self.frame, text="Старт", bg="light green")
        self.start.bind('<Button-1>', self.par.prep)
        self.start.pack(pady=10)
    def devmode (self, event):
        if self.extraon == 0:
            self.energy = Button(self.exframe, text="Show energy", bg="white", fg="black")
            self.energy.bind('<Button-1>', self.showenergy)
            self.energy.pack(side=LEFT, padx=5)
            self.nolim = Button(self.exframe, text="No limits", bg="white", fg="black")
            self.nolim.bind('<Button-1>', self.nolimits)
            self.nolim.pack(side=LEFT)
            self.extraon = 1
        else:
            self.energy.destroy()
            self.nolim.destroy()
            self.extraon = 0
    def nolimits (self, event):
        if self.nolimon == 0 and self.par.started == 0:
            self.but1.m['state'] = DISABLED
            self.but2.m['state'] = DISABLED
            self.but3.m['state'] = DISABLED
            self.nolim['fg'] = "red"
            self.nolim['bg'] = "black"
            self.nolimon = 1
        else:
            if self.par.started == 0:
                self.but1.m['state'] = NORMAL
                self.but2.m['state'] = NORMAL
                self.but3.m['state'] = NORMAL
                self.nolimon = 0
                if self.but1.count > self.but1.max:
                    self.but1.count = self.but1.max
                    self.but1.descr['text'] = self.but1.txt + str(self.but1.count)
                if self.but2.count > self.but1.max:
                    self.but2.count = self.but1.max
                    self.but2.descr['text'] = self.but2.txt + str(self.but2.count)
                if self.but3.count > self.but1.max:
                    self.but3.count = self.but1.max
                    self.but3.descr['text'] = self.but3.txt + str(self.but3.count)
                self.nolim['fg'] = "black"
                self.nolim['bg'] = "white"
    def showenergy (self, event):
        if self.par.show == 0:
            self.par.show = 1
            self.par.enform.descr1 = Label(self.par.enform)
            self.par.enform.descr2 = Label(self.par.enform)
            self.par.enform.descr3 = Label(self.par.enform)
            self.par.enform.descr1.pack(side=LEFT)
            self.par.enform.descr2.pack(side=LEFT)
            self.par.enform.descr3.pack(side=LEFT)
            self.energy['fg'] = "red"
            self.energy['bg'] = "black"
            self.par.root.geometry('815x400')
        else:
            self.energy['fg'] = "black"
            self.energy['bg'] = "white"
            self.par.enform.descr1.destroy()
            self.par.enform.descr2.destroy()
            self.par.enform.descr3.destroy()
            self.par.show = 0
            self.par.root.geometry('670x400')
        
        

class app:
    def __init__(self):
        self.started = 0
        self.en = 0
        self.show = 0
        self.root = Tk()
        self.root.geometry('670x400')
        self.form = form(self, self.root)
        #self.form.frame.pack(side=RIGHT)
        self.form.frame.place(x=400, y=75)
        self.box = box(self.root)
        self.box.canvas.pack(side=LEFT)
        self.enform = Frame(self.root)
        self.enform.place(x=410, y=40)
        self.cc=0

    def run(self):
        self.root.mainloop()
    def prep(self, event):
        if self.started == 1:
            return 0
        self.started = 1
        self.form.but1.active = 0
        self.form.but2.active = 0
        self.form.but3.active = 0
        self.box.canvas.delete("all")
        balls = []
        q=0
        while q < self.form.but1.count:
            rr = 5*random.randint(1, self.form.but3.count)
            balls.append ( ball(random.randint(5+rr,395-rr), random.randint(5+rr,395-rr), rr, random.randint(1, self.form.but2.count), random.randint(1, self.form.but2.count)))
            x1=balls[q].c.x
            y1=balls[q].c.y
            r1=balls[q].r
            key=0
            for g in range(q):
                x2=balls[g].c.x
                y2=balls[g].c.y
                r2=balls[g].r
                if (x1-x2)**2+(y1-y2)**2<=(r1+r2)**2+75 and key==0:
                    balls.pop()
                    key=1
            if key == 0:
                q+=1
        for i in range(self.form.but1.count):
            x=balls[i].c.x
            y=balls[i].c.y
            r=balls[i].r
            balls[i].obj=self.box.canvas.create_oval(x-r, y+r, x+r, y-r, fill='lightgrey')
        self.box.canvas.update()
        print("PREP")
        self.balls=balls
        self.main()
        for i in range(self.form.but1.count):
            self.en+=abs(self.balls[i].v) * self.balls[i].m

            
    def main(self):
        balls=self.balls
        
        for i in range(self.form.but1.count):
            for g in range(self.form.but1.count):
                if i!=g and abs(balls[i].c-balls[g].c)>=abs((balls[i].c+balls[i].v)-(balls[g].c+balls[g].v)):
                    if ((balls[i].c.x-balls[g].c.x)**2 + (balls[i].c.y-balls[g].c.y)**2) <= (balls[i].r+balls[g].r)**2:
                        print("COLLIDE")
                        v1=balls[i].v
                        v2=balls[g].v
                        m1=balls[i].m
                        m2=balls[g].m
                        c1=balls[i].c
                        c2=balls[g].c
                        u1=v1-2*m2/(m1+m2)*((v1-v2)*(c1-c2))/abs(c1-c2)*(c1-c2)
                        u2=v2-2*m1/(m1+m2)*((v2-v1)*(c2-c1))/abs(c2-c1)*(c2-c1)
                        
                        balls[i].v=u1
                        balls[g].v=u2
                        
                        
        for i in range(self.form.but1.count):
            
            if (balls[i].c.y+balls[i].r>=395) and (balls[i].v.y>0):
                balls[i].v.y=-balls[i].v.y
                
            if (balls[i].c.y-balls[i].r<=5) and (balls[i].v.y<0):
                balls[i].v.y=-balls[i].v.y
                
            if (balls[i].c.x+balls[i].r>=395) and (balls[i].v.x>0):
                balls[i].v.x=-balls[i].v.x
                
            if (balls[i].c.x-balls[i].r<=5) and (balls[i].v.x<0):
                balls[i].v.x=-balls[i].v.x
                
        for i in range(self.form.but1.count):
            balls[i].dx+=balls[i].v.x
            balls[i].dy+=balls[i].v.y
            if abs(balls[i].dx)>=1:
                self.box.canvas.move(balls[i].obj, balls[i].dx//1, 0)
                balls[i].c.x+=balls[i].dx//1
                balls[i].dx=balls[i].dx%1
                
            if abs(balls[i].dy)>=1:
                self.box.canvas.move(balls[i].obj, 0, balls[i].dy//1)
                balls[i].c.y+=balls[i].dy//1
                balls[i].dy=balls[i].dy%1
        self.balls=balls
        self.box.canvas.update()

        
        self.cc+=1
        print(self.cc)
        if self.show == 1:
            curr = 0
            for i in range(self.form.but1.count):
                curr+=abs(self.balls[i].v) * self.balls[i].m
            if curr>=self.en:
                sign = "+"
                self.enform.descr2['fg'] = "light green"
            else:
                sign = "-"
                self.enform.descr2['fg'] = "red"
            self.enform.descr1['text'] = "Кинетическая энергия: " + str(curr) + " ("
            self.enform.descr2['text'] = sign + " " + str(abs(self.en-curr))
            self.enform.descr3['text'] = ")"
            
        self.box.canvas.after(10, self.main)
                
        

a=app()
a.run()
    


