def helper(x: int):
    tree = [9]
    if tree[0] % x == 0:
        return tree[0]
    deepest = 0
    while True:
        length = len(tree)
        for i in range(length - 2 ** deepest, length):
            a1 = tree[i] * 10
            if a1 % x == 0:
                return a1
            a2 = tree[i] * 10 + 9
            if a2 % x == 0:
                return a2
            tree.append(a1)
            tree.append(a2)
        deepest += 1


a = int(input())
print(helper(a))
