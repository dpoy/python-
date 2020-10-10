cars = ['audi', 'bmw', 'toyota', 'honda']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

car = 'honda'
print('\n', car == 'honda')

print('\n', car == 'bmw', '\n')

age = 19

if age >= 18:
    print("You are old enough to vote")


alien_0 = {'color': 'green', 'point': '5'}
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 5
alien_0['y_position'] = 100
print(alien_0)