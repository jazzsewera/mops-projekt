import logging as log
from simulator.timer import Timer


def on_state_handler():
    log.debug("On event fired")

def off_state_handler():
    log.debug("Off event fired")

def main():
    log.getLogger().setLevel(log.DEBUG)

    log.debug("Program started")
    simulation_time = 5
    p_on = 0.7
    p_off = 0.3
    timer = Timer(simulation_time, p_on, p_off)
    timer.register_on_event_handler(on_state_handler)
    timer.register_off_event_handler(off_state_handler)
    timer.print_on_event()
    timer.launch_timer_threads()

if __name__ == "__main__":
    main()
