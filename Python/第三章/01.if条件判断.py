# score=700
# if score>680:
#     print("欢迎来Thu")
#     print("恭喜你")
# print("..................")
from importlib.metadata import pass_none

# ok_account="18888888888"
# ok_password="666888"
# account=input("请输入账号： ")
# password=input("请输入密码: ")
# # if account==ok_account and password==ok_password:
# #     print("登陆成功")
# #     print("进入首页")
# # if account!=ok_account or password!=ok_password:
# #     print("登录失败")
# #     print("请重新输入")
#
# if account==ok_account and password!=ok_password:
#     print("登陆成功")
#     print("进入首页")
# else:
#     print("登录失败")
#     print("请重新输入")

# year=int(input("请输入一个年份: "))
# if (year%100 !=0 and year%4==0) or (year%400==0):
#     print("该年份是闰年")
# else:
#     print("该年份是平年")

# num=input("请输入数字: ")
# if num>0:
#     print(f"{num}是一个正数")
# elif num<0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}为0")

a=int(input("请输入第一个边: "))
b=int(input("请输入第二个边: "))
c=int(input("请输入第三个边: "))

if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("等边三角形")
    elif a==b or b==c or a==c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不能构成一个三角形")

