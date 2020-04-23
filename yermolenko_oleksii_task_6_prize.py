# Эта задача не отменяет решение основного ДЗ
# Дан лабиринт (Матрица NxN) дана точка входа в лабиринт.
# Стеной являеться символ - # коридор - . Например

with open('yermolenko_oleksii_task_6_prize_in.txt', 'r') as maze_in:
    maze = maze_in.read()
    maze_print = maze.split("\n")
    maze_list = []
    for items in maze_print:
        subl = []
        for num in items.split(' '):
            subl.append(str(num))
            maze_list.append(subl)
    for item in maze_list:
        list2 = []
        list2 = list(item[0])
        print(list2)
    start_point_x = input('please input your point of start (x): ')
    start_point_y = input('please input your point of start (y): ')





# a = "1 2 3; 4 5 6"
#
# aSplit = a.split('; ')
#
# l = []
#
# for item in aSplit:
#     subl = []
#     for num in item.split(' '):
#         subl.append(int(num))
#     l.append(subl)

# print l


# print(maze_list)
    # for item in maze:
    #     print(maze[item])











#
# ##########
# .........#
# ######.###
# #......###
# #.####.###
# #........#
# ##.#######
# ##.##.####
# ##......##
# #######.##
#
# enter = [1,0]
# exit = ???
# Найти выход из лабиринта.
#
# Первые ТРОЕ кто скинет мне решение и сможет его объяснить - получит приз от меня :) Дерзайте!
#
# P.S. Деделайн призовой задачи - 22.03.2020 23:59:59
