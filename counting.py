# from operator import truediv


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# active = True
# while active:
#     message = input("何か書いてください。'終了'と打てば終わります。")

#     if message == '終了':
#         active = False
#     else:
#         print(message)

# while True:
#     message = input("何か書いてください。'終了'と打てば終わります。")

#     if message == '終了':
#         break
#     else:
#         print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)