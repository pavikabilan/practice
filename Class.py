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
