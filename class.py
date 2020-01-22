Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@pavikabilan 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


pavikabilan
/
pavi
0
00
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights Settings
pavi/AAPYTHON task.py / 
@pavikabilan pavikabilan Update AAPYTHON task.py
bbd1de8 15 days ago
82 lines (61 sloc)  1.69 KB
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

You're using code navigation to jump to definitions or references.
Learn more or give us feedback
# prime numbers


class Prime:
    def prime_num(self):
        self.n=int(input("enter the number:"))
        self.a=[]
        self.b=[]
        for self.i in range(self.n):
            self.a.append(self.i)
        print(self.a , end = " " )
        for self.j in self.a:
            if self.j>1:
                for self.k in (2,self.n):
                    if (self.j % self.k) == 0:
                        break
                else:
                    self.b.append(self.j)
        print(" \n prime numbers are:" ,self.b)
    
                
obj=Prime()
obj.prime_num()


#evenodd

class EvenOdd:
    def even_odd(self):
        self.n=int(input("enter the value of 'n': "))
        evenlist=[]
        oddlist=[]
        self.a=[]
        for self.i in range (self.n):
            self.a.append(self.i)
        print(self.a)
        for self.b in self.a:
            if self.b % 2 == 0:
                evenlist.append(self.b)
                
                
                
 # reverse list
def reverse():
    n=int(input("enter the value:"))
    a=[]
    revlist=[]
    for i in range (11,n+1):
        rev=0
        a.append(i)
        while i!=0:
            d =i % 10
            rev = (rev * 10) + d
            i = i // 10
        revlist.append(rev)
    print(" \n the list is: ",a , end = " ")
    print(" \n the reverse list is: ",revlist,end = "  ")
    
reverse() 





'''a=int(input("enter the number:"))
d=0
while a>0:
    rev=a%10
    d=(d*10)+rev
    a=a//10
print(d)'''


                
            else:
                 oddlist.append(self.b)
        print(" \n even list is", evenlist, end=" ")        
        print(" \n odd list is" , oddlist, end=" ")
obj=EvenOdd()
obj.even_odd()

        

