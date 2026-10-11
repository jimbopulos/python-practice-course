my_list = [1, 2, 3]
# print(my_list)

my_list = ['STRING', 100, 23.2]
# print(len(my_list))

my_list = ['one', 'two', 'three']
# print(my_list[0])
# print(my_list[1:])

another_list = ['four', 'five']
# print(my_list + another_list)

new_list = my_list + another_list
# print(new_list)

new_list[0] = 'ONE ALL CAPS'
# print(new_list)

new_list.append('six')

new_list.append('seven')

new_list.pop()

popped_item = new_list.pop()

new_list.pop(0)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()

my_sorted_list = new_list

num_list.sort()
num_list.reverse()

# print(my_sorted_list)
print(num_list)
