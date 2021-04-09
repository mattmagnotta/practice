print('hello welcome to the fucking Unit Converter!')
user_distance = int(input('how long is your fucking distance? '))
print('jesus thats fucking long')
user_unit = input('What fucking conversion are you doing?')

distance_dict = {'ft': .3048,'mi': 1609.34, 'km':1000}
converted_distance = user_distance * distance_dict[user_unit]
def distance_converter(user_unit,distance_dict,user_distance):
    converted_distance = user_distance * distance_dict[user_unit]
    return converted_distance
distance_converter(user_distance,distance_dict,user_unit)
