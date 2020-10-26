alien_0 = {'color': 'green'}
print('This alien is ' + alien_0['color'] + '.\n')

alien_0 = {'color': 'yellow'}
print('This alien is ' + alien_0['color'] + '.\n')

alien_0 = {"x_position": 0, 'y_position': 25, 'speed': "medium"}  # 字典中x，y位置是变量，不能打引号

if alien_0["speed"] == 'slow':
    x_increment = 1
if alien_0["speed"] == 'medium':
    x_increment = 2
if alien_0["speed"] == 'high':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment  # x_increment + alien_0['x_position']

print("New x-position: " + str(alien_0['x_position']))  # 输出为字符串所有用函数str()把字典中的value变成字符串.

