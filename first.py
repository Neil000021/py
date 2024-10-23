#'''RPG剪刀石頭布遊戲'''
#import random
#
#'''定義角色的初始屬性'''
#class Player:
#    def __init__(self, name):
#        self.name = name
#        self.hp = 100
#
#    def take_damage(self, damage):
#        self.hp -= damage
#        if self.hp < 0:
#            self.hp = 0
#
#    def is_alive(self):
#        return self.hp > 0
#
#choices = ["剪刀", "石頭", "布"]
#
#'''判斷勝負的函數'''
#def determine_winner(player_choice, computer_choice):
#    if player_choice == computer_choice:
#        return "平手"
#    elif (player_choice == "剪刀" and computer_choice == "布") or \
#         (player_choice == "布" and computer_choice == "石頭") or \
#         (player_choice == "石頭" and computer_choice == "剪刀"):
#        return "玩家"
#    else:
#        return "電腦"
#'''遊戲主函數'''
#def game():
#    player_name = input("請輸入你的名字: ")
#    player = Player(player_name)
#    computer = Player("電腦")
#
#    print(f"歡迎來到剪刀石頭布對戰, {player.name}!")
#
#    while player.is_alive() and computer.is_alive():
#        print(f"\n{player.name} 的HP: {player.hp} | 電腦的HP: {computer.hp}")
#        
#        # 玩家選擇
#        player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#        while player_choice not in choices:
#            print("無效的選擇，請重新選擇")
#            player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#
#        # 電腦隨機選擇
#        computer_choice = random.choice(choices)
#        print(f"電腦選擇了: {computer_choice}")
#
#        # 判斷勝負
#        result = determine_winner(player_choice, computer_choice)
#
#        if result == "玩家":
#            print(f"{player.name} 勝利！")
#            computer.take_damage(20)
#        elif result == "電腦":
#            print("電腦勝利！")
#            player.take_damage(20)
#        else:
#            print("這局平手！")
#
#    # 遊戲結束
#    if player.is_alive():
#        print(f"\n{player.name} 獲勝了！")
#    else:
#        print("\n電腦獲勝了！")
#
## 開始遊戲
#game()