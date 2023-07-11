from examples.slowdown import apiCall, DataSet

def func_slow():
    apiresponse = apiCall()
    return apiresponse

def func_slowdown():
    dataset = DataSet()
    return dataset.data_loader()

def num_return():
    r_val = DataSet()
    return r_val.return_val()

def static_return():
    stat = DataSet()
    return stat.static_return()