
# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = float(input('Введите число:\n'))
n = len(input('Введите число для заданной точности:\n').split('.')[1])
print(f"{a:.{n}f}")