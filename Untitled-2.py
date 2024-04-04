# %%
import numpy as np
import tensorly as tl
from tensorly.decomposition import non_negative_parafac, partial_tucker

# %%
sales_tensor = np.load('sales_3d_array.npy')


# %%
rank = 10

factor_matrices = non_negative_parafac(sales_tensor, rank=rank)

# %%


# print("Factor Matrix for Articles (Shape: {}):".format(article_factors.shape))
# print(article_factors)
# print("\nFactor Matrix for Regions (Shape: {}):".format(region_factors.shape))
# print(region_factors)
# print("\nFactor Matrix for Weeks (Shape: {}):".format(week_factors.shape))
# print(week_factors)


# %%



