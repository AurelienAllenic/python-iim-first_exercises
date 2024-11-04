list_number = [33, 6, 9, 12, 90, 34, 56]
list_number_2 = [{"value": 33}, {"value": 6}, {"value": 9}, {"value": 12}, {"value": 90}, {"value": 34}, {"value": 56}]

list_number.sort()

print(list_number)

def sort_list(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

sort_list(list_number)

print(list_number)

lambda x: x + 1

list_number_2_sorted = sorted(list_number_2, key=lambda x: x["value"])

print(list_number_2_sorted)