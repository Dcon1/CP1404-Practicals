def count_blocks(n):
    if n == 0:
        return 0
    else:
        print(n)
        count_blocks(n - 1)


count_blocks(6)