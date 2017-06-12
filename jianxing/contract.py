
#coding:utf-8
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
