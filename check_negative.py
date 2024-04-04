import numpy as np

sales_3d_array = np.load('sales_3d_array.npy')
neg_indices = np.where(sales_3d_array < 0)

if len(neg_indices[0]) > 0:
    print("The array contains negative values at the following indices:")
    for idx in range(len(neg_indices[0])):
        i, j, k = neg_indices[0][idx], neg_indices[1][idx], neg_indices[2][idx]
        value = sales_3d_array[i, j, k]
        print(f"Index ({i}, {j}, {k}): Sales{value}")
else:
    print("The array does not contain negative values.")