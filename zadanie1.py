height = int(input())
width = int(input())
for h in range(height + 1):
    line = ""
    for w in range(width + 1):
        if h % height == 0 and w % width == 0:
            line += "*"
        elif h % height == 0 and w % width != 0:
            line += "-"
        elif h % height != 0 and w % width == 0:
            line += "|"
        else:
            line += "."
    print(line)
