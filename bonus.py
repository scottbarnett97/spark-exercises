import os
import requests
import re

def download_sql_files():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = "https://github.com/"
    repo_url = base_url + "scottbarnett97/database-exercises"
    
    # Make a GET request to the repository URL
    response = requests.get(repo_url, auth=(user, pswd))
    
    if response.status_code == 200:
        # Extract the HTML content from the response
        html_content = response.text
        
        # Find all the SQL file links in the HTML content
        sql_file_links = re.findall(r'href="(.*\.sql)"', html_content)
        
        if sql_file_links:
            # Download each SQL file
            for link in sql_file_links:
                sql_file_url = base_url + link
                sql_file_name = link.split("/")[-1]
                
                # Send a GET request to download the SQL file
                sql_file_response = requests.get(sql_file_url, auth=(user, pswd))
                
                if sql_file_response.status_code == 200:
                    # Save the SQL file to disk
                    with open(sql_file_name, "wb") as file:
                        file.write(sql_file_response.content)
                    
                    print(f"Downloaded: {sql_file_name}")
                else:
                    print(f"Failed to download: {sql_file_name}")
        else:
            print("No SQL files found in the repository.")
    else:
        print("Failed to access the repository.")


def download_ipynb_files():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = "https://github.com/"
    repo_url = base_url + "scottbarnett97/python-exercises"
    
    # Make a GET request to the repository URL
    response = requests.get(repo_url, auth=(user, pswd))
    
    if response.status_code == 200:
        # Extract the HTML content from the response
        html_content = response.text
        
        # Find all the IPython Notebook file links in the HTML content
        ipynb_file_links = re.findall(r'href="(.*\.ipynb)"', html_content)
        
        if ipynb_file_links:
            # Download each IPython Notebook file
            for link in ipynb_file_links:
                ipynb_file_url = base_url + link
                ipynb_file_name = link.split("/")[-1]
                
                # Send a GET request to download the IPython Notebook file
                ipynb_file_response = requests.get(ipynb_file_url, auth=(user, pswd))
                
                if ipynb_file_response.status_code == 200:
                    # Save the IPython Notebook file to disk
                    with open(ipynb_file_name, "wb") as file:
                        file.write(ipynb_file_response.content)
                    
                    print(f"Downloaded: {ipynb_file_name}")
                else:
                    print(f"Failed to download: {ipynb_file_name}")
        else:
            print("No IPython Notebook files found in the repository.")
    else:
        print("Failed to access the repository.")


if __name__ == "__main__":
    download_sql_files()
    download_ipynb_files()
