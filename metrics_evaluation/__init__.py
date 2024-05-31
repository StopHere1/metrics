# Importing functions to make them available at the package level
from .metrics_evaluation import *


# from .module2 import function2
# print("__init__ script is executed")
# Setting the version of the package
__version__ = '0.1.0'

# Initializing package-level data
print("Initializing the package")

# Defining the package API
__all__ = ['MAE','include_test','MSE','MAPE','RMSE']