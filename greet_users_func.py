def greet_users(names):
    for name in names:
        message = f"こんにちは、{name.title()}!"
        print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)