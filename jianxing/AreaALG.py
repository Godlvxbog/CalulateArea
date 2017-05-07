# coding=utf-8
import math
from scipy import integrate
from scipy.optimize import fsolve as fs
import numpy as np
import matplotlib.pyplot as plt
###构造数据结构
class Circle:
     def __init__(self, X, Y, R):
         self.X = X
         self.Y = Y
         self.R = R
     def sayHello(self,i):
         print"圆 O{i} 方程：(x-{X})**2 + (y-{Y})**2 == {R}\n".format(i = i,X = self.X,Y =self.Y, R = self.R**2),
class Point:
    def __init__(self, X, Y):
         self.X = X
         self.Y = Y
    def sayHello(self,str):
        print "点 {name} 的坐标是：({X},{Y})".format(name = str, X =self.X ,Y = self.Y)
class Line:
     def __init__(self, K, B):
         self.K = K
         self.B = B

     def sayHello(self,i):
         print "直线方程 y{i}：y{i} = {K} * x + {B} \n".format(i = i,K = self.K,B =self.B),

################# 交互 #################

SUIWEI =float(raw_input("请输入水位的高度【数字】："))

POINT_A_X =float(raw_input("请输入POINT_A_X【数字】："))
POINT_A_Y =float(raw_input("请输入POINT_A_Y【数字】："))

POINT_P_X =float(raw_input("请输入POINT_P_X【数字】："))
POINT_P_Y =float(raw_input("请输入POINT_P_Y【数字】："))

POINT_B_X =float(raw_input("请输入POINT_B_X【数字】："))
POINT_B_Y =float(raw_input("请输入POINT_B_Y【数字】："))

POINT_C_X =float(raw_input("请输入POINT_C_X【数字】："))
POINT_C_Y =float(raw_input("请输入POINT_C_Y【数字】："))

R1 =float(raw_input("请输入R1【数字】："))
R2 =float(raw_input("请输入R2【数字】："))
R3 =float(raw_input("请输入R3【数字】："))
R4 =float(raw_input("请输入R4【数字】："))

################# 初始化 #################
POINT_A = Point(POINT_A_X,POINT_A_Y)
POINT_P = Point(POINT_P_X,POINT_P_Y)
POINT_B = Point(POINT_B_X,POINT_B_Y)
POINT_C = Point(POINT_C_X,POINT_C_Y)

# R1 = 2
# R2 = 15
# R3 = 3
# R4 = 3

CIRCLE_1 = Circle(0,3,R1)
CIRCLE_4 = Circle(21,43,R4)
# SUIWEI = 20
# R1 = 2


################# 切点M #################
def qiedian(m):
    x,y = m.tolist()
    return [(x - CIRCLE_1.X) * (POINT_C.X-CIRCLE_1.X) + (y - CIRCLE_1.Y) * (POINT_C.Y-CIRCLE_1.Y) - CIRCLE_1.R**2,
            (x - CIRCLE_1.X)**2 + (y-CIRCLE_1.Y)**2 - CIRCLE_1.R**2,]
POINT_M = fs(qiedian,[1,1])
POINT_M = Point(POINT_M[0],POINT_M[1])


################# 直线 LINE_1和LINE_2 #################
def lineBy2Point(point1,point2,i):
    K2 = (point2.Y-point1.Y)*1.0/(point2.X-point1.X)*1.0
    B2 = point2.Y-K2*point2.X;
    LINE = Line(K2,B2)
    LINE.sayHello(i)
    return LINE
LINE_1 = lineBy2Point(POINT_C,POINT_M,1)
LINE_2 = lineBy2Point(POINT_C,POINT_B,2)

################# 圆2和圆3 #################

def solve_circle_2(m,):
    Ox,Oy = m.tolist()
    return [LINE_1.K*Ox-Oy+LINE_1.B - R2*math.sqrt(LINE_1.K**2+1),
           LINE_2.K*Ox-Oy+LINE_2.B - R2*math.sqrt(LINE_2.K**2+1)
            ,]
R2_cicle = fs(solve_circle_2,[1,1],)
CIRCLE_2 = Circle(R2_cicle[0],R2_cicle[1],15)
CIRCLE_2.sayHello(2)

def solve_circle_3(m):
    Ox = float(m[0])
    Oy = float(m[1])
    return [LINE_2.K*Ox-Oy+LINE_2.B + R3*math.sqrt(LINE_2.K**2+1),
            Ox-21,]
R3_cicle = fs(solve_circle_3,[1,1])
CIRCLE_3 = Circle(R3_cicle[0],R3_cicle[1],3)
CIRCLE_3.sayHello(3)

################# 交点 #################
POINT_E = Point(0,3)
POINT_E.sayHello("E")
POINT_M.sayHello("M")

def line1ToCircle2(m):
    x,y = m.tolist()
    return [LINE_1.K * x + LINE_1.B -y,
            (x-CIRCLE_2.X)**2 + (y-CIRCLE_2.Y)**2 - CIRCLE_2.R**2,]
POINT_N = fs(line1ToCircle2,[1,1])
POINT_N = Point(POINT_N[0],POINT_N[1])
POINT_N.sayHello("N")


def line2ToCircle2(m):
    x,y = m.tolist()
    return [LINE_2.K * x + LINE_2.B -y,
            (x-CIRCLE_2.X)**2 + (y-CIRCLE_2.Y)**2 - CIRCLE_2.R**2,]
POINT_L = fs(line2ToCircle2,[1,1])
POINT_L = Point(POINT_L[0],POINT_L[1])
POINT_L.sayHello("L")

def line2ToCircle3(m):
    x,y = m.tolist()
    return [LINE_2.K * x + LINE_2.B -y,
            (x-CIRCLE_3.X)**2 + (y-CIRCLE_3.Y)**2 - CIRCLE_3.R**2,]
POINT_Y = fs(line2ToCircle3,[1,1])
POINT_Y = Point(POINT_Y[0],POINT_Y[1])
POINT_Y.sayHello("Y")

def line3ToCircle3(m):
    x,y = m.tolist()
    return [x -24,
            (x-CIRCLE_3.X)**2 + (y-CIRCLE_3.Y)**2 - CIRCLE_3.R**2,]
POINT_X = fs(line3ToCircle3,[1,1])
POINT_X = Point(POINT_X[0],POINT_X[1])
POINT_X.sayHello("X")

################# 临界面积 #################
print "\n现在开始求积分:"


# def area1():
#     s1,abser1 = integrate.dblquad(lambda x,y: 1,1,POINT_M.Y, lambda y : 0,lambda y : (CIRCLE_1.X + R1**2-(y-CIRCLE_1.Y)**2)**0.5,)
#     s2 = (POINT_N.X + POINT_M.X)*(POINT_N.Y - POINT_M.Y)/2
#     s3,abser3 = integrate.dblquad(lambda x,y: 1,POINT_N.Y,POINT_L.Y, lambda y : 0,lambda y : CIRCLE_2.X- (R2**2-(y-CIRCLE_2.Y)**2)**0.5,)
#     s4 = (POINT_Y.X + POINT_L.X)*(POINT_Y.Y - POINT_L.Y)/2
#     s5,abser5 = integrate.dblquad(lambda x,y: 1,POINT_Y.Y,POINT_X.Y, lambda y : 0,lambda y : CIRCLE_3.X + (R3**2-(y-CIRCLE_3.Y)**2)**0.5,)
#
#     print "S1的面积是： {s1}".format(s1 = s1)
#     print "S2的面积是： {s2}".format(s2 = s2)
#     print "S3的面积是： {s3}".format(s3 = s3)
#     print "S4的面积是： {s4}".format(s4 = s4)
#     print "S5的面积是： {s5}".format(s5 = s5)
#     return [
#         s1,s2,s3,s4,s5,
#     ]
# AREA =  area1()


################# 逻辑计算 #################
################# 逻辑计算 #################

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

print client(SUIWEI)

################# 逻辑计算 #################
################# 逻辑计算 #################



# x = np.arange(3,46,1)
# print type(x)
# y = np.ndarray(client(i) for i in x)
# print y
# # plt.plot(x, y, 'r--',)

################# 写入文件 #################
import pandas as pd
# x = np.arange(3,46,0.1)
# array_X = np.array(x)
# list_Y = list()
# for i in array_X:
#     y =  client(i)
#     list_Y.append(y)
# aa={'suiwei':array_X,'Area':list_Y,}
# df1 = pd.DataFrame(aa,columns=['suiwei','Area',])
# writer = pd.ExcelWriter('output.xlsx')
# df1.to_excel(writer,'Sheet1')
# writer.save()
################# 画图 #################

FILE = pd.read_excel("output.xlsx")
# print np.array(FILE["suiwei"])

plt.plot(FILE["suiwei"],FILE["Area"])

plt.show()






