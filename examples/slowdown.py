import time

def apiCall():
    time.sleep(3)
    return 9

class DataSet:

    def __init__(self):
        self.data = None
        self.num = None

    def data_loader(self):
        time.sleep(5)
        self.data = "slow down!"
    
    def return_val(self):
        time.sleep(3)
        self.num = 3

    @staticmethod
    def static_return():
        return "always this!!"