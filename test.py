seq1 = [k**3 for k in range(1,54)]

seq2 = [2**k - 2 for k in range(4, 28)]

seq3 = [k**5 + 1 for k in range(-3, 19)]

seq4 = [2**k for k in range(-2, 8)]

print(sum(seq1)) # 2047761
print(sum(seq2)) # 268435392
print(sum(seq3)) # 6656947
print(sum(seq4)) # 255.75