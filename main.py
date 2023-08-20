# Import required libraries
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Firefox setup
# Ensure GeckoDriver is properly set up on your OS before running this script.
# For setup details, refer to: https://www.browserstack.com/guide/geckodriver-selenium-python

# Specify the path to the Firefox profile
profile_path = r"C:\Users\david\AppData\Roaming\Mozilla\Firefox\Profiles\uzrys2hr.default-release"
options = Options()
# Configure the browser to start in headless mode
options.add_argument('--headless')
options.set_preference('profile', profile_path)
options.set_preference("javascript.enabled", False)
# Specify the path to the GeckoDriver executable
service = Service(r"C:\Users\david\PycharmProjects\pythonProject\geckodriver.exe")
# Specify the path to the Firefox binary
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
# Initialize the Firefox WebDriver with the configured options
driver = Firefox(service=service, options=options)

# Read URLs from an Excel file
df = pd.read_excel('cep_url_data.xlsx')
cep_link = df.values.tolist()
data_list = []

# Loop through each URL in the list
for _ in cep_link:
    # Combine the list elements to form a complete URL
    cep_string = "_".join(_)
    try:
        # Load the URL in the browser
        driver.get(cep_string)
        driver.set_page_load_timeout(10)  # Set a timeout for page loading
        current_url = driver.current_url  # Store the current URL

        # Extract various data elements from the page using CSS and XPATH selectors
        cep_element = driver.find_element(By.CSS_SELECTOR, "span[itemprop='postalCode']")
        cep = cep_element.text.strip()

        address_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[3]/span")
        address = address_element.text.strip()

        bairro_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[4]")
        bairro = bairro_element.text.strip()

        cidade_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[5]/span")
        cidade = cidade_element.text.strip()

        estado_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[7]/span")
        estado = estado_element.text.strip()

        full_address_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[9]")
        full_address = full_address_element.text.strip()

        lon_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[10]")
        lon = lon_element.text.strip()

        lat_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/p[11]")
        lat = lat_element.text.strip()

        # Store the extracted data into a dictionary
        data = {
            "CEP": cep,
            "Endereço": address,
            "Bairro": bairro,
            "Cidade": cidade,
            "Estado": estado,
            "Endereço completo": full_address,
            "Longitude": lon,
            "Latitude": lat
        }
        data_list.append(data)

        # Print the collected data and current URL
        print(data_list)
        print(current_url)
    except TimeoutException as e:
        # Handle TimeoutException: refresh the page and continue scraping
        print("Timeout occurred while loading the page:", e)
        print("Refreshing page:")
        driver.refresh()
        print("Page refreshed")
        print("Getting Current_URL")
        driver.get(current_url)
        print("Success")

# Create a DataFrame from the collected data
df = pd.DataFrame(data_list)

# Export the DataFrame to an Excel file
df.to_excel("scraped_data.xlsx", index=False, engine='openpyxl')

# Quit the browser
driver.quit()
