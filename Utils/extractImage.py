from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def duckduckgo_image_search(query):
    service = Service('ThirdParty/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(f"https://duckduckgo.com/?q={query}&iax=images&ia=images")

        # Wait for the images to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tile--img__img")))

        # Find all image elements
        images = driver.find_elements(By.CLASS_NAME, "tile--img__img")

        # Extract image links
        image_links = [img.get_attribute('data-src') for img in images[:3]]
        return image_links
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    # Example usage
    query = "Rode Wireless GO II TX (698813010882)"
    image_links = duckduckgo_image_search(query)

    if image_links:
        print("Images found:")
        for image_link in image_links:
            print(image_link)
    else:
        print("No images found")
