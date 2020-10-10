alien_0 = {'color': 'yellow', 'points': 5}
alien_1 = {'color': 'green', 'points': 6}
alien_2 = {'color': 'purple', 'points': 8}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
# 创建一个存储外星人的列表
aliens = []

# 创建三十个绿色外星人
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 8}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens:" + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '6'

for alien in aliens[0:5]:
    print(alien)
