import argparse
import json

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
args = parser.parse_args()

data = []

with open(args.filename, "r") as in_file:
    for line in in_file.readlines():
        data.append(json.loads(line))

names = {
    "avg_queue_length_Q1": "Średnia liczba pakietów w kolejce pierwszej",
    "avg_queue_waiting_time_Q1": "Średni czas oczekiwania w kolejce pierwszej",
    "avg_delay_Q1": "Średnie opóźnienie przekazu pakietu w kolejce pierwszej",
    "avg_load_Q1": "Średnie obciążenie serwera pierwszego",
    "packets_passed_Q1": "Pakiety obsłużone przez pierwszy węzeł",
    "avg_queue_length_Q2": " Średnia liczba pakietów w kolejce drugiej",
    "avg_queue_waiting_time_Q2": "Średni czas oczekiwania w kolejce drugiej",
    "avg_delay_Q2": "Średnie opóźnienie przekazu pakietu w kolejce drugiej",
    "avg_load_Q2": "Średnie obciążenie serwera drugiego",
    "packets_passed_Q2": "Pakiety obsłużone przez drugi węzeł",
}


xs_0 = [
    d["simulation_params"]["streams_number"]
    for d in data
    if d["simulation_params"]["dropped_streams"] == 0
]
xs_1 = [
    d["simulation_params"]["streams_number"]
    for d in data
    if d["simulation_params"]["dropped_streams"] == 1
]

ys_0 = [
    d["avg_queue_length_Q1"]
    for d in data
    if d["simulation_params"]["dropped_streams"] == 0
]
ys_1 = [
    d["avg_queue_length_Q1"]
    for d in data
    if d["simulation_params"]["dropped_streams"] == 1
]

plt.plot(xs_0, ys_0)
plt.plot(xs_1, ys_1)
plt.title(names["avg_queue_length_Q1"])
plt.show()
