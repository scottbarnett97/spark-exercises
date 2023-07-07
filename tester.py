import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time as t


def download_sql_files():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = "https://github.com/"
    repo_url = base_url + "scottbarnett97/database-exercises"

    # Set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    
    # Authenticate with GitHub
    driver.get(base_url + "login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME,"password").send_keys(pswd)
    driver.find_element(By.NAME,"commit").click()
    
    # Access the repository
    driver.get(repo_url)
    html_content = driver.page_source
    
    # Find all the SQL file links in the HTML content
    sql_file_links = re.findall(r'href="(.*\.sql)"', html_content)
    
    if sql_file_links:
        # Download each SQL file
        for link in sql_file_links:
            sql_file_url = base_url + link
            sql_file_name = link.split("/")[-1]
            
            # Download the SQL file using Selenium
            driver.get(sql_file_url)
            
            with open(sql_file_name, "wb") as file:
                file.write(driver.page_source.encode("utf-8"))
            
            print(f"Downloaded: {sql_file_name}")
    else:
        print("No SQL files found in the repository.")
    
    # Quit the web driver
    driver.quit()


def download_ipynb_files():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = "https://github.com/"
    repo_url = base_url + "scottbarnett97/python-exercises"

    # Set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    
    # Authenticate with GitHub
    driver.get(base_url + "login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME,"password").send_keys(pswd)
    driver.find_element(By.NAME,"commit").click()
    
    # Access the repository
    driver.get(repo_url)
    html_content = driver.page_source
    
    # Find all the IPython Notebook file links in the HTML content
    ipynb_file_links = re.findall(r'href="(.*\.ipynb)"', html_content)
    
    if ipynb_file_links:
        # Download each IPython Notebook file
        for link in ipynb_file_links:
            ipynb_file_url = base_url + link
            ipynb_file_name = link.split("/")[-1]
            
            # Download the IPython Notebook file using Selenium
            driver.get(ipynb_file_url)
            
            with open(ipynb_file_name, "wb") as file:
                file.write(driver.page_source.encode("utf-8"))
            
            print(f"Downloaded: {ipynb_file_name}")
    else:
        print("No IPython Notebook files found in the repository.")
    
    # Quit the web driver
    driver.quit()


if __name__ == "__main__":
    download_sql_files()
    download_ipynb_files()
