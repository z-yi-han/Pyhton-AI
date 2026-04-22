day=input("请输入日期: ")
match day:
    case "1":
        print("周一，工作日")
    case "2":
        print("周二，工作日")
    case "3":
        print("周三，工作日")
    case "4":
        print("周四，工作日")
    case "5":
        print("周五，工作日")
    case "6"|"7":
        print("休息日")
    case _:
        print("输入错误！")
