from kecutil import reduce


strings = ["ab", "acb", "abcdef", "abd"]
longestString = reduce(lambda x, y: x if len(x) > len(y) else y, strings, "")

print(longestString)