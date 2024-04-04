import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac, tucker
print("jolihjk")
# Load the sales tensor
sales_tensor = np.load("sales_3d_array.npy")
print("loaded")
# Perform Sparse CP decomposition
rank = 2
sparse_cp_factors = parafac(sales_tensor, rank=rank, init='random', tol=1e-2, normalize_factors=False, verbose=2, return_errors=True)

# # Perform Sparse Tucker decomposition
# rank = [10, 10, 10]
# sparse_tucker_factors = tucker(sales_tensor, rank=rank, init='random', tol=1e-6, sparsity=0.1, normalize_factors=True)

# View the factorized matrices
print("Sparse CP Factors:")
# for i, factor_matrix in enumerate(sparse_cp_factors[1]):
#     print(f"Factor Matrix {i + 1}:")
#     print(factor_matrix)
#     print()

# print("Sparse Tucker Factors:")
# for i, factor_matrix in enumerate(sparse_tucker_factors[1]):
#     print(f"Factor Matrix {i + 1}:")
#     print(factor_matrix)
#     print()
