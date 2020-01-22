class Reverse():
    def reverse(self):
        self.rev=0
        self.n=int(input("enter the value: "))
        while(self.n>0):
            self.d=self.n%10
            self.rev=(self.rev*10)+self.d 
            self.n=self.n//10
        print(self.rev)    
obj=Reverse()
obj.reverse()

''' sum of the digit'''
class Sum():
    def sum(self):
        self.sum=0
        self.n=int(input("enter the value: "))
        while(self.n>0):
            self.d=self.n%10
            self.sum=self.sum+self.d 
            self.n=self.n//10
        print(self.sum)    
obj=Sum()
obj.sum()
