import random

a = "おにぎり"
b = "サンドイッチ"

riceball_list = [75, 80, 100, 120, 150]
sandwich_list = [200, 250, 280, 300, 350]

riceball_price = random.choice(riceball_list)
sandwich_price = random.choice(sandwich_list)

n = random.randint(2, 75)

riceball_number = random.randint(1, n - 1)
sandwich_number = n - riceball_number

m = riceball_price * riceball_number + sandwich_price * sandwich_number

sentence = f"""{a}は１つ{riceball_price}円、{b}は１つ{sandwich_price}円です。
サトルくんが{a}と{b}を合計で{n}個買ったところ、{m}円かかりました。
サトルくんは{a}を何個買ったでしょう。"""

answer = f'{riceball_number}個'






