import matplotlib.pyplot as plt
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
args = parser.parse_args()

data = []

with open(args.filename, "r") as in_file:
    for line in in_file.readlines():
        data.append(json.loads(line))

names = {'avg_queue_length_Q1': 'Średnia liczba pakietów w kolejce pierwszej',
           'avg_queue_waiting_time_Q1': 'Średni czas oczekiwania w kolejce pierwszej',
           'avg_delay_Q1': 'Średnie opóźnienie przekazu pakietu w kolejce pierwszej',
           'avg_load_Q1': 'Średnie obciążenie serwera pierwszego',
           'packets_passed_Q1': 'Pakiety obsłużone przez pierwszy węzeł',
           'avg_queue_length_Q2':' Średnia liczba pakietów w kolejce drugiej',
           'avg_queue_waiting_time_Q2': 'Średni czas oczekiwania w kolejce drugiej',
           'avg_delay_Q2': 'Średnie opóźnienie przekazu pakietu w kolejce drugiej',
           'avg_load_Q2': 'Średnie obciążenie serwera drugiego',
           'packets_passed_Q2': 'Pakiety obsłużone przez drugi węzeł'}

i = 0

for key, value in data[0].items():
  val = []
  if key == "simulation_params":
    continue
  print(key)
  tail_data = data[-10:]
  for measure in tail_data:
    val.append(measure[key])
    print(measure)
  plt.figure(i)
  plt.plot(range(len(val)), val)
  plt.title(names[key])
  plt.ylim([0, max(val)*1.1])
  plt.savefig(".\out\\" + key)
  #print(val)
  i += 1
