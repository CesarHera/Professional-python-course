# def remove_duplicated(some_list: list) -> list:
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

# def run():
#     a = [1, 1, 1, 2, 2, 2]
#     print(a)
#     print(remove_duplicated(a))






# def remove_duplicates(some_list: list) -> list:
#     return list(set(some_list))

# def run():
#     print(remove_duplicates([1,1,1,1,2,2,2,2,2,3,3,3,4,4,54,8]))





# remove_duplicates = lambda some_list: list(set(some_list))
# print(remove_duplicates([1,1,1,1,12,2,2,2,2,3,334,4,]))


# w_dup = []
# [w_dup.append(i) for i in [1,1,11,12,2,2,2,2] if i not in w_dup]
# print(w_dup)