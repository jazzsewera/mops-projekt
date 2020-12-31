import logging as log
from mops.simulator.rand import Rand
from mops.simulator.timer import Timer


def on_state_handler():
    log.debug("On event fired")


def off_state_handler():
    log.debug("Off event fired")


def main():
    log.getLogger().setLevel(log.DEBUG)

    log.debug("Program started")
    simulation_time = 5
    rand = Rand(0.5, 0.5)
    timer = Timer(rand, simulation_time)
    timer.register_on_event_handler(on_state_handler)
    timer.register_off_event_handler(off_state_handler)
    timer.print_on_event()
    timer.launch_timer_threads()


if __name__ == "__main__":
    main()
