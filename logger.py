import pyperclip
import pyautogui
import time
from datetime import datetime


def save_screenshot(window_title):
    screenshot_path = "D:/OneDrive/Backup/logger/screenshots/"
    date = datetime.now().date()
    time = datetime.now().strftime("%H-%M")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{screenshot_path}{date} {time} {window_title}.png")


def save_clipboard(window_title, clipboard_content):
    clipboard_path = "D:/OneDrive/Backup/logger/clipboard.txt"
    with open(clipboard_path, "a", encoding="utf-8") as f:
        f.write(f"{window_title}: {clipboard_content} \n")


def main():
    last_clipboard_content = ""
    screenshot_timer = time.time()

    while True:
        window_title = pyautogui.getActiveWindowTitle()

        if int(time.time() - screenshot_timer) > 60 * 2:
            save_screenshot(window_title)

        clipboard_content = pyperclip.paste() or ""

        if "" != clipboard_content != last_clipboard_content:
            save_clipboard(window_title, clipboard_content)
            last_clipboard_content = clipboard_content

        time.sleep(1)


main()
