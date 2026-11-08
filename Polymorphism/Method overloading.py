class Addition:
      ans=0
      def cal(self,a=0,b=0,c=0):
            self.ans=a+b+c
      def show(self):
            print("Ans:",self.ans) 

a1=Addition()
a1.cal(10)
a1.show()

a1=Addition()
a1.cal(10,12)
a1.show()

a1=Addition()
a1.cal(10,12,16)
a1.show()


                 