my_dict = {'login': 111111,
           'login2': 22222,
           'login3': 33333}
print(my_dict) # 1
print((my_dict.get('login4'))) # 2
print(my_dict['login']) # 3
my_dict['login'] = 'sssss'
print(my_dict['login']) # 4

my_dict.update({'login1s': 44444,
                      'login2ss': 55555})
print(my_dict.pop('login3')) # 5
print(my_dict)

my_set = {1, 2, 3, 'one', 'second', 1.5, 1.5, 1, 'one', 2, 'second', True, False, 17}
print(my_set) # 6
my_set.add(21)
my_set.add(24)
my_set.discard(False)
print(my_set) # 7