#importing math library to use the math functions
import math

#creating class in order to use the python OOP method...
class Calculate_Armstrong(object):

    #creating power function first in order to evaluate...
   def power(self,base,exponent):
      res = 1
      #making a loop for continuation of exponent...
      while exponent:
         if exponent & 1:
            res *= base
         base *= base
         exponent>>=1
      return res

    #creating armstrong function for the final calculation of a number...
   def isArmstrong(self, n):
       #taking log of a number..
      exponent =int(math.log10(n)) + 1
      temp = n
      res = 0

      #making a loop to calculate mode...
      while temp:
         res += (self.power(temp%10,exponent))
         temp//=10 
      return res == n


#creating object of Calculate_Armstrong class...
obj = Calculate_Armstrong()
number = 1

#creating loop to provide user a facility to check multiple numbers...
while(number):
    #taking input from user...
    number = int(input("Enter number to check: "))


    #making decision on the basis of previous calculation...
    if(obj.isArmstrong(number)==True):
       output = "It is an armstrong number"
    else:
      output = "It is not an armstrong number"


    #printing result to the user...
    print(output)
    #printing a line to create a line space between two iterations...
    print(" ")