import webbrowser
from PIL import ImageGrab
import pyautogui
from time import sleep


def main():
    # Go to the below website
    webbrowser.open_new("https://elgoog.im/t-rex/")
    # wait for 5 seconds to the website it
    sleep(5)
    # Start the game by pressing up key
    press("up")

    on = True
    while on:
        # Get full screen as an image
        screen = ImageGrab.grab()

        # Check for black pixel in between 1270 pixel in 1287
        for x in range(1270, 1287):
            # If there is a black pixel, press up key in keyboard
            if screen.getpixel((x, 480)) == (83, 83, 83):
                press("up")
                break


def press(key):
    pyautogui.press(key)


main()
