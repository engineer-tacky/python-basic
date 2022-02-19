from email import message, message_from_string


names = ['james', 'john', 'samuel', 'lisa']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = f"私の友達の{names[0]}です。"
print(message)

cars = ['toyota', 'nissan', 'honda', 'subaru']
message = f"私は、{cars[-1]}の車が欲しい。"
print(message)