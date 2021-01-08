import argparse
import json

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
parser.add_argument(
    "-o", "--outfolder", help="Output (plot) folder", type=str, required=True
)
args = parser.parse_args()

data = []

with open(args.filename, "r") as in_file:
    for line in in_file.readlines():
        data.append(json.loads(line))

names = {
    "avg_queue_length_Q1": "Średnia liczba pakietów w kolejce pierwszej",
    "avg_queue_waiting_time_Q1": "Średni czas oczekiwania w kolejce pierwszej [s]",
    "avg_delay_Q1": "Średnie opóźnienie przekazu pakietu w kolejce pierwszej [s]",
    "avg_load_Q1": "Średnie obciążenie serwera pierwszego",
    "packets_passed_Q1": "Pakiety obsłużone przez pierwszy węzeł",
    "avg_queue_length_Q2": " Średnia liczba pakietów w kolejce drugiej",
    "avg_queue_waiting_time_Q2": "Średni czas oczekiwania w kolejce drugiej [s]",
    "avg_delay_Q2": "Średnie opóźnienie przekazu pakietu w kolejce drugiej [s]",
    "avg_load_Q2": "Średnie obciążenie serwera drugiego",
    "packets_passed_Q2": "Pakiety obsłużone przez drugi węzeł",
}

for k, _ in names.items():
    legend = []
    for i in range(1, 11):
        xs = [
            d["simulation_params"]["lambda_on"]
            for d in sorted(data, key=lambda x: x["simulation_params"]["lambda_on"])
            if d["simulation_params"]["lambda_off"] == i
        ]

        ys = [
            d[k]
            for d in sorted(data, key=lambda x: x["simulation_params"]["lambda_on"])
            if d["simulation_params"]["lambda_off"] == i
        ]

        plt.plot(xs, ys)
        legend.append(
            r"$\lambda_{off}$ = " f"{i}",
        )
    plt.title(names[k])
    plt.xlabel(r"$\lambda_{on}$")
    plt.legend(legend)
    plt.savefig(f"{args.outfolder}/{k}.png")
    plt.clf()
