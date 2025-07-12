multipliers = [0, 1, 2]
funcs = list(map(lambda i: (lambda x: x * i), multipliers))

print(funcs[0](10))  # 0
