import time

# 开场白逐字打印
text_first = "Hello user !\n你可以随便输入一段话"  # 修正变量名拼写
for ch in text_first:
    print(ch, end="", flush=True)
    time.sleep(0.1)
print()  # 换行

# 输入一段话（不能为空）
while True:
    a = input("请输入一段话：")
    if a.strip():  # 去除空白后非空
        break
    print("错误，请重新输入！")

# 输入要统计的字（允许为空）
b = input("请输入字（如果不输入则为空）：")

# 统计次数
c = a.count(b)

# 输出结果（修正引号问题）
print(f"文中出现了想统计的文字 {c} 次 “{b}”")