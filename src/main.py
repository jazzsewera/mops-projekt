import logging as log
from simulator.rand import Rand
from simulator.timer import Timer
from simulator.state import SimulationTime
from simulator.state import GeneratorParameters


def on_state_handler():
    log.debug("On event fired")


def off_state_handler():
    log.debug("Off event fired")

def set_generator_parameters():
    GeneratorParameters.set_packet_length(input("Enter packet length: "))
    GeneratorParameters.set_generation_time(input("Enter generation time: "))
    GeneratorParameters.set_streams_number(input("Enter a number of streams: "))

def main():
    log.getLogger().setLevel(log.DEBUG)
    log.debug("Program started")

    set_generator_parameters()
    GeneratorParameters.get_packet_lenght()

    simulation_time = 5
    rand = Rand(0.5, 0.5)
    timer = Timer(rand, simulation_time)
    timer.register_on_event_handler(on_state_handler)
    timer.register_off_event_handler(off_state_handler)
    timer.print_on_event()
    timer.launch_timer_threads()


if __name__ == "__main__":
    main()
