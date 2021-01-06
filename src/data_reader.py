from logger import Logger

log = Logger(None)


def show_queue_length_average(number_of_packets):
    vals = []
    for _, v in number_of_packets.items():
        vals.append(v)

    av = sum(vals) / len(vals)
    log.info(f"Average number of packets: {av}")
    return av


def show_average_queue_waiting_time_Q1(sent_packets):
    ts = []
    for packet in sent_packets:
        ts.append(packet.out_of_queue_time - packet.in_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average waiting time: {av}")
    return av


def show_average_delay_Q1(sent_packets):
    ts = []
    for packet in sent_packets:
        ts.append(packet.in_second_queue_time - packet.in_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average delay time: {av}")
    return av


def show_average_server_load_Q1(sent_packets):

    av_service_time = (
        sent_packets[0].in_second_queue_time - sent_packets[0].out_of_queue_time
    )

    vals = []
    for i in range(len(sent_packets) - 1):
        vals.append(sent_packets[i + 1].in_queue_time - sent_packets[i].in_queue_time)

    av_time_between_in_queue = sum(vals) / len(vals)

    influx = 1 / av_time_between_in_queue
    outflow = 1 / av_service_time

    av = influx / outflow
    log.info(f"Average server load: {av}")
    return av


def show_average_queue_waiting_time_Q2(sent_packets):
    ts = []
    for packet in sent_packets:
        ts.append(packet.out_of_second_queue - packet.in_second_queue_time)

    av = sum(ts) / len(ts)
    log.info(f"Average waiting time: {av}")
    return av


def show_average_delay_Q2(sent_packets):
    ts = []
    for packet in sent_packets:
        ts.append(packet.out_of_system_time - packet.in_second_queue_time)
    av = sum(ts) / len(ts)
    log.info(f"Average delay time: {av}")
    return av


def show_average_server_load_Q2(sent_packets):

    av_service_time = (
        sent_packets[0].out_of_system_time - sent_packets[0].out_of_second_queue
    )
    vals = []
    for i in range(len(sent_packets) - 1):
        vals.append(
            sent_packets[i + 1].in_second_queue_time
            - sent_packets[i].in_second_queue_time
        )

    av_time_between_in_queue = sum(vals) / len(vals)

    influx = 1 / av_time_between_in_queue
    outflow = 1 / av_service_time

    av = influx / outflow
    log.info(f"Average server load: {av}")
    return av
