from random import choice

shopping_cart={}
print("欢迎使用购物车管理系统")
menu="""
    #####购物车管理系统#####
    #    1.添加购物车
    #    2.修改购物车
    #    3.删除购物车
    #    4.查询购物车
    #    5.退出购物车
    #####################
"""
print(menu)
while True:
    choice =input("请选择操作: ")
    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
            break
        case _:
            print("输入错误,请重新输入！")



