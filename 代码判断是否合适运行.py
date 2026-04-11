while True:
    a = input("请输入一段话：")
    print(a)
    if a.strip():
        break
    print("错误，请重新输入！")
    