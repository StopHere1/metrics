import sys
import numpy as np

original_sys_path = sys.path.copy()
sys.path.append('../')

import metrics_evaluation
metrics_evaluation.include_test()
sys.path = original_sys_path    

X = np.array([1,2,3,4,5])
Y1 = np.array([2,3,4,5,6])
Y2 = np.array([2.2,3,4,5,6])
Y3 = np.array([2.2,3,4,5,6.1])
n_test = 3
n_test_passed = 0

if 1 == metrics_evaluation.MAE(X,Y1):
   n_test_passed+=1
if 1.04 == metrics_evaluation.MAE(X,Y2):
    n_test_passed+=1
if 1.06 == metrics_evaluation.MAE(X,Y3):
    n_test_passed +=1
if n_test_passed == n_test:
    print("MAE Test Passed")

n_test = 3
n_test_passed = 0
X = np.array([1,2,3,4,5])
Y1 = np.array([1,2,3,4,5])
Y2 = np.array([2,3,4,5,6]) # 4-1+9-4+16-9+25-16+36-25 = 3+5+7+9+11 = 35
Y3 = np.array([4,5,6,7,8]) # 

if 0 == metrics_evaluation.MSE(X,Y1):
   n_test_passed+=1
if 7 == metrics_evaluation.MSE(X,Y2):
    n_test_passed+=1
if 27 == metrics_evaluation.MSE(X,Y3):
    n_test_passed +=1
if n_test_passed == n_test:
    print("MSE Test Passed")