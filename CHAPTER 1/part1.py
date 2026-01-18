import numpy as np
from scipy import sparse
import sklearn
import pandas as pd
# print("Scikit-learn verison: {}".format(sklearn.__version__))

# eye = np.eye(5)
# print(eye)
# # CONVERT Numpy array into a SciPy sparse matrix
# # Only non-zero entries are stored
# # CSR format
# sparse_matrix = sparse.csr_matrix(eye)
# print("SciPy sparse CSR matrix: \n{}".format(sparse_matrix))

# COO format
data = np.ones(5)
row_indices = np.arange(5)
col_indices = np.arange(5)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation: \n{}".format(eye_coo))


F1Set = {"Team":["Ferrari", "Sauber", "Redbull", "Alpine", "Mercedes", "McLaren"], "Home":["Italy", "Switzerland", "Austria", "France", "Germany", "Great Britain"], "WCC":[16, 0, 6, 2, 8, 8]}
data_pandas = pd.DataFrame(F1Set)
print(data_pandas)
# lets query our table
print("\n",data_pandas[data_pandas.WCC > 5])

