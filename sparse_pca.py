import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac, tucker

sales_tensor = np.load("sales_3d_array.npy")

rank = 10  
sparse_cp_factors = parafac(sales_tensor, rank=rank, init='random', tol=1e-6, sparsity='l1', normalize_factors=True)

rank = [10, 10, 10]  
sparse_tucker_factors = tucker(sales_tensor, rank=rank, init='random', tol=1e-6, sparsity='l1', normalize_factors=True)

