
import pyautogui  # pip install pyautogui
import time
import schedule   # pip install schedule

def refresh_page():
    pyautogui.press('q')
    pyautogui.hotkey('command', 'r')
    time.sleep(60)
    pyautogui.press('q')

def main():
    time.sleep(5)  # Wait for 5 seconds
    refresh_page()
    schedule.every().hour.do(refresh_page)  # Back to running every hour

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
