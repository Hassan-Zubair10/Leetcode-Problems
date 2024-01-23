class RequestLogger:
    def __init__(self, _time_limit):
        self.table = {}
        self.time_limit = _time_limit
        print("Time Limit:", self.time_limit)

    def message_request_decision(self, timestamp, request):
        if request not in self.table or timestamp - self.table[request] >= self.time_limit:
            self.table[request] = timestamp
            return True
        return False
