 
# # def func1(n):
# #     li = [x**2 for x in range(1,n+1)if x%2==1]
# #     print(li)
# #     return sum(li)


# # print(func1(5))


# def fibonoci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonoci(n-1) + fibonoci(n-2)
    
    

# print(fibonoci(5))


# def power(x,n):
   
#    if n == 0:
#        return 1
#    else:
     
#      return x * power(x,n-1)
   

# print(power(5,3))



def addnum(j):

    sum1  = j 
    if j == 0:
        return sum1
    else:
       
        sum1 += addnum(j-1)
       
        return sum1
    
       




print( addnum(4))



def countnum(number):
    
    if number == 0:
        print (0)
    else:
        print(number)
        number = number-1
        countnum(number) 
        
        
x =countnum(10)



def fibonaci(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
    


print(fibonaci(4))



def mul(somenumber):
    if somenumber  == 0 or somenumber == 1:
        return 1
    else:
        return somenumber * mul(somenumber-1)    
       

def x2(number1):
    sum = number1
    
    for i in range(number1-1):
        sum *= number1-1 
        number1 =number1 -1
    return sum
    




# x =mul(3)
# print(x)
x = x2(4)
print(x)



def sumofnumbers(num):
    if num == 0:
        return 0
    else:
        num = num % 10 + sumofnumbers(num // 10)
        return num         





z = sumofnumbers(12)
print(z)


def polindrom(number):

        if number[0]!= number[-1]:
            return False
        
        elif len(number) ==1:
            return True
        
        elif polindrom(number[:len(number)//2]) == bool(number[len(number)-1:len(number)//2:-1]==number[:len(number)//2]):
            return True
        else:
            return False
            



x =polindrom("12321")

print(x)
    


