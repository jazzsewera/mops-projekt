import logging as log

from simulator.packet_generator import PacketGenerator
from simulator.queue import Queue
from simulator.state import GeneratorParameters
from simulator.timer import Timer


def set_generator_parameters():
    GeneratorParameters.set_packet_length(input("Enter packet length: "))
    GeneratorParameters.set_generation_time(input("Enter generation time: "))
    GeneratorParameters.set_streams_number(input("Enter a number of streams: "))
    GeneratorParameters.set_dropped_streams(input("Enter number of streams dropped after leaving first queue:")) # TODO assertion that dropped streams < all streams


def main():
    log.getLogger().setLevel(log.DEBUG)
    log.debug("Program started")

    set_generator_parameters()

    simulation_time = 50
    timer = Timer(simulation_time)
    queue_two = Queue(timer, GeneratorParameters.get_packet_length())
    queue_one = Queue(timer, GeneratorParameters.get_packet_length(), queue_two)
    timer.add_clock_event_listener(queue_one.queue_packet_listener)
    timer.add_clock_event_listener(queue_two.queue_packet_listener)

    generator_pool = []

    dropped_number = GeneratorParameters.get_dropped_streams()

    for _ in range(GeneratorParameters.get_streams_number()):
        if GeneratorParameters.get_dropped_streams() > 0:
            generator = PacketGenerator(
                timer, queue_one, GeneratorParameters.get_packet_length(), 1, False
            )
            timer.add_clock_event_listener(generator.generator_event_listener)
            generator_pool.append(generator)
            GeneratorParameters.set_dropped_streams(GeneratorParameters.get_dropped_streams() - 1)
        else:
            generator = PacketGenerator(
                timer, queue_one, GeneratorParameters.get_packet_length(), 1, True
            )
            timer.add_clock_event_listener(generator.generator_event_listener)
            generator_pool.append(generator)

    for _ in range(dropped_number):
        generator = PacketGenerator(
            timer, queue_two, GeneratorParameters.get_packet_length(), 1, True
        )
        timer.add_clock_event_listener(generator.generator_event_listener)
        generator_pool.append(generator)

    timer.start_timer_event_loop()

    print("queue one data:")
    print(queue_one.packets_number)
    print(queue_one.packets)
    print(queue_one.packets_passed)
    print("queue two data:")
    print(queue_two.packets_number)
    print(queue_two.packets)
    print(queue_two.packets_passed)

if __name__ == "__main__":
    main()
