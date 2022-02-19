from email import message


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# リストの最後を取得
print(bicycles[-1].title())

message = f"私の最初の自転車は{bicycles[0].title()}でした。"
print(message)