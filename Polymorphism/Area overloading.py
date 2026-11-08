class Area:
    ans=0
    def cal(self,x=0,y=0):
        if x==0 and y==0:
            ans=0
        elif x!=0 and y==0:
            ans=3.14*x*x
        else:
            ans=x*y
    def show(self):
        print(f"Area={self.ans}")

a1=Area()
a1.cal()
a1.show()


a1=Area()
a1.cal(14)
a1.show()
a1=Area()
a1.cal(15)
a1.show()
a1=Area()
a1.cal(12,16)
a1.show()
