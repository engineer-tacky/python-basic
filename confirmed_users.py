# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"確認中のユーザー: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\n以下のユーザーは確認済みです。")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

from urllib import response


responses = {}
polling_active = True

while polling_active:
    name = input("あなたのお名前は？")
    response = input("いつか登りたい山はなんですか？")

    responses[name] = response

    repeat = input("誰か他に回答してくれる人はいますか？(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- 投票結果 ---")
for name, response in responses.items():
    print(f"{name}さんが登りたいのは、{response}です。")