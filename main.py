import webbrowser
from PIL import ImageGrab
import pyautogui
from time import sleep


def main():
    # Go to the related website to play dinosaur game
    webbrowser.open_new_tab("https://elgoog.im/t-rex/")
    # wait for 5 seconds to load it
    sleep(5)
    # Start the game by pressing space
    pyautogui.press("space")

    on = True
    while on:
        # Get full screen as an image
        screen = ImageGrab.grab(xdisplay="")

        # Few pixels in front of dinosaur's nose
        mouth_pixel_color = screen.getpixel(xy=(1342, 471))
        # Few pixels in front of dinosaur's hands
        hands_pixel_color = screen.getpixel(xy=(1337, 479))

        # If mouth pixel or hands pixels turn to black press space using pyautogui
        if mouth_pixel_color == (83, 83, 83) or hands_pixel_color == (83, 83, 83):
            pyautogui.press("space")

            if mouth_pixel_color == (83, 83, 83):
                print(f"mouth pixel {mouth_pixel_color}")
            elif hands_pixel_color == (83, 83, 83):
                print(f"hands pixel {hands_pixel_color}")


main()
