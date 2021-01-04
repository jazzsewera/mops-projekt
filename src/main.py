import logging as log

from simulator.packet_generator import PacketGenerator
from simulator.queue import Queue
from simulator.state import GeneratorParameters
from simulator.timer import Timer


def set_generator_parameters():
    GeneratorParameters.set_packet_length(input("Enter packet length: "))
    GeneratorParameters.set_generation_time(input("Enter generation time: "))
    GeneratorParameters.set_streams_number(input("Enter a number of streams: "))


def main():
    log.getLogger().setLevel(log.DEBUG)
    log.debug("Program started")

    set_generator_parameters()

    simulation_time = 50
    timer = Timer(simulation_time)
    queue_one = Queue(timer, GeneratorParameters.get_packet_length())
    timer.add_clock_event_listener(queue_one.queue_packet_listener)

    generator_pool = []

    for _ in range(GeneratorParameters.get_streams_number()):
        generator = PacketGenerator(
            timer, queue_one, GeneratorParameters.get_packet_length(), 1
        )
        timer.add_clock_event_listener(generator.generator_event_listener)
        generator_pool.append(generator)

    timer.start_timer_event_loop()

    print(queue_one.packets_number)
    print(queue_one.packets)


if __name__ == "__main__":
    main()
