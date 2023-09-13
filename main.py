from pynput.keyboard import Key, Listener
import datetime


def on_press(key):
    now = datetime.datetime.now()
    print(f'{key} pressed.')
    log(now, key)


def log(time, key):
    with open('./log.txt', 'a') as f:
        f.write(f'{time}: {key} pressed\n')     


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()