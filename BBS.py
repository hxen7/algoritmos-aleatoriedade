# Blum-Blum-Shub (BBS)

def blum_blum_shub(seed, p=11, q=19, length=10):
    n = p * q
    result = []
    x = (seed ** 2) % n
    for _ in range(length):
        x = (x ** 2) % n
        result.append(x % 2)
    return result

print(blum_blum_shub(seed=3))
