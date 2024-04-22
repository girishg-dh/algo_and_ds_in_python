import binary_search

class TimeStamp:
    def __init__(self) -> None:
        self.value_dict = {}
        self.timestamps = {}

    def set_value(self, key, value, timestamp):
        if key not in self.value_dict:
            self.value_dict[key] = [value]  # list of value
            self.timestamps[key] = [timestamp]  # list of timestamp
            return
        else:
            