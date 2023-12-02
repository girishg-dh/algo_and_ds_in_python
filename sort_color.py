def sort_colors(colors):
    length = len(colors)
    red, white, blue = 0, 0, length-1
    while white <= blue and red <= white:
        if colors[white] == 0:
            colors[red], colors[white] = swap(colors[red], colors[white])
            red += 1
            white += 1
        elif colors[white] == 1:
            white += 1
        else:
            colors [blue], colors[white] = swap(colors[blue], colors[white])
            blue -= 1
    # Replace this placeholder return statement with your code
    return colors

def swap(left, right):
    return right, left


if __name__ == '__main__':
    print(sort_colors([2, 2, 1, 1, 0]))
    print(sort_colors([2, 2, 0, 1, 2, 2, 0, 2]))
    print(sort_colors([0, 0, 1, 0, 1, 1, 1, 2, 1, 2]))