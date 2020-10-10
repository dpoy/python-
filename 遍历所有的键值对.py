user_0 = {
    'username': 'shark',
    'first': 'enric',
    'last': 'hai',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)  # 键值对成队出现

favourite_language = {
    'Jen': 'python',
    'lucks': 'c',
    'phil': 'java',
}

for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is " + language.title() + '.\n')

for name in favourite_language.keys():
    print(name.title() + '\n')

for language in favourite_language.values():
    print(language.title())