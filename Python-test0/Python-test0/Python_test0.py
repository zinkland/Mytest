#class Bird:
#    def __init__(self):
#        self.hungry =True
#    def eat(self):
#        if self.hungry :
#            print('Ahhhhh....')
#            self.hungry=False
#        else:
#            print('No')
#class SongBird(Bird):
#    def __init__(self):
#        super(SongBird,self).__init__()
#        self.sound='Squaaawk..'
#    def sing(self):
#        print(self.sound)
#Bird.eat()


#b=SongBird()#hungry方法在初始化时就被绑定
#b.sing()
#b.eat()
#b.eat()
#class footbar:
#    def __init__(self,value):
#        self.somevar=value


#类的方法绑定和魔法方法测试
#方法的参数测试
#方法的描述


#class Test:
#    def __init__(self):
        
#        self.color='red'
#        self.height=100
#    def __getattribute__(self, name):
         
#            self.color='blue'
#            return super().__getattribute__(name)
#    def __setattr__(self, name, value):
#        print(name)
#        return super().__setattr__(name, value)
#    def ChangeColor(self):
#        'change color'
#        self.color='blue'
#    def ChangeHeight(self):
#        self.height=100
#a=Test()
#print(a.ChangeColor.__doc__)
#a.ChangeColor()
#print(a.color)
#print(Test.__dict__)
#print(a.color)
#a.color='black'
#change.__doc__


        #yield使用

#def odd():
#    print('1')
#    yield
#    print('2')
#    yield
#    print('3')
#    yield
#a=odd()

#读取文件流（类似于C语言fopen）

#import fileinput        
#for line in fileinput.input(r'C:\Users\asus\source\repos\test1\test1\indata.txt'):
#    print(line)
#    print(fileinput.lineno())

#集合操作

#a=set([1,2,3])
#b=set([2,3,4])
#a|b


#字符串匹配

#re.search('r','aaaarbbit')
#    sre.SRE_Match object; span=(4, 5), match='r'>
#re.search('rb','aaaarbbit')
#    _sre.SRE_Match object; span=(4, 6), match='rb'>
#re.escape('www.baidu.com')

#文件读取

#import fileinput
#def process(string):
#    print('processing: ',string)

#for line in fileinput.input(r'C:\Users\asus\Desktop\test.txt'):
#    process(line)


#标准文件流

#import sys
#name=sys.stdin.readline()
#print('Hello',name)


import wx

app=wx.App()
win=wx.Frame(None)
win.Show()
app.MainLoop()
