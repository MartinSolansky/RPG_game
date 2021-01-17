import time
import pdb


def slow_print(string, delay=.02, blick=False):
    """Print as it was some human"""
    for letter in string:
        time.sleep(delay)
        print(letter, end='', flush=True)
    if blick:
        return
    print('\r')


def blick_print(string, repetition=5):
    """Blicking print on the same row"""
    blank_line = " " * len(string)
    for i in range(1, repetition):
        slow_print('\r' + string, blick=True)
        time.sleep(1)
        slow_print('\r' + blank_line, blick=True, delay=0)
    slow_print('\r' + string)


if __name__ == '__main__':
    text = "Thug did 2 dmg by dagger to M. And he got {} HP remaining."
    blick_print(text, repetition=3)
    print("END")
    slow_print(text)