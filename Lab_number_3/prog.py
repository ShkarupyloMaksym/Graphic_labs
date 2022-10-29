import matplotlib.pyplot as plt


def ccw(p, a, b):
    return (a[0] - p[0]) * (b[1] - p[1]) - (a[1] - p[1]) * (b[0] - p[0])


def find(points):
    points_for_change = points.copy()
    points_for_change.sort(key=lambda a: a[0])
    points_for_change.sort(key=lambda a: a[1])
    stack = []
    for point in points_for_change:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    stack_len = len(stack)
    points_for_change.reverse()
    for point in points_for_change:
        while len(stack) > stack_len and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack


dpi = plt.rcParams['figure.dpi']
fig = plt.figure(figsize=(960/dpi, 540/dpi))       # size in inches

dots_list = []
with open("DS7.txt", "r") as file:
    for dot_line in file:
        if dot_line == "":
            break
        dot_arr = dot_line.split()
        dots_list.append([int(dot_arr[1]), int(dot_arr[0])])

plt.plot([i[0] for i in dots_list], [i[1] for i in dots_list], '.r')
dots_list = find(dots_list)
xcoor = [i[0] for i in dots_list]
ycoor = [i[1] for i in dots_list]
xcoor.append(xcoor[0])
ycoor.append(ycoor[0])
plt.plot(xcoor, ycoor, '-b')

plt.savefig("Shkarupylo_7Var.png")
plt.show()
plt.close()
