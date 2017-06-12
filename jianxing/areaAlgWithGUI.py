#coding:utf-8

import math
from scipy import integrate
from scipy.optimize import fsolve as fs
import numpy as np
import matplotlib.pyplot as plt

from Tkinter import *
from contract import Point
from contract import Circle
from contract import Line

# 下面是测试数据
# R1 = 2
# R2 = 15
# R3 = 3
# R4 = 3
#
# POINT_A = Point(24,46)
# POINT_P = Point(24,43)
# POINT_B = Point(24,27)
# POINT_C = Point(5.6,21)
#
#
# CIRCLE_1 = Circle(0,3,R1)
# CIRCLE_4 = Circle(21,43,R4)








################# 客户端容器 #################
root = Tk()

frame1 = Frame(root)
frame1.pack()
frame = Frame(root)
frame.pack()

################# 按钮事件 #################

def qiedian(m):
    x = float(m[0])
    y = float(m[1])
    list_1 = [(x - CIRCLE_1.X) * (POINT_C.X - CIRCLE_1.X) + (y - CIRCLE_1.Y) * (POINT_C.Y - CIRCLE_1.Y) - CIRCLE_1.R ** 2,
            (x - CIRCLE_1.X) ** 2 + (y - CIRCLE_1.Y) ** 2 - CIRCLE_1.R ** 2, ]
    return list_1


def calcu():
##########初始化坐标##########
    global R1
    R1 = float(e_CIRCLE_1.get())
    global R2
    R2 = float(e_CIRCLE_2.get())
    global R3
    R3 = float(e_CIRCLE_3.get())
    global R4
    R4 = float(e_CIRCLE_4.get())

    global CIRCLE_1
    CIRCLE_1 = Circle(0, 3, R1)
    global CIRCLE_4
    CIRCLE_4 = Circle(21, 43, R4)

    global POINT_A
    global POINT_P
    global POINT_B
    global POINT_C
    POINT_A = Point(float(e_POINT_A_X.get()), float(e_POINT_A_Y.get()))
    POINT_P = Point(float(e_POINT_P_X.get()), float(e_POINT_P_Y.get()))
    POINT_B = Point(float(e_POINT_B_X.get()), float(e_POINT_B_Y.get()))
    POINT_C = Point(float(e_POINT_C_X.get()), float(e_POINT_C_Y.get()))


##########得到M点的坐标##########
    global POINT_M
    POINT_M = fs(qiedian, [1, 1])
    POINT_M = Point(POINT_M[0], POINT_M[1])
##########求LINE1和LINE2##########
    global LINE_1 ## 全局变量必须设置在方法体内部
    LINE_1 = lineBy2Point(POINT_M,POINT_C,1)
    LINE_1.sayHello(1)

    global LINE_2
    LINE_2 = lineBy2Point(POINT_C,POINT_B,2)
    LINE_2.sayHello(2)
##########求CIRCLE2和CIRCLE3##########
    R2_cicle = fs(solve_circle_2,[1,1],)
    global CIRCLE_2
    CIRCLE_2 = Circle(R2_cicle[0],R2_cicle[1],15)
    CIRCLE_2.sayHello(2)

    R3_cicle = fs(solve_circle_3,[1,1])
    global CIRCLE_3
    CIRCLE_3 = Circle(R3_cicle[0],R3_cicle[1],3)
    CIRCLE_3.sayHello(3)
################# 交点 #################
    global POINT_E
    POINT_E = Point(0,3)
    POINT_E.sayHello("E")
    POINT_M.sayHello("M")

    global POINT_N
    POINT_N = fs(line1ToCircle2,[1,1])
    POINT_N = Point(POINT_N[0],POINT_N[1])
    POINT_N.sayHello("N")

    global POINT_L
    POINT_L = fs(line2ToCircle2,[1,1])
    POINT_L = Point(POINT_L[0],POINT_L[1])
    POINT_L.sayHello("L")

    global POINT_Y
    POINT_Y = fs(line2ToCircle3,[1,1])
    POINT_Y = Point(POINT_Y[0],POINT_Y[1])
    POINT_Y.sayHello("Y")

    global POINT_X
    POINT_X = fs(line3ToCircle3,[1,1])
    POINT_X = Point(POINT_X[0],POINT_X[1])
    POINT_X.sayHello("X")

################# 临界面积 #################
    print "\n现在开始求积分:"
    SUIWEI = e_suiwei.get()
    area =  client(float(SUIWEI))


    lable1 = Label(root, text="面积是：" + str(float(area)))
    lable1.pack()



def client(level):
    if(level <= POINT_E.Y-CIRCLE_1.R or level >POINT_A.Y):
        return "输入的水位线异常，请重新输入！"
    elif(POINT_E.Y-CIRCLE_1.R < level <= POINT_M.Y):
        x = CIRCLE_1.X + (R1**2-(level-CIRCLE_1.Y)**2)**0.5
        JIAODIAN = Point(x,level)
        #求积分
        s1,abser = integrate.dblquad(lambda x,y: 1,POINT_E.Y-CIRCLE_1.R,JIAODIAN.Y, lambda y : 0,lambda y : (CIRCLE_1.X + R1**2-(y-CIRCLE_1.Y)**2)**0.5,)
        return s1
    elif(POINT_M.Y < level <= POINT_N.Y):
        x = (level - LINE_1.B)/LINE_1.K
        JIAODIAN = Point(x,level)
        s2 = (JIAODIAN.X + POINT_M.X)*(JIAODIAN.Y - POINT_M.Y)/2
        return client(POINT_M.Y) +s2
    elif(POINT_N.Y < level <= POINT_L.Y):
        x = CIRCLE_2.X- (R2**2-(level-CIRCLE_2.Y)**2)**0.5
        JIAODIAN = Point(x,level)
        s3,abser = integrate.dblquad(lambda x,y: 1,POINT_N.Y,JIAODIAN.Y, lambda y : 0,lambda y : CIRCLE_2.X- (R2**2-(y-CIRCLE_2.Y)**2)**0.5,)
        return client(POINT_N.Y) +s3
    elif(POINT_L.Y < level <= POINT_Y.Y):
        x = (level - LINE_2.B)/LINE_2.K
        JIAODIAN = Point(x,level)
        s4 = (JIAODIAN.X + POINT_L.X)*(JIAODIAN.Y - POINT_L.Y)/2
        return client(POINT_L.Y) +s4
    elif(POINT_Y.Y < level <= POINT_X.Y):
        x = CIRCLE_3.X + (R3**2-(level-CIRCLE_3.Y)**2)**0.5
        JIAODIAN = Point(x,level)
        # print JIAODIAN.X
        s5,abser = integrate.dblquad(lambda x,y: 1,POINT_Y.Y,JIAODIAN.Y, lambda y : 0,lambda y : CIRCLE_3.X + (R3**2-(y-CIRCLE_3.Y)**2)**0.5,)
        return client(POINT_Y.Y) + s5
    elif(POINT_X.Y < level <= POINT_P.Y):
        x =  POINT_P.X
        JIAODIAN = Point(x,level)
        s6 = (JIAODIAN.X + POINT_X.X)*(JIAODIAN.Y - POINT_X.Y)/2
        return client(POINT_X.Y) +s6

    elif(POINT_P.Y < level <= POINT_A.Y):
        x = CIRCLE_4.X + (R4**2-(level-CIRCLE_4.Y)**2)**0.5
        JIAODIAN = Point(x,level)
        # print JIAODIAN.X
        s7,abser = integrate.dblquad(lambda x,y: 1,POINT_P.Y,JIAODIAN.Y, lambda y : 0,lambda y : CIRCLE_4.X + (R4**2-(y-CIRCLE_4.Y)**2)**0.5,)
        return client(POINT_P.Y) + s7


def line2ToCircle3(m):
    x,y = m.tolist()
    return [LINE_2.K * x + LINE_2.B -y,
            (x-CIRCLE_3.X)**2 + (y-CIRCLE_3.Y)**2 - CIRCLE_3.R**2,]


def line3ToCircle3(m):
    x,y = m.tolist()
    return [x -24,
            (x-CIRCLE_3.X)**2 + (y-CIRCLE_3.Y)**2 - CIRCLE_3.R**2,]


def line2ToCircle2(m):
    x,y = m.tolist()
    return [LINE_2.K * x + LINE_2.B -y,
            (x-CIRCLE_2.X)**2 + (y-CIRCLE_2.Y)**2 - CIRCLE_2.R**2,]


def line1ToCircle2(m):
    x,y = m.tolist()
    return [LINE_1.K * x + LINE_1.B -y,
            (x-CIRCLE_2.X)**2 + (y-CIRCLE_2.Y)**2 - CIRCLE_2.R**2,]

################# 圆2和圆3 #################

def solve_circle_2(m,):
    Ox = float(m[0])
    Oy = float(m[1])
    return [LINE_1.K*Ox-Oy+LINE_1.B - R2*math.sqrt(LINE_1.K**2+1),
           LINE_2.K*Ox-Oy+LINE_2.B - R2*math.sqrt(LINE_2.K**2+1)
            ,]

def solve_circle_3(m):
    Ox = float(m[0])
    Oy = float(m[1])
    return [LINE_2.K*Ox-Oy+LINE_2.B + R3*math.sqrt(LINE_2.K**2+1),
            Ox-21,]

Button(frame, text="计算水流量体积", command=calcu, ).grid(row=10, column=0)

################# gui #################
w_suiwei = Label(frame1, text="请输入水位的高度【数字】：") #标签
w_suiwei.pack()
e_suiwei = Entry(frame1) #输入框
e_suiwei.pack(padx=100, pady=2)


w_POINT_A_X = Label(frame1, text="请输入POINT_A_X【数字】：") #标签
w_POINT_A_X.pack()
e_POINT_A_X = Entry(frame1) #输入框
e_POINT_A_X.pack(padx=100, pady=2)
w_POINT_A_Y = Label(frame1, text="请输入POINT_A_Y【数字】：") #标签
w_POINT_A_Y.pack()
e_POINT_A_Y = Entry(frame1) #输入框
e_POINT_A_Y.pack(padx=100, pady=2)

w_POINT_P_X = Label(frame1, text="请输入POINT_P_X【数字】：") #标签
w_POINT_P_X.pack()
e_POINT_P_X = Entry(frame1) #输入框
e_POINT_P_X.pack(padx=100, pady=2)
w_POINT_P_Y = Label(frame1, text="请输入POINT_P_Y【数字】：") #标签
w_POINT_P_Y.pack()
e_POINT_P_Y = Entry(frame1) #输入框
e_POINT_P_Y.pack(padx=100, pady=2)

w_POINT_B_X = Label(frame1, text="请输入POINT_B_X【数字】：") #标签
w_POINT_B_X.pack()
e_POINT_B_X = Entry(frame1) #输入框
e_POINT_B_X.pack(padx=100, pady=2)
w_POINT_B_Y = Label(frame1, text="请输入POINT_B_Y【数字】：") #标签
w_POINT_B_Y.pack()
e_POINT_B_Y = Entry(frame1) #输入框
e_POINT_B_Y.pack(padx=100, pady=2)


w_POINT_C_X = Label(frame1, text="请输入POINT_C_X【数字】：") #标签
w_POINT_C_X.pack()
e_POINT_C_X = Entry(frame1) #输入框
e_POINT_C_X.pack(padx=100, pady=2)
w_POINT_C_Y = Label(frame1, text="请输入POINT_C_Y【数字】：") #标签
w_POINT_C_Y.pack()
e_POINT_C_Y = Entry(frame1) #输入框
e_POINT_C_Y.pack(padx=100, pady=2)


w_CIRCLE_1 = Label(frame1, text="请输入R1【数字】：") #标签
w_CIRCLE_1.pack()
e_CIRCLE_1 = Entry(frame1) #输入框
e_CIRCLE_1.pack(padx=100, pady=2)
w_CIRCLE_2 = Label(frame1, text="请输入R2【数字】：") #标签
w_CIRCLE_2.pack()
e_CIRCLE_2 = Entry(frame1) #输入框
e_CIRCLE_2.pack(padx=100, pady=2)
w_CIRCLE_3 = Label(frame1, text="请输入R3【数字】：") #标签
w_CIRCLE_3.pack()
e_CIRCLE_3 = Entry(frame1) #输入框
e_CIRCLE_3.pack(padx=100, pady=2)
w_CIRCLE_4 = Label(frame1, text="请输入R4【数字】：") #标签
w_CIRCLE_4.pack()
e_CIRCLE_4 = Entry(frame1) #输入框
e_CIRCLE_4.pack(padx=100, pady=2)

################# 直线 LINE_1和LINE_2 #################
def lineBy2Point(point1,point2,i):
    K2 = (point2.Y-point1.Y)*1.0/(point2.X-point1.X)*1.0
    B2 = point2.Y-K2*point2.X;
    LINE = Line(K2,B2)
    return LINE

root.mainloop()