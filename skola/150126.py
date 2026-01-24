import random
import numpy as np

vectors = []
n = 2

def random_vectors(num):
  for _ in range(num):
    vector = [round(random.random(), 3) for _ in range(5)]
    vectors.append(vector)
  return vectors

print("Random", n, "vector(s):", random_vectors(n))

def dot_product(vts):
  a = np.array(vts[0], dtype=float)
  b = np.array(vts[1], dtype=float)
  
  if a.shape != b.shape:
    raise ValueError("Vectors must have the same dimensions.")
  
  return np.dot(a, b)
  
print("Dot product of", vectors, "is", dot_product(vectors))
