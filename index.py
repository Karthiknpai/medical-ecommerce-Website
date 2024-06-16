from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get('https://nimble-horse-1b354a.netlify.app/')

# Maximize the window to ensure full scrolling
driver.maximize_window()


time.sleep(6)

link_text = 'Login'
login_link = driver.find_element(By.LINK_TEXT, link_text)
login_link.click()

time.sleep(2)
username_field = driver.find_element(By.NAME, 'username')
time.sleep(3)
password_field = driver.find_element(By.NAME, 'password')
time.sleep(2)

# Now you can interact with these elements, for example:
username_field.send_keys('user')
password_field.send_keys('password')

login_button = driver.find_element(By.CSS_SELECTOR, 'input[type=\"submit\" i]')
time.sleep(2)
login_button.click()


time.sleep(3)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://nimble-horse-1b354a.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0
    
    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)
    time.sleep(1)
    
    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment
    
    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")

time.sleep(5)


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'products')))

# Find the 'Stethoscope' product element
product_element = driver.find_element(By.XPATH, "//h2[text()='Face Mask']/..")

# Slowly scroll the product into view
driver.execute_script("""
    arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center'});
    """, product_element)

# Allow time for scrolling animation
time.sleep(2)

# Wait until the 'Buy Now' button is visible and clickable
buy_now_button = WebDriverWait(product_element, 10).until(
    EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Buy Now')]"))
)

# Click the 'Buy Now' button
buy_now_button.click()

# Wait for some time to see the result
time.sleep(2)  # Adjust time as needed

# Check if alert is present
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    if 'product-order placed successfully!' in alert_text:
        print("Order placed successfully!")
    else:
        print("Failed to place the Order..")
except:
    print("Product not found for order..")

time.sleep(2)



WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products"))
    )

    # Find the 'Face Mask' product
products = driver.find_elements(By.CLASS_NAME, "product")
for product in products:
        product_name = product.find_element(By.TAG_NAME, "h2").text
        if product_name == "Blood Bag":
            # Scroll to the product slowly
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", product)
            time.sleep(2)  # Wait for 2 seconds to ensure smooth scrolling

            # Click the 'Add to Cart' button
            add_to_cart_button = product.find_element(By.CLASS_NAME, "add-to-cart")
            add_to_cart_button.click()

            time.sleep(3)
            # Wait for the alert to appear
            WebDriverWait(driver, 10).until(EC.alert_is_present())

            # Handle the alert
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            # Verify the result
            if "product-added to cart!" in alert_text:
                print("Product added to cart successfully")
            else:
                print("Failed to add product to cart")
            
            break
else:
        print("Product not found")



top_element = driver.find_element(By.TAG_NAME, 'body')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", top_element)

# Keep the browser open for a while to observe the scrolling


time.sleep(2)


# try:
#     # Find all product elements
#     products = driver.find_elements(By.CLASS_NAME, 'product')

#     for product in products:
#         # Check if the product name is 'Face Mask'
#         product_name = product.find_element(By.TAG_NAME, 'h2').text
#         if product_name == 'Chloroprene gloves':
#             # Scroll to the product element slowly
#             actions = ActionChains(driver)
#             actions.move_to_element(product).perform()
#             time.sleep(1)  # Adjust the sleep time as needed

#             # Find the 'Add to Cart' button and click it
#             add_to_cart_button = product.find_element(By.CLASS_NAME, 'add-to-cart')
#             add_to_cart_button.click()

#             # Verify if the alert message is displayed
#             alert = driver.switch_to.alert
#             alert_text = alert.text
#             if 'Face Mask product-added to cart!' in alert_text:
#                 print("Product added to cart successfully")
#             else:
#                 print("Failed to add to cart")

#             alert.accept()
#             break

# except Exception as e:
#     print(f"An error occurred: {e}")
# time.sleep(3)


home_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, home_text)
home_link.click()

time.sleep(2)

about_text = 'About'
about_link = driver.find_element(By.LINK_TEXT, about_text)
about_link.click()

time.sleep(1)
page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
current_position = 0
    
while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.008)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)

    
    # Scroll back slowly to the top
while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.008)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment


home_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, home_text)
home_link.click()    

time.sleep(2)
contact_text = 'Contact'
contact_link = driver.find_element(By.LINK_TEXT, contact_text)
contact_link.click()    

time.sleep(2)

home_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, home_text)
home_link.click() 

time.sleep(2)

print('************************************************************')
print("Testing of Cure e-Commerce Website is successfully Done......")
print('************************************************************')

driver.quit()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'products')))

#     # Find the 'Stethoscope' product element
# product_element = driver.find_element(By.XPATH, "//h2[text()='Stethoscope']/..")

#     # Scroll the product into view
# driver.execute_script("arguments[0].scrollIntoView(true);", product_element)
# time.sleep(1)  # Allow time for scrolling animation

#     # Wait until the 'Buy Now' button is visible and clickable
# buy_now_button = WebDriverWait(product_element, 10).until(
#         EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Buy Now')]"))
#     )

#     # Click the 'Buy Now' button
# buy_now_button.click()

#     # Wait for some time to see the result
# time.sleep(2)  # Adjust time as needed

#     # Check if alert is present
# try:
#         WebDriverWait(driver, 10).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert_text = alert.text
#         alert.accept()
#         if 'product-order placed successfully!' in alert_text:
#             print("success")
#         else:
#             print("failed to click")
# except:
#         print("failed to click")
     
     














    
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product")))

#     # Find the product named "Face Mask"
# products = driver.find_elements(By.CLASS_NAME, "product")
# for product in products:
#         name = product.find_element(By.TAG_NAME, "h2").text
#         if name == "Stethoscope":
#             buy_now_button = product.find_element(By.CLASS_NAME, "buy-now")
#             buy_now_button.click()
#             break

#     # Wait for some time to observe the result (optional)
# time.sleep(2)

#     # Check if the alert is present
# try:
#         WebDriverWait(driver, 10).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#         print("Success: Clicked the 'Buy Now' button for 'Face Mask'")
# except:
#         print("Failed: Could not click the 'Buy Now' button for 'Face Mask'")    

# products = driver.find_elements(By.CLASS_NAME, "product")

# # Iterate over products to find the 'Face Mask' product
# for product in products:
#     product_name = product.find_element(By.TAG_NAME, "h2").text
#     if product_name == "Face Mask":
#         # Locate and click the 'Buy Now' button for the 'Face Mask' product
#         buy_now_button = product.find_element(By.CLASS_NAME, "buy-now")
#         buy_now_button.click()



# try:
#     # Wait up to 10 seconds for the dashboard URL or element indicating dashboard page
#     WebDriverWait(driver, 10).until(
#         EC.url_contains('https://nimble-horse-1b354a.netlify.app/products.html')  # Adjust condition based on your application
#         # You can also use other conditions like presence of specific elements on the dashboard
#     )
#     print("Login successful! Redirected to the dashboard.")
#     # Example: Navigate to the dashboard using its path
#     driver.get('https://nimble-horse-1b354a.netlify.app/products.html')
#     # You can add further actions on the dashboard here if needed

# except:
#     print("Login unsuccessful. Please check your credentials.")


# print("logged in succesfully")

# driver.get('https://nimble-horse-1b354a.netlify.app/products.html')


# try:
#     # Wait for the login form elements to load
#     username_field = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'username'))
#     )
#     password_field = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'password'))
#     )
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
#     )

#     # Example: Enter login credentials
#     username_field.send_keys('user')  # Replace with your username
# #     password_field.send_keys('password')  # Replace with your password
    
#     # Example: Click on the login button
#     login_button.click()
    # print("Clicked on the login button")

    # # Wait for login process (replace with appropriate waiting logic)
    # WebDriverWait(driver, 10).until(
    #     EC.url_changes(driver.current_url)
    # )
    
#     # Example: Perform actions after login, such as navigating to another page
#     driver.get('https://nimble-horse-1b354a.netlify.app/products.html')
    
# except Exception as e:
#     print(f"Login failed: {e}")






