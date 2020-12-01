Title: Model symulacji — raport częściowy — Projekt MOPS
Author: Błażej Sewera, Mateusz Winnicki, Wojciech Kowalski
Date: 1 grudnia 2020
Language: pl
Geometry: margin=2.2cm

# Projekt MOPS

## Cele projektu
Celem projektu jest zasymulowanie węzła lub systemu dwóch węzłów sieciowych,
obsługujących $n$ źródeł ruchu typu ON-OFF, zdolnych generować pakiety o
stałej długości $L$ w stanie ON.

Każdy węzeł sieciowy modelujemy jako nieskończoną kolejkę FIFO, każdy ma
podłączoną dowolną liczbę źródeł ruchu.

Liczba pakietów w stanie ON jest opisywana rozkładem geometrycznym o funkcji
rozkładu prawdopodobieństwa:
$$
n_{ON} = (1-p_{ON})^{k-1} p_{ON}
$$
$$
n_{ONavg} = \frac{1}{p_{ON}}
$$
gdzie $n_{ON}$ to liczba pakietów przesłana w jednej iteracji stanu ON.
Odstęp między pakietami (czas interwału) jest stały i wynosi $t_{int}$.

Wtedy średni czas trwania stanu ON:
$$
t_{ONavg} = \frac{t_{int}}{p_{ON}} + t_{prog}
$$
gdzie $t_{prog}$ to dodatkowy czas wprowadzany przez ograniczenia narzędzi
programistycznych, implementacji i sprzętu, który dla uproszczenia pominiemy.

Średnia liczba bitów wysłanych przez źródło podczas jednego stanu ON wynosi:
$$
n_{b\,avg} = \frac{L}{p_{ON}}
$$

Długość stanu OFF opisana jest rozkładem wykładniczym.
$$
t_{OFF} = \lambda e^{-\lambda t}
$$
$$
t_{OFFavg} = \frac{1}{\lambda}
$$

Dla uproszczenia, można posłużyć się podobnym rozkładem geometrycznym dla
długości stanu OFF, tylko w odróżnieniu od stanu ON, nie symulujemy wysyłania
pakietów, a jedynie uwzględniamy interwał pomiędzy kolejnymi iteracjami tego
stanu, czyli de facto bezczynnością.
$$
t_{OFFavg} = \frac{1}{p_{OFF}} \cdot t_{int}
$$

Z racji że stany ON i OFF następują naprzemiennie, średni czas trwania tych dwóch stanów:
$$
t_{ON\,OFF\,avg} = \frac{t_{int}}{p_{ON}} + \frac{t_{int}}{p_{OFF}} = \frac{t_{int} \cdot (p_{ON} + p_{OFF})}{p_{ON} \cdot p_{OFF}}
$$

Na podstawie powyższych danych można obliczyć średnią przepływność generowaną przez jedno źródło:
$$
BR_{avg} = \frac{n_{b}}{t_{ON\,OFF\,avg}} = \frac{L p_{ON} p_{OFF}}{t_{int} p_{ON} (p_{ON} + p_{OFF})}
$$

Badane metryki pomiarowe:
- średnia liczba pakietów w kolejce $l_{queue}$
- średni czas oczekiwania w kolejce $t_{wait}$
- średnie opóźnienie przekazu pakietu, definiowane jako średnia suma czasu
  oczekiwania w kolejce oraz czasu odebrania całego pakietu przez węzeł
  sieciowy. Jako że długość pakietu jest stała i wynosi L, czas odebrania
  pakietu przez węzeł również będzie stały $t_{delay} = t_{wait} + T_{receive}$
- średnie obciążenie serwera

Przedstawiony model zaimplementujemy w języku programowania Python.

## Scenariusz i algorytmy

```
napływ klientów -> kolejka -> serwer

nadawca \                       / odbiorca
nadawca -> kolejka z serwerem <-  odbiorca
nadawca /                       \ odbiorca
```

Automat przedstawiający nadawcę ON/OFF

Jeden stan będzie trwał T (np. 0.01s)

```
    (default)
        |
 <choose_state()>
    /       \
  (ON)     (OFF)
    |       |
/send()/  /idle()/
    \       /
    (default)
```

```python
import numpy as np
import random

T = 0.01  # stan trwa 0.01s

def choose_state():
    if bool(random.getrandbits(1)):
        send()
    else:
        idle()

def send():
    duration = np.random.exponential(scale=1)
    iterations = int(1/T * duration)
    for iterations:
        # send data
        sleep(T)

def idle():
    duration = np.random.exponential(scale=1)
    iterations = int(1/T * duration)
    for iterations:
        sleep(T)
```
