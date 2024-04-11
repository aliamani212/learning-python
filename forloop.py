#******************* afctorial**************
# n =int(input('enter the number:'))
# fac = 1
# for i in range(1,n+1):
#     fac *= i
# print(fac)


#******n**m*************************
# n1 =int(input('enter number 1:'))
# n2 =int(input('enter number 2:'))

# sum = 1
# for i in range(n2):
#     sum *= n1
# print(sum)


#**********series**********
# n =int(input('enter the number:'))

# sum = 0

# for i in range(1,n+1):
#     fac = 1
#     for j in range(1,n+2):
#         fac *= j
#     if i%2 == 1:
#         sum += i/fac
#     else:
#         sum -= i/fac
# print(sum)



#************sekeh*************
# daftar = 4
# ketab = 6
# medad = 8
# amount = 120

# for i in range(1,amount//(daftar)+1):
#     sum = i*daftar
    
#     if (sum) <= amount:
#         sum += daftar
#         for j in range(1,amount//(ketab)+1):
#             if (sum + ketab) <= amount:
#                 sum += ketab
            
#                 for k in range(1,amount//(medad)+1):
#                     if (sum + medad) <= amount:
#                         sum += medad
#                     else:
#                         if sum+daftar >= amount and sum+daftar >= amount and sum+daftar >= amount:
#                             print(f'amount = {amount}, daftar = {i}, ketab = {j}, medad = {k-1}')
#                             sum = i*daftar + j*ketab
#                             break
#                         else:
#                             sum = i*daftar + j*ketab
#                             break
#             else:
#                 if sum+daftar >= amount and sum+daftar >= amount and sum+daftar >= amount:
#                     print(f'amount = {amount}, daftar = {i}, ketab = {j-1}, medad = {k}')
#                     break
#                 else:
#                     break

#     else:
#         print(f'amount = {amount}, daftar = {i-1}, ketab = {j}, medad = {k}')
        
        
#******************************fibonachi***********************
# a = 1
# b = 1
# n = int(input('enter a number : '))
# print(f'{a},{b}',end=',')
# for i in range(n-2):
#     # c = b
#     # b = a+b
#     c,b = b , a+b
#     print(f',{b}',end='')
#     a = c
    
#اعداد متقارن
#ب.م.م و ک.م.م
#n امین عدد اول را چاپ کند
#145=1!+2!+3!
#7254 = 186 × 39
#برج هانوی
#مار و پله



# دیکشنری:
# مسله موبایل قدیمی و تفسیر پیام موبایل



# n = int(input('enter a number:'))
# while n!= 9:
#     n = int(input('enter a number:'))
#     print(n*'*')
# else:
#     print('wrong')


# list1 = [1,23,4,5]
# list1 += range(9,21,2)
# print(list1)




# tup = ()
# tup += (2,3,)
# print(tup)
# tup += (4,5)
# print(tup)
# tup += (2,3,[35,45])
# print(tup) 
# tup[6][0] = 25
# print(tup) 

# tup[6].append(75)
# print(tup) 
# print(tup.count(3))
# tup.index


# tup1 = ('ali',[8601193,3934565050])
# name , detail = tup1
# print(tup1)
# print(name)
# print(detail)


# num1 =100
# num2 = 200
# num1 , num2 = num2,num1
# print(f'num1:{num1}\nnum2:{num2}')


# list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(f'values is:{'index':>20}')
# print(f'values is:                    {'index'}')

# ***********************************************************
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# def func():
#     return list1


# tup = (func(),)
# print(tup)


# list2 = []
# list2.append(func())
# print(list2)


# list2 = func()
# print(list2)



# print(list2[0:5])
# print(list2.append(func())) // notice

# **************************************************************


# list1 = [1,2,3,4,5,6]
# list2 = ['two','three','five']
# list1[2:5] = 'two','three','five'
# print(list1)


# print:'ali'
input('enter:')