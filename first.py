import random

# 选项列表
choices = ["剪刀", "石头", "布"]

# 用户输入
user_choice = input("请输入你的选择（剪刀、石头或布）：")

# 电脑随机选择
computer_choice = random.choice(choices)
print(f"电脑选择了：{computer_choice}")

# 判断胜负
if user_choice == computer_choice:
    print("平局！")
elif (user_choice == "剪刀" and computer_choice == "布") or \
     (user_choice == "石头" and computer_choice == "剪刀") or \
     (user_choice == "布" and computer_choice == "石头"):
    print("你赢了！")
else:
    print("你输了！")









