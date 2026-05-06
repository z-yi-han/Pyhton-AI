try:
    print("----------------")
    #print(1/0)
    #print(my_name)
    print("ABC"[10])
    #print("----------------")
except NameError as e:
    print("程序运行出错,请联系管理员,异常信息: ",e)
except ZeroDivisionError as e:
    print("程序出错了，请联系管理员，异常信息: ",e)
except IndexError as e:
    print("程序出错了，请联系管理员，异常信息: ", e)
except Exception as e:
    print("程序出错了，请联系管理员，异常信息: ", e)
finally:
    print("资源释放~")
