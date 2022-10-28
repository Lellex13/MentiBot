from asyncio.windows_events import NULL
import threading
import time
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from unittest import result

from pynput import keyboard
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from win32api import GetSystemMetrics
from random_word import RandomWords
from string import ascii_letters
import undetected_chromedriver
from dhooks import Webhook
from msvcrt import getch
import pyautogui
from time import sleep
import ctypes
import sys
import os

os.system("cls")

code = input("Code: ")
text = input("Message: ")
times = int(input("Threads: "))
delay = int(input("Delay Between: "))
print()


def generate(self):
    self.DRIVER.get(self.URL)
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="enter-vote-key"]'))).send_keys(code)
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/form/button'))).click()
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/form/fieldset/div[1]/div/input'))).send_keys(text)
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/form/fieldset/div[2]/div/input'))).send_keys(text)
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/form/fieldset/div[3]/div/input'))).send_keys(text)
    WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/form/div/button/span[2]'))).click()

class Pro:
    def __init__(self):
        super(Pro, self).__init__()

        self.DRIVER = None
        self.DRIVERDIRECTORY = "chromedriver.exe"
        self.URL = f"https://www.menti.com/"
        
        self.DRIVERTIMEOUT = 86400
        self.DRIVERVERSION = 103
        self.DRIVERWINDOWSIZE = (450, 600)
        self.DRIVEROPTIONS = undetected_chromedriver.ChromeOptions()
        self.DRIVEROPTIONS.headless = True

        if not os.path.exists("chromedriver.exe"):
            undetected_chromedriver.install(executable_path="", target_version=self.DRIVERVERSION)
        self.DRIVER = undetected_chromedriver.Chrome(executable_path=self.DRIVERDIRECTORY, options=self.DRIVEROPTIONS)

        self.DRIVER.set_window_size(self.DRIVERWINDOWSIZE[0], self.DRIVERWINDOWSIZE[1])
        self.DRIVER.set_window_position((round(GetSystemMetrics(0) / 2) - round(self.DRIVERWINDOWSIZE[0] / 2)), (round(GetSystemMetrics(1) / 2) - round(self.DRIVERWINDOWSIZE[1] / 2)))

        print("[!] Sent vote")
        generate(self)

        self.DRIVER.close()

if __name__ == '__main__':
    threads = []
    for i in range(times):
        # determine the indices of the list this thread will handle
        start = i * len(str(times))
        # special case on the last chunk to account for uneven splits
        end = None if i+1 == times else (i+1) * len(str(times))
        # create the thread
        threads.append(
            threading.Thread(target=Pro))
        threads[-1].start()
        Sleep(int(delay))
exit()
