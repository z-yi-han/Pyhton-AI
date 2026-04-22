# i=0
# while(i<10):
#     print(",,,,,")
#     i+=1
# else:
#     print("退出循环")

# n=1
# total=0
# while(n<=100):
#     if(n%2==0):
#         total+=n
#     n+=1
# print(total)
# msg=input("请输入字符串:")
# print(msg)
# for s in  msg:
#     print(f"元素：{s}")
# else:
#     print("循环结束")

m=int(input("请输入长方形的长度: "))

n=int(input("请输入长方形的宽度: "))

for j in range(n):
    for i in range(m):
        print("*", end="")
    print()



