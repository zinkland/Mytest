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



class Test:
    def __init__(self):
        self.color='red'
        self.height=100
    def __getattribute__(self, name):
         
            self.color='blue'
            return super().__getattribute__(name)
       
a=Test()
print(a.__dict__)
print(a.color)
print(a.__dict__)
        
