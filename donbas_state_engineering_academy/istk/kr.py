import numpy as np

A = np.array([[1, 3, 5, 8],
              [3, 5, 8, 0],
              [5, 8, 0, 0],
              [8, 0, 0, 0]])


def determinant(matrix):
    return round(np.linalg.det(matrix), 2)


det1 = determinant(A)
det2 = determinant(A[1:, 1:])
det3 = determinant(A[2:, 2:])

print("Обчислення детермінанту 4x4 (Δ₁):")
print(f"Δ₁ = {det1}")

print("\nОбчислення детермінанту 3x3 (Δ₂):")
print(f"Δ₂ = {det2}")

print("\nОбчислення детермінанту 2x2 (Δ₃):")
print(f"Δ₃ = {det3}")

if det1 > 0 and det2 > 0 and det3 > 0:
    print("\nСистема є стійкою.")
else:
    print("\nСистема не є стійкою.")
