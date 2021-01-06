class Packet:
    def __init__(self, in_queue_time, is_passing):
        self.in_queue_time = in_queue_time
        self.out_of_queue_time = 0.0
        self.in_second_queue_time = 0.0
        self.out_of_second_queue = 0.0
        self.out_of_system_time = 0.0
        self.is_passing = is_passing

    def __repr__(self):
        return (
            f"{self.in_queue_time:.2f} {self.out_of_queue_time:.2f} "
            f"{self.in_second_queue_time:.2f} {self.out_of_second_queue:.2f} "
            f"{self.out_of_system_time:.2f} "
            f"{'PASSING' if self.is_passing else 'NOT PASSING'}"
        )
