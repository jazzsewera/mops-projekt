from logger import Logger
from numpy import average

log = Logger(None)


def show_queue_length_average(number_of_packets):
    timestamps = []
    vals = []

    if len(number_of_packets) == 0:
        log.info(f"Average number of packets: NO DATA")
        return 0

    for k, v in number_of_packets.items():
        timestamps.append(float(k))
        vals.append(v)

    vals.pop()
    timedeltas = []

    for i in range(len(timestamps) - 1):
        timedeltas.append(timestamps[i + 1] - timestamps[i])

    av = average(vals, weights=timedeltas)

    log.info(f"Average number of packets: {av}")
    return av


def show_average_queue_waiting_time_Q1(sent_packets):
    ts = []

    if len(sent_packets) == 0:
        log.info(f"Average waiting time: NO DATA")
        return 0

    for packet in sent_packets:
        ts.append(packet.out_of_queue_time - packet.in_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average waiting time: {av}")
    return av


def show_average_delay_Q1(sent_packets):
    ts = []

    if len(sent_packets) == 0:
        log.info(f"Average delay time: NO DATA")
        return 0

    for packet in sent_packets:
        ts.append(packet.in_second_queue_time - packet.in_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average delay time: {av}")
    return av


def show_average_server_load_Q1(sent_packets):

    if len(sent_packets) == 0:
        log.info(f"Average server load: NO DATA")
        return 0

    av_service_time = (
        sent_packets[0].in_second_queue_time - sent_packets[0].out_of_queue_time
    )

    vals = []
    for i in range(len(sent_packets) - 1):
        vals.append(sent_packets[i + 1].in_queue_time - sent_packets[i].in_queue_time)

    if sum(vals) == 0 or len(vals) == 0:
        log.info(f"Average server load: NO DATA")
        return 0

    av_time_between_in_queue = sum(vals) / len(vals)

    influx = 1 / av_time_between_in_queue
    outflow = 1 / av_service_time

    av = influx / outflow
    log.info(f"Average server load: {av}")
    return av


def show_average_queue_waiting_time_Q2(sent_packets):
    ts = []

    if len(sent_packets) == 0:
        log.info(f"Average waiting time: NO DATA")
        return 0

    for packet in sent_packets:
        ts.append(packet.out_of_second_queue - packet.in_second_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average waiting time: {av}")
    return av


def show_average_delay_Q2(sent_packets):
    ts = []

    if len(sent_packets) == 0:
        log.info(f"Average delay time: NO DATA")
        return 0

    for packet in sent_packets:
        ts.append(packet.out_of_system_time - packet.in_second_queue_time)
    av = sum(ts) / len(ts)
    log.info(f"Average delay time: {av}")
    return av


def show_average_server_load_Q2(sent_packets):

    if len(sent_packets) == 0:
        log.info(f"Average server load: NO DATA")
        return 0

    av_service_time = (
        sent_packets[0].out_of_system_time - sent_packets[0].out_of_second_queue
    )
    vals = []
    for i in range(len(sent_packets) - 1):
        vals.append(
            sent_packets[i + 1].in_second_queue_time
            - sent_packets[i].in_second_queue_time
        )

    if sum(vals) == 0 or len(vals) == 0:
        log.info(f"Average server load: NO DATA")
        return 0

    av_time_between_in_queue = sum(vals) / len(vals)

    influx = 1 / av_time_between_in_queue
    outflow = 1 / av_service_time

    av = influx / outflow
    log.info(f"Average server load: {av}")
    return av
