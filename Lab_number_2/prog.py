import matplotlib.pyplot as plt

dpi = plt.rcParams['figure.dpi']
fig = plt.figure(figsize=(960/dpi, 540/dpi))       # size in inches
with open("DS7.txt", "r") as file:
    for dots in file:
        if dots == "":
            break
        dot = dots.split()
        plt.plot(int(dot[1]), int(dot[0]), '.r')


plt.savefig("Shkarupylo_7Var.png")
plt.show()
plt.close()
