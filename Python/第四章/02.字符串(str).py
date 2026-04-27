s="Hello-World"
# print(s[4])
# print(s[-8])

# for i in s:
#     print(i)
#
# print(s[0:5:1])

mail=input("请输入邮箱: ")
# if mail.count("@")==1 and mail.count(".")>=1 :
#     print(f"{mail}是合法邮箱")
# else:
#     print(f"邮箱非法")
# 
if mail.count("@")==1 and "." in mail:
    print(f"{mail}是合法邮箱")
else:
    print(f"不是合法邮箱")