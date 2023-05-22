from examples.slowdown import apiCall, DataSet

def func_slow():
    apiresponse = apiCall()
    return apiresponse

def func_slowdown():
    dataset = DataSet()
    return dataset.data_loader()
