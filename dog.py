class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name}はお座りしている。")

    def roll_over(self):
        print(f"{self.name}がゴローンした！")

my_dog = Dog('ウィリー', 6)
your_dog = Dog('ルーシー', 3)
print(f"私の犬の名前は、{my_dog.name}です。")
print(f"私の犬は、{my_dog.age}歳です。")
my_dog.sit()

print(f"\nあなたの犬の名前は、{your_dog.name}です。")
print(f"あなたの犬は、{your_dog.age}歳です。")
your_dog.sit()