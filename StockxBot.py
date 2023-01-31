import webbrowser
import time
from pynput.mouse import Button, Controller

# Uses Mouse interaction

url = 'https://stockx.com'  # list of sites to visit array

m = Controller()  # assign m to the pynput mouse controller

webbrowser.open_new_tab(url)
time.sleep(3)

print('Current pointer position is {0}'.format(m.position))

# go to position of stock x search bar
m.position = (466.32421875, 170.66796875)
print('Now we have moved to the search bar {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)

time.sleep(2)

itemToSearch = "NikeCraft General Purpose Shoe"
m.press(Button.right)
m.release(Button.right)
m.position = (491.109375, 219.25)
print('Pasting Clipboard into search box {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)


m.position = (376.34375, 315.625)  # go to postition of item 1 of search result
print('Selected item number 1 of search result {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)

m.position = (850.046875, 482.80859375)  # select size dropdown
print('Opening Size dropdown menu {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)

time.sleep(2)
m.position = (896.45703125, 629.03125)  # select size e.g US 5.5W/4M - £110
print('Selected size picked{0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)

time.sleep(1)
m.position = (1001.4375, 547.37109375)  # select buy for x price
print('Clicking on Buy {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)

time.sleep(1)
m.position = (1105.24609375, 670.1015625)  # Clicks Next for x price
print('Processing to Checkout/Sign in page {0}'.format(m.position))
m.press(Button.left)
m.release(Button.left)


time.sleep(10)  # wait x sec

# k.press_keys(['Command', 'W'])  # close webpage using keyboard command
