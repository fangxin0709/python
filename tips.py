####################################################欄寬對齊
# a = float(input()) 無float預設字串
# b = float(input())
# c = float(input())
# d = float(input())
#向右靠齊
# print(f"|{a:>7.2f} {b:>7.2f}|")
# print(f"|{c:>7.2f} {d:>7.2f}|")
#向左靠齊
# print(f"|{a:<7.2f} {b:<7.2f}|")
# print(f"|{c:<7.2f} {d:<7.2f}|")
####################################################二維陣列
# type int2D = list[list[int]]
# a:int2D =[[1 for _ in range(2)]for _ in range(3)]
# print(a)

# a = [[0 for _ in range(3)] for _ in range(4)] 輸入值在判定型態

# a:list[list[int]]=[[9 for _ in range(2)] for _ in range(3)] 
# print(a)
##################################################print預設空格處理
# print("ab","ac",sep="") sep是空格裡填入的東西
##################################################取陣列值
# a = [1]*5
# for num,item in enumerate(a):
#     print(num,item) 輸出num為次數 item是陣列值
##################################################************join和格式化字串
# total = 0.0
# a = [0] * 5

# for i in range(5):
#     a[i] = float(input())
#     total += a[i] 
# avg = total / 5
# print(" ".join(f"{x:g}" for x in a)) 去掉無意義的小數點
# print(f"Sum = {total:.1f}")
# print(f"Average = {avg:.1f}")
###################################################次方寫法
# ax = float(input())
# ay = float(input())
# bx = float(input())
# by = float(input())
# d = ((ax-bx)**2+(ay-by)**2)**(1/2)
# print(f"( {ax:g} , {ay:g} )")
# print(f"( {bx:g} , {by:g} )")
# print(f"Distance = {d:.4f}")
###################################################**********引入math
# import math
# s = int(input())
# area = ((5*(math.pow(s,2))/(4*math.tan(math.pi/5))))
# print(f"Area = {area:.4f}")
###################################################閏年
# while(1):
#     a = int(input())
#     if(a%400==0):
#         print(f"{a} is a leap year.")
#     elif(a%100==0):
#         print(f"{a} is not a leap year.")
#     elif(a%4==0):
#         print(f"{a} is a leap year.")
#     else:
#         print(f"{a} is not a leap year.")
###################################################**************字串判斷
# while(1):
#     a = input()
#     if(a.isalpha()):
#         print(f"{a} is an alphabet.")
#     elif(a.isdigit()):
#         print(f"{a} is a number.")
#     else:
#         print(f"{a} is a symbol.")
#     // a.isalnum 判斷是否全為數字 or 字母
#     // a.isdecimal 判斷是否為十進制
#     text = "abcdefg"
#     for char in text: //逐字判斷
#####################################################***********判斷是否三角形
# while(1):
#     a = [0]*3
#     max =0
#     total =0
#     for i in range(3):
#         a[i] = int(input())
#         if(a[i]>max):
#             max = a[i]
#             temp = i
#     for j in range(3):
#         if(j!=temp):
#             total += a[j]
#     if(total > a[temp]):
#         print(total+a[temp])
#     else:
#         print("Invalid")
##################################################指定範圍的迴圈
# a = int(input())
# b = int(input())
# total = 0
# for i in range(a,b+1):
#     total += i
# print(total)
#################################################************!!!!三角形!!!!
# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(f"{i * j:>4}", end="")
#     print()
#################################################*************字串反轉
# 第一種
# s = input()
# print(s[::-1]) # s[開始:結束:間隔]
# 第二種
# s = input()
# rs =""
# for char in s:
#     rs = char+rs
# print(rs) 
# 第三種
# s = input()
# print("".join(reversed(s)))
####################################################99乘法表
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{j:<2}{"*":<2}{i:<2}{"=":<2}{j*i:<4}",end="")
#     print()
################################################字串轉整數
# a = int(input())
# total = 0
# for i in range(a):
#     b = input()
#     for char in b:
#         total += int(char)
#     print(f"Sum of all digits of {b} is {total}")
#     total =0
#######################################################格式化輸出   
# a = int(input())
# b = float(input())
# c = int(input())

# total = a
# print('%s \t  %s' % ('Month', 'Amount'))

# for i in range(1, c + 1):
#     total += total * b / 1200
#     print('%3d \t %.2f' % (i, total)) %-3d是靠左
#####################################################遞減迴圈
# a = int(input())
# total = 0.0
# for i in range(a,1,-1):
#     if(i!=1):
#         total += 1/((i-1)**(1/2)+(i)**(1/2))
# print(f"{total:.4f}")
#####################################################找最小值
# a = [0]*10
# for i in range(10):
#     a[i] = int(input())
# c = min(a) #min函數直接找
# print(c)
########################################################空格分割輸出找三個最大值
# a = [0]*10
# b = [0]*3
# sum =0
# for i in range(10):
#     a[i] = int(input())
# for j in range(3):
#     b[j] = max(a) #max函數
#     temp = a.index(b[j]) #找最大值的index
#     a[temp] = 0
# print(" ".join(map(str,b))) #用空格分隔值 map將int字串轉成str
# print(*b) #用空格分隔值
############################################################*********************二微陣列最大最小
# a:list[list:int] = [[0 for _ in range(3)] for _ in range(3)]
# for i in range(3):
#     for j in range(3):
#         a[i][j] = int(input())
# a_max = max(max(r) for r in a)
# a_min = min(min(s) for s in a)
# for i in range(3):
#     for j in range(3):
#         if(a[i][j]==a_max):
#             max_i = i
#             max_j = j
#         if(a[i][j]==a_min):
#             min_i = i
#             min_j = j
# print(f"Index of the largest number {a_max} is: ({max_i}, {max_j})")
# print(f"Index of the smallest number {a_min} is: ({min_i}, {min_j})")
###################################################輸入定值才結束輸入 switch case
# while(1):
#     n = int(input())
#     if n ==-9999:
#         break
#     match n:
#         case s if 90 <=s<=100:
#             print("A")
#         case s if 80 <=s<90:
#             print("B")
#         case s if 70 <=s<80:
#             print("C")
#         case s if 60 <=s<70:
#             print("D")
#         case s if s<60:
#             print("E")
###################################################################****************正三角形
# n = int(input())
# for i in range(n):
#     # print(i)
#     for y in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
##################################################################函式
# def compute(a,b,c):
#     print(f"Department: {a}")
#     print(f"Student ID: {b}")
#     print(f"Name: {c}")

# a = input()
# b = input()
# c = input()
# # a,b,c = input().split(" ") 以空格分開 只有str可用
# compute(a,b,c)
#########################################################最大公因數&分數加減
# import math;
##找最大公因數(分母)
# def compute(a,b):
#    ans = math.gcd(a,b)
#    return ans
# a,b = input().split(",")
# c,d = input().split(",")
# # compute(a1,a2)
# p = int(a)*int(d) + int(b)*int(c)
# q = int(b)*int(d)
# ans= compute(p,q)
# a1 = int(p/ans)
# a2 = int(q/ans)
# print(f"{a}/{b} + {c}/{d} = {a1}/{a2}")
########################################################找質數
# def compute(a):
#     for i in range(2,a):
#         if(a%i==0):
#             return False
#         else:
#             return True
# a = int(input())
# c = compute(a)
# if c:
#     print("Prime")
# else:
#     print("Not Prime")
############################################################費式數列
# def compute(n):
#     a = [0]*999
#     a[0] =0
#     a[1] =1
#     print(a[0],a[1],end=" ")
#     for i in range(2,n):
#         a[i] = a[i-1] + a[i-2]
#         print(a[i],end=" ")
# n = int(input())
# compute(n)
##############################################################################匯入寫入匯出成txt檔案
# with open("data.txt","r",encoding="utf-8") as f: #r是讀 w寫 a附加
#         char = f.read().split("\n")
#         for i in range(5):
#             char.append(input())
# with open("data.txt","w",encoding='utf-8') as f:
#         f.write("Append completed!\n")
#         f.write("Content of \"data.txt\":\n")
#         for a in char:
#             f.write(f"{a}\n")
# with open("data.txt","r",encoding='utf-8') as f:
#         c = f.read()
#         print(c,end="")
#############################################################################分割讀取資料
# with open("read.txt", "r", encoding="utf-8") as f:
#     c = f.read()
#     s = c.splitlines()
#     a = []
#     for line in s:
#         data = line.split()
#         a.append([data[0], int(data[1]), int(data[2])])
#     total_h = 0
#     total_w = 0
#     max_i = 0
#     max_j = 0
#     for i in range(len(a)):
#         total_h += a[i][1]
#         total_w += a[i][2]
#         if a[i][1] > a[max_i][1]:
#             max_i = i
#         if a[i][2] > a[max_j][2]:
#             max_j = i
#     c1 = c.split("\n")
#     print(c1[0])
#     print()
#     print(c1[1])
#     print()
#     print(c1[2])
#     print(f"Average height: {total_h / len(a):.2f}")
#     print(f"Average weight: {total_w / len(a):.2f}")
#     print(f"The tallest is {a[max_i][0]} with {a[max_i][1]:.2f}cm")
#     print(f"The heaviest is {a[max_j][0]} with {a[max_j][2]:.2f}kg")
# ########################################################################移出指定檔案資料
# fe = input()
# s = input()

# with open(fe, "r", encoding="utf-8") as f:
#     before = f.read()
# print("=== Before the deletion")
# print(before)

# # 移除輸入的元素
# after = before.replace(s, "", 1) 用""把s取代

# with open(fe, "w", encoding="utf-8") as f:
#     f.write(after)
# print("=== After the deletion")
# print(after)
###############################################################**************判斷文字
# fe = input()
# with open(fe, "r", encoding="utf-8") as f:
#     before = f.read().splitlines()
# lines = len(before)  # 行數
# a = []
# total = 0            # 單字數
# total1 = 0           # 字母數
# for line in before:
#     a.append(line.split())
# for row in a:
#     total += len(row)
# for line in before:
#     for char in line:
#         if char.isalpha():
#             total1 += 1
#         elif char.isspace():
#             total1 +=0
#         else:
#             total1+=1
# print(f"{lines} line(s)")
# print(f"{total} word(s)")
# print(f"{total1} character(s)")
######################################################找男女
# with open("read.dat","r",encoding="utf-8") as f:
#     before = f.read().splitlines()
#     g=0
#     b=0
#     for line in before[1:]:
#         data = line.split()
#         if(data[2]=="0"):
#             g+=1
#         else:
#             b+=1
# print(g,b)