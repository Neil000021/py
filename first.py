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

import random

class Property:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500  # 每位玩家初始擁有1500金
        self.position = 0

    def move(self, steps):
        self.position = (self.position + steps) % len(board)
        print(f"{self.name} moved to {board[self.position].name}")

    def buy_property(self):
        property = board[self.position]
        if property.owner is None:
            if self.money >= property.price:
                self.money -= property.price
                property.owner = self
                print(f"{self.name} bought {property.name} for {property.price} gold.")
            else:
                print(f"{self.name} doesn't have enough money to buy {property.name}.")
        else:
            print(f"{property.name} is already owned by {property.owner.name}.")

class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0

    def next_turn(self):
        player = self.players[self.current_player_index]
        dice_roll = random.randint(1, 6)
        print(f"{player.name} rolled a {dice_roll}.")
        player.move(dice_roll)
        player.buy_property()

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

# 棋盤設定
board = [
    Property("Start", 0),
    Property("Mediterranean Avenue", 100),
    Property("Community Chest", 0),
    Property("Baltic Avenue", 100),
    Property("Income Tax", 0),
    Property("Reading Railroad", 200),
    Property("Oriental Avenue", 100),
    Property("Chance", 0),
    Property("Vermont Avenue", 100),
    Property("Connecticut Avenue", 120),
    Property("Jail", 0),
    Property("St. Charles Place", 140),
    Property("Electric Company", 150),
    Property("States Avenue", 140),
    Property("Virginia Avenue", 160),
    Property("Community Chest", 0),
    Property("St. James Place", 180),
    Property("Tennessee Avenue", 180),
    Property("New York Avenue", 200),
    Property("Free Parking", 0),
    Property("Kentucky Avenue", 220),
    Property("Chance", 0),
    Property("Indiana Avenue", 220),
    Property("Illinois Avenue", 240),
    Property("B&O Railroad", 200),
    Property("Atlantic Avenue", 260),
    Property("Ventnor Avenue", 260),
    Property("Water Works", 150),
    Property("Marvin Gardens", 280),
    Property("Go to Jail", 0),
    Property("Pacific Avenue", 300),
    Property("North Carolina Avenue", 300),
    Property("Community Chest", 0),
    Property("Pennsylvania Avenue", 320),
    Property("Short Line", 200),
    Property("Chance", 0),
    Property("Park Place", 350),
    Property("Luxury Tax", 0),
    Property("Boardwalk", 400),
]

# 遊戲開始
players = [Player("Player 1"), Player("Player 2")]
game = Game(players)

# 進行10輪遊戲
for _ in range(10):
    game.next_turn()
