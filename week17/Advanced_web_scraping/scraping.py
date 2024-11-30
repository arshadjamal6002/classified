# open google

# search arshadjamal 

# open leanwith
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the ChromeDriver executable
s = Service("C:/Users/arsha/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open the MonkeyType website
driver.get("https://monkeytype.com")

# Wait for the cookies accept button to be clickable
try:
    # Wait for the accept cookies button to be visible and clickable
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/dialog[2]/div[2]/div[2]/div[2]/button[1]"))
    )
    accept_button.click()
    print("Cookies accepted successfully!")
except Exception as e:
    print("Error while accepting cookies:", e)

# Wait for the word container to load
try:
    word_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "words"))
    )
    print("Word container loaded!")
except Exception as e:
    print("Error while waiting for word container:", e)
    driver.quit()
    exit()

# Fetch all words to type
try:
    words = word_container.find_elements(By.CLASS_NAME, "word")
    text_to_type = " ".join(word.text for word in words)
    print("Text to type:", text_to_type)
except Exception as e:
    print("Error while fetching words:", e)
    driver.quit()
    exit()

# Start typing dynamically
try:
    # Loop through each word dynamically as they load
    while True:
        # Locate the current active word
        active_word = word_container.find_element(By.CLASS_NAME, "word.active")
        
        # Extract all the letters in the active word
        letters = active_word.find_elements(By.TAG_NAME, "letter")
        
        # Type each letter one by one
        for letter in letters:
            char = letter.text  # Get the letter to type
            if char:  # Ensure the character is not empty
                driver.find_element(By.TAG_NAME, "body").send_keys(char)
                time.sleep(0.05)  # Mimic human typing speed
        
        # Press space after finishing a word
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)
        time.sleep(0.05)  # Small delay to match real typing

except Exception as e:
    print("Error during typing:", e)
# Wait for a while so we can observe the typing on the screen
input("Press Enter to close the browser...")

# Close the browser when done
driver.quit()












# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Path to the ChromeDriver executable
# s = Service("C:/Users/arsha/Downloads/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=s)

# # Open the MonkeyType website
# driver.get("https://monkeytype.com")

# # Maximize the browser window
# driver.maximize_window()

# # Accept cookies
# try:
#     accept_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/dialog[2]/div[2]/div[2]/div[2]/button[1]"))
#     )
#     accept_button.click()
#     print("Cookies accepted successfully!")
# except Exception as e:
#     print("Error while accepting cookies:", e)

# # Wait for the word container to load
# try:
#     word_container = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "words"))
#     )
#     print("Word container loaded!")
# except Exception as e:
#     print("Error while waiting for word container:", e)
#     driver.quit()
#     exit()

# # Fetch all words to type
# try:
#     words = word_container.find_elements(By.CLASS_NAME, "word")
#     text_to_type = " ".join(word.text for word in words)
#     print("Text to type:", text_to_type)
# except Exception as e:
#     print("Error while fetching words:", e)
#     driver.quit()
#     exit()

# # Simulate typing
# try:
#     typing_area = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "body"))  # Typing is done globally on the page
#     )
#     for char in text_to_type:
#         typing_area.send_keys(char)
#         time.sleep(0.05)  # Adjust to mimic human typing speed
# except Exception as e:
#     print("Error while typing:", e)

# # Observe the result before closing the browser
# input("Press Enter to close the browser...")

# # Close the browser
# driver.quit()
