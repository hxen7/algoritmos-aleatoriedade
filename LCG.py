# Linear Congruential Generator (LCG)

def lcg(seed, a=1664525, c=1013904223, m=2**32):
    return (a * seed + c) % m

# Gerar números aleatórios
seed = 42
for _ in range(5):
    seed = lcg(seed)
    print(seed / 2**32)
