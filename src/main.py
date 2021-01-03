import logging as log

from simulator.packet_generator import PacketGenerator
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
    GeneratorParameters.get_packet_length()

    simulation_time = 10
    timer = Timer(simulation_time)

    generator_pool = []

    for _ in range(GeneratorParameters.get_streams_number()):
        generator = PacketGenerator(timer, 1, 1)
        timer.add_clock_event_listener(generator.generator_event_listener)
        generator_pool.append(generator)

    timer.launch_timer_thread()
    timer.join_timer_thread()


if __name__ == "__main__":
    main()
