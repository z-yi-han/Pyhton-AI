# s=[1,2,3,4,5,6,7,8,9]
# print(type(s))
#
# print(s[0]) #正向索引
# print(s[-9]) #反向索引
# s[ 5 ]="ABC"
# print(s)
#
# del s[ 5 ]
# print(s)
#
# for item in s:
#     print(item)

# s=[1,2,3,4,5,6,7,8,9,10]
# m=s[:5]
# print(m)
# print(type(m))
# n=s[0:4:2]
# print(n)
# print(type(n))

# s=['A','B','C','D','E','F','G','H','I','J']
# s.append('K')
# print(s)
# s.remove('K')
# print(s)
# s.sort()
# print(s)
# s.pop()
# print(s)
# s.pop(0)
# print(s)
# s.reverse()
# print(s)
# s.sort()
# print(s)
# s.insert(0,'A')
# print(s)
nums_list=[]
for it in range(10):
    num=int(input("输入数字: "))
    nums_list.append(num)

print("数字列表: ",nums_list)

nums_list.sort()
print(f"排序后数字列表: {nums_list}")

print("最小值:",nums_list[0])
print("最大值:",nums_list[-1])
