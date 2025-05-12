def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    n = (x2 - x1) / (v1 - v2)
    if n >= 0 and n.is_integer():
        return "YES"
    else:
        return "NO"
