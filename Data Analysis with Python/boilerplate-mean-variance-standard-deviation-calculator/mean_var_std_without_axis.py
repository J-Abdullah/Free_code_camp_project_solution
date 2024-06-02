import numpy as np

def calculate(list):
    mean_0,mean_1=[],[]
    v_0,v_1=[],[]
    std_0,std_1=[],[]
    min_0,min_1=[],[]
    max_0,max_1=[],[]
    sum_0,sum_1=[],[]
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    list=np.array(list)
    a2d=list.reshape((3,3))
    for i in range(3):
        mean_0.append(np.mean(a2d[i]))
        mean_1.append(np.mean(a2d[:,i]))
        v_0.append(np.var(a2d[i]))
        v_1.append(np.var(a2d[:,i]))
        std_0.append(np.std(a2d[i]))
        std_1.append(np.std(a2d[:,i]))
        min_0.append(np.min(a2d[i]))
        min_1.append(np.min(a2d[:,i]))
        max_0.append(np.max(a2d[i]))
        max_1.append(np.max(a2d[:,i]))
        sum_0.append(np.sum(a2d[i]))
        sum_1.append(np.sum(a2d[:,i]))

    calculations={
  'mean': [mean_1,mean_0 , np.mean(a2d)],
  'variance': [v_1,v_0 , np.var(a2d)],
  'standard deviation': [std_1,std_0 , np.std(a2d)],
  'max': [max_1,max_0 , np.max(a2d)],
  'min': [min_1,min_0 , np.min(a2d)],
  'sum': [sum_1,sum_0 , np.sum(a2d)]
}

    return calculations
    

