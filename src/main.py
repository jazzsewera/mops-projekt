import logging as log
from typing import List

from data_reader import *
from simulator.event_queue import EventQueue
from simulator.packet_generator import PacketGenerator
from simulator.queue import Queue
from simulator.state import GeneratorParameters
from simulator.timer import Timer

try:
    from colorlog import ColoredFormatter
except:
    print(
        "Install dependencies, e.g. from requirements.txt from the repo root\n\n"
        "$ pip3 install -r requirements.txt\n"
    )
    exit(2)


def set_generator_parameters():
    GeneratorParameters.set_packet_length(input("Enter packet length: "))
    GeneratorParameters.set_generation_time(input("Enter generation time: "))
    GeneratorParameters.set_streams_number(input("Enter a number of streams: "))
    GeneratorParameters.set_dropped_streams(
        input("Enter number of streams dropped after leaving first queue: ")
    )
    if (
        GeneratorParameters.get_streams_number()
        <= GeneratorParameters.get_dropped_streams()
    ):
        log.error(
            "The number of dropped streams has to be lower than "
            "the number of streams going into the first queue"
        )
        exit(1)


def main():
    LOGFORMAT = (
        "%(log_color)s%(levelname)-5s%(reset)s | %(log_color)s%(message)s%(reset)s"
    )
    LOGLEVEL = log.DEBUG
    log.getLogger().setLevel(LOGLEVEL)
    formatter = ColoredFormatter(LOGFORMAT)
    stream = log.StreamHandler()
    stream.setLevel(LOGLEVEL)
    stream.setFormatter(formatter)
    log.getLogger().addHandler(stream)
    log.debug("Program started")

    set_generator_parameters()

    simulation_time = 50
    timer = Timer()
    event_queue = EventQueue(timer)
    queue_two = Queue(timer, GeneratorParameters.get_packet_length())
    queue_one = Queue(timer, GeneratorParameters.get_packet_length(), queue_two)

    generator_pool: List[PacketGenerator] = []

    dropped_number = GeneratorParameters.get_dropped_streams()

    for _ in range(GeneratorParameters.get_streams_number()):
        if GeneratorParameters.get_dropped_streams() > 0:
            generator = PacketGenerator(
                timer,
                event_queue,
                queue_one,
                GeneratorParameters.get_packet_length(),
                GeneratorParameters.get_generation_time(),
                False,
            )
            generator_pool.append(generator)
            GeneratorParameters.set_dropped_streams(
                GeneratorParameters.get_dropped_streams() - 1
            )
        else:
            generator = PacketGenerator(
                timer,
                event_queue,
                queue_one,
                GeneratorParameters.get_packet_length(),
                GeneratorParameters.get_generation_time(),
                True,
            )
            generator_pool.append(generator)

    for _ in range(dropped_number):
        generator = PacketGenerator(
            timer,
            event_queue,
            queue_two,
            GeneratorParameters.get_packet_length(),
            GeneratorParameters.get_generation_time(),
            True,
        )
        generator_pool.append(generator)

    while timer.current_time < simulation_time:
        log.debug(f"@{timer.current_time}")
        for generator in generator_pool:
            generator.generate_packet()
        while event_queue.handle_event():
            pass

    log.debug("queue one data:")
    log.debug(queue_one.packets_number)
    log.debug(queue_one.packets)
    log.debug(queue_one.packets_passed)
    show_queue_length_average(queue_one.packets_number)
    show_average_queue_waiting_time_Q1(queue_one.packets_passed)
    show_average_delay_Q1(queue_one.packets_passed)
    show_average_server_load_Q1(queue_one.packets_passed)

    log.debug("queue two data:")
    log.debug(queue_two.packets_number)
    log.debug(queue_two.packets)
    log.debug(queue_two.packets_passed)
    show_queue_length_average(queue_two.packets_number)
    show_average_queue_waiting_time_Q2(queue_two.packets_passed)
    show_average_delay_Q2(queue_two.packets_passed)
    show_average_server_load_Q2(queue_two.packets_passed)


if __name__ == "__main__":
    main()
