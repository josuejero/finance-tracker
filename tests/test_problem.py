import os
import subprocess
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def clear_file_content(file_path):
    with open(file_path, "w") as file:
        pass

def append_problem_message(file_path, problem_message):
    with open(file_path, "a") as file:
        file.write(f"{problem_message}\n\n")
        file.write("Please analyze this project structure, description, and errors carefully in order to help me with the issue.\n\n")

def run_subprocess(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def append_tree_output(file_path):
    tree_output = run_subprocess(["tree", "-I", "venv"])
    with open(file_path, "a") as file:
        file.write(tree_output)
        file.write("\n")

def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver
