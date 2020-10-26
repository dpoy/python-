mc = ["asa", "sdj", "ss"]
for i in mc:
    print(i.title() + ", that was agret trick!")
    print("I can‘t see you next tirck, " + i.title() + "!\n")

print("Congrutions everone! \n")

for i in range(0,5):
    print(i)

print("\n")

numbers = list(range(1, 6))
print(numbers)
print("\n")

print(min(numbers))
print("\n")


squares = []
for value in range(0,6):
    square = value**2
    squares.append(square)

print(squares)
print("\n")

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
print("\n")

squares = [value for value in range(1, 11)]
print(squares)
print("\n")

players = ['charles', 'martina', 'lee', 'liu', 'mm']
ppp = players[0:3]
print(ppp, '\n')
print(players[:4], '\n')
print(players[:2], '\n')
print(players[1:], '\n')

print(players, "\n")

players = ['charles', 'martina', 'lee', 'liu', 'mm', 'dachacha', 'makeli', 'temeipu']
for player in players[:4]:
    print("This is my man @" + player, "\n")
pppp = [print("This is my man @" + player, '\n') for player in players[:5]]
# 为什么这个列表不能使用sort方法
my_favourite_foods = ['sanmingzhi', 'pai', 'hot dog']
my_friends_foods = my_favourite_foods[:]

zhongjianbianliang = my_favourite_foods.sort(reverse=True)
print(zhongjianbianliang)
my_friends_foods = zhongjianbianliang

print("My favourite foods are :")
print(my_favourite_foods)
print('\nMy friend favourite foods are :')
print(my_friends_foods)

my_foods = ['sanmingzhi', 'pai', 'hot dog']
friends_foods = my_foods[:]
print("My favourite foods are :")
print(my_foods)
print('\nMy friend favourite foods are :')
print(friends_foods)

numbers = list(range(1, 6))
print(numbers)
print("\n")








