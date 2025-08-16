import numpy as np

def calculate(list):
    if len(list) == 9:
        arrays = np.array(list).reshape(3,3)
        calculations = {
            'mean': [np.mean(arrays, axis=0).tolist(), np.mean(arrays, axis=1).tolist(), np.mean(arrays).item()],
            'variance': [np.var(arrays, axis=0).tolist(), np.var(arrays, axis=1).tolist(), np.var(arrays).item()],
            'standard deviation': [np.std(arrays, axis=0).tolist(), np.std(arrays, axis=1).tolist(), np.std(arrays).item()],
            'max': [np.max(arrays, axis=0).tolist(), np.max(arrays, axis=1).tolist(), np.max(arrays).item()],
            'min': [np.min(arrays, axis=0).tolist(), np.min(arrays, axis=1).tolist(), np.min(arrays).item()],
            'sum': [np.sum(arrays, axis=0).tolist(), np.sum(arrays, axis=1).tolist(), np.sum(arrays).item()]
        }
    else:
        raise ValueError("List must contain nine numbers.")

    return calculations