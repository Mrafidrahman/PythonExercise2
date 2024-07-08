data_list = [13,24,'Karim',{'name':'guru'},45,17]

new_data_list = []
for x in data_list:
    if isinstance(x, int):
        new_data_list.append(x)
    else:
        continue

print(new_data_list)
