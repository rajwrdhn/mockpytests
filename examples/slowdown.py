import time

def apiCall():
    time.sleep(3)
    return 9

class DataSet:

    def __init__(self):
        self.data = None

    def data_loader(self):
        time.sleep(5)
        self.data = "slow down!"