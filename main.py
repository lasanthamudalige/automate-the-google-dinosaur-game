from PIL import ImageGrab
import pyautogui
from time import sleep


def main():
    # wait for 5 seconds to load it
    sleep(5)
    # Start the game by pressing space
    pyautogui.press("up")

    on = True
    while on:
        # Get full screen as an image
        screen = ImageGrab.grab()

        # Few pixels in front of dinosaur's hands
        hands_pixel_color1 = screen.getpixel(xy=(1310, 462))
        hands_pixel_color2 = screen.getpixel(xy=(1310, 465))
        hands_pixel_color3 = screen.getpixel(xy=(1310, 467))
        hands_pixel_color4 = screen.getpixel(xy=(1310, 469))
        hands_pixel_color5 = screen.getpixel(xy=(1310, 472))
        hands_pixel_color4 = screen.getpixel(xy=(1310, 475))

        if hands_pixel_color1 == (83, 83, 83) or hands_pixel_color2 == (83, 83, 83) or hands_pixel_color3 == (83, 83, 83) or hands_pixel_color4 == (83, 83, 83):
            pyautogui.press("up")


main()
