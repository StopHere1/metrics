import numpy as np

# eqaution for MAE: sigma(abs(y_i - y^hat))
def check_input_dimension(ground_truth, prediction):
    if ground_truth.shape[0] != prediction.shape[0]:
            print("Error: the ground truth and prediction should be 2 numpy array of shape (n,1) or (n,)")
            return False
    ground_truth.reshape(ground_truth.shape[0],1)
    prediction.reshape(prediction.shape[0],1)
    return True

def MAE(ground_truth, prediction):
    if not check_input_dimension(ground_truth,prediction):
        return
    return np.sum(np.abs(ground_truth-prediction))/ground_truth.shape[0]

def MSE(ground_truth, prediction):
    if not check_input_dimension(ground_truth,prediction):
        return
    return np.sum(np.abs(ground_truth.T@ground_truth-prediction.T@prediction))/ground_truth.shape[0]

def MAPE(ground_truth, prediction):
    if not check_input_dimension(ground_truth,prediction):
        return
    return 100*np.sum(np.divide(np.abs(ground_truth-prediction),np.abs(ground_truth)))/ground_truth.shape[0]

def RMSE(ground_truth, prediction):
    if not check_input_dimension(ground_truth,prediction):
        return
    return np.sqrt(np.sum(np.abs(ground_truth.T@ground_truth-prediction.T@prediction))/ground_truth.shape[0])

def include_test(): 
    print("Hello from metrics module!")



