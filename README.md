# Projekt MOPS

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
