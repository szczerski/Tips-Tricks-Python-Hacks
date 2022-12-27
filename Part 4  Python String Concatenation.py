txt = ["P", "y", "t", "h", "o", "n", 3, '.', 1, 1]

# 94 characters
result = []
for x in txt:
    result.append(str(x))
result = "".join(result)
print(result)

# 91 characters
def print_txt(txt):
    print("".join(str(x) for x in (yield from txt)))
print_txt(txt)

# 93 characters
print("".join(str(chr(x + 48)) if i in (6, 8, 9)
      else x for (i, x) in enumerate(txt)))

# 64 characters
print("".join(str(x) if isinstance(x, int) else x for x in txt))

# 61 characters
print(txt.__str__()[1:-1].replace(", ", "").replace("'", ""))

# 43 characters
print("".join("{}".format(x) for x in txt))

# 42 characters
print("".join(map(lambda x: str(x), txt)))

# 42 characters
print("{}{}{}{}{}{}{}{}{}{}".format(*txt))

# 37 characters
print("".join([str(x) for x in txt]))

# 35 characters - third place
print("".join(str(x) for x in txt))

# 29 characters - second place
print("".join(map(str, txt)))

# 19 characters - first place
print(*txt, sep="")
