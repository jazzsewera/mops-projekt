class Packet:
    def __init__(self, start_time):
        self.sending_time = start_time
        self.in_queue_time = 0
        self.out_of_queue_time = 0
        self.in_second_queue_time = 0
        self.out_of_second_queue = 0

    def __repr__(self):
        return str(self.sending_time) + " " + str(self.in_queue_time) + " " + str(self.out_of_queue_time) + " " + str(self.in_second_queue_time) + " " + str(self.out_of_second_queue)