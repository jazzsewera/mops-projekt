import numpy as np
import time


def idle(iterations, T):
    for i in range(iterations):
        print(f'Idle {i+1}/{iterations}')
        time.sleep(T)


def send(iterations, T):
    for i in range(iterations):
        # send data
        print(f'Sent packet {i+1}/{iterations}')
        time.sleep(T)


def main():
    T = 0.1  # state duration: 0.1s
    p_off = 0.7
    p_on = 0.3
    current_time = time.time_ns()
    end_time = current_time + 3e9  # simulation duration: 3s

    while current_time < end_time:
        off_iterations = np.random.geometric(p_off)
        idle(off_iterations, T)

        on_iterations = np.random.geometric(p_on)
        send(on_iterations, T)

        current_time = time.time_ns()


if __name__ == "__main__":
    main()
