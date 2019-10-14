import pyautogui
import random
import time

keyboard_keys= [
	'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '('
		,')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7'
		,'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`'
		,'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
		,'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
		,'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace'
		,'browserback', 'browserfavorites', 'browserforward', 'browserhome'
		,'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear'
		,'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete'
		,'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10'
		,'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20'
		,'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
		,'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja'
		,'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail'
		,'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack'
		,'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6'
		,'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn'
		,'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn'
		,'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator'
		,'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab'
		,'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen'
		,'command', 'option', 'optionleft', 'optionright'
		];

actions= [ 

"pyautogui.scroll(random.randrange(-500,500))"  # scroll up or down
# ,"pyautogui.moveRel(random.randint(0,500), random.randint(0,500), random.randrange(0,10), pyautogui.easeInOutQuad)"  # move mouse, start slow, end fast
# ,"pyautogui.click(button=random.choice(['left','right']), clicks=random.choice(1,2,3))" #random clicking of mouse
# ,"pyautogui.dragRel(random.randrange(-200,200), random.randrange(-200,200), random.randrange(0, 3), button=random.choice(['left','right']))" # click and drag
# ,"pyautogui.press( random.choice( keyboard_keys ) )" # press random key
# ,"pyautogui.hotkey('ctrl', 'c')"  # ctrl-c to copy
# ,"pyautogui.hotkey('ctrl', 'v')"  # ctrl-v to paste
# ,"pyautogui.hotkey('ctrl', 'z')"  # ctrl-z to undo
# ,"pyautogui.hotkey('ctrl', 'f')"  # ctrl-f to search
# ,"pyautogui.typewrite('Robot')"  #type 'Robot'
# ,"pyautogui.press('enter')"  # hit enter (increase chances of pressing enter)
,"pyautogui.press(['backspace','backspace'] * random.randint(1,100))" # press backspace some random number of times
];

while True:
	time.sleep( random.randint( 0, 10) );
	# print( random.choice( keyboard_keys ) );
	
	eval(random.choice(actions));

