first_list =[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

second_list = [i for i in first_list if first_list.count(i) == 1]

print(second_list)
