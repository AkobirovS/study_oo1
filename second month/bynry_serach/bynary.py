# # number = int(input("add the number: "))
# # arr = [4,5,2,8,6,2,815,6552,632,522,335]
# # arr = sorted(arr)
# # rights = len(arr)
# # left = 0
# # while left <= rights:
# #     mid = (rights + left)// 2
# #     if arr[mid] == number:
# #         print(number)
# #     elif arr[mid] < number:
# #         left = mid + 1
# #         print(mid)
# #     else:
# #         print(mid)
# #         rights = mid - 1
# #
#
#
# def bynery_search(number , arr):
#     arr = sorted(arr)
#     rights = len(arr)
#     left = 0
#     while rights >= left:
#         mid = (rights + left) // 2
#         if arr[mid] == number:
#             return mid
#         elif arr[mid] > number:
#             rights = mid - 1
#         else:
#             left = mid + 1
#     return -1
# # print(bynery_search(2,[1,2,3,4,5,6,7,8,9]))
# number_1 = int(input("thing a number :: "))
# number_3 = 100
# number_2 = input("number< 50")
# number_3 //= 2
# if number_2 == "y":
#     number_3 //= 2
#     number_2 = input(f"number<{number_3}")
#     if number_2 == "y":
#         number_3 //= 2
#         number_2 = input(f"number<{number_3}")
#         if number_2 == "y":
#             number_3 //= 2
#             number_2 = input(f"number  {number_3}")
#             if number_2 == "y":
#                 number_3 //= 2
#                 number_2 = input(f"number id {number_3}")
# else:
#     pass