from alpha_term import AlphaTerm

# Terms
term1 = AlphaTerm(2, "x", 3)
term2 = AlphaTerm(4, "y", 6)
term3 = AlphaTerm(5, "x", 4)
term4 = AlphaTerm(3, "y", 8)
term5 = AlphaTerm(1, "z", 2)
term6 = AlphaTerm(3, "z", 3)
term7 = AlphaTerm(4, "t", 1)
term8 = AlphaTerm(3, "a", 0)
term9 = AlphaTerm(0, "b", 2)

mterm1 = term1 * term2 * term7  # 2x³ * 4y⁶ * 4t = 32x³y⁶t
mterm2 = term3 * term5 * term4  # 5x⁴ * z² * 3y⁸ = 15x⁴z²y⁸
mterm3 = mterm1 * mterm2  # 32x³y⁶t * 15x⁴z²y⁸ = 480x⁷y¹⁴tz²
mterm4 = term8 * term9  # 1 * 0 = 0
mterm5 = 5 * term2 * 10 * mterm2 * 8 * term8  # 5 * 4y⁶ * 10 * 15x⁴z²y⁸ * 8 = 24000x⁴z²y¹⁴
mterm6 = ((mterm1 / 2) * term8) ** 2  # ((32x³y⁶t / 2) * 1)² = 256x⁶y¹²t²

print(mterm1)
print(mterm2)
print(mterm3)
print(mterm4)
print(mterm5)
print(mterm6)
