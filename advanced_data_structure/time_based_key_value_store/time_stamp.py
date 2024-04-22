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
            self.value_dict[key].append(value)
            self.timestamps[key].append(timestamp)
            return

    def get_value(self, key, timestamp):
        if key not in self.value_dict:
            return None
        elif timestamp < self.timestamps[key][0]:
            return None
        elif timestamp > self.timestamps[key][-1]:
            return self.value_dict[key][-1]
        else:
            index = binary_search.binary_search(self.timestamps[key], timestamp)
            return self.value_dict[key][index]