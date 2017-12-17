import time

import matplotlib.pyplot as plt


def handle_keyboard_interrupt():
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            plt.close()
            break
