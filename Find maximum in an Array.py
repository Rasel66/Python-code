def height():
    t = int(input())

    for i in range(t):
        n = int(input())
        max_height = 0;
        for i in range(n):
            heights = int(input())
            if heights > max_height:
                max_height = heights
        print(max_height)

height()