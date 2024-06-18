# import csv
# with open('weather_data.csv', ) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         x = row[1:2]
#         for _ in x:
#             if _ == 'temp':
#                 pass
#             else:
#                 data = int(_)
#                 temperatures.append(data)
#     print(temperatures)
import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = data['Primary Fur Color']
color_list = fur_color.to_list()
gray = color_list.count('Gray')
black = color_list.count('Black')
cinnamon = color_list.count('Cinnamon')

new_file_data = {
    'Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}
new_file = pandas.DataFrame(new_file_data)
new_file.to_csv('Color Count')
