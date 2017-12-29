import time


def draw_with_keyboard_interrupt(plt):
    plt.draw()
    plt.pause(1)
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            plt.close()
            break
