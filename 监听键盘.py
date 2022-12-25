from pynput import keyboard


def on_press(key):
    try:
        print('正在按压:{0}'.format(key.char))
    except AttributeError:
        print('正在按压:{0}'.format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


while True:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()