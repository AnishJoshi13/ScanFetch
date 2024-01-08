from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def search_and_extract_combined_descriptions(product_name):
    service = Service('ThirdParty/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Search for product description on DuckDuckGo
        search_query = f"{product_name} product description"
        duckduckgo_url = f"https://www.duckduckgo.com/?q={search_query}"
        driver.get(duckduckgo_url)

        # Extract the description elements for the first and second search results
        first_description_element = driver.find_element(By.XPATH,
                                                        '(//div[@data-result="snippet"]//span[contains(@class, "kY2IgmnCmOGjharHErah")])[1]')
        second_description_element = driver.find_element(By.XPATH,
                                                         '(//div[@data-result="snippet"]//span[contains(@class, "kY2IgmnCmOGjharHErah")])[2]')

        # Extract the description texts
        first_description_text = first_description_element.text
        second_description_text = second_description_element.text

        # Combine descriptions
        combined_descriptions = first_description_text + "\n" + second_description_text
        return combined_descriptions

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    product_name = "Realme GT5 Pro 5G (RMX3888) (1TB+16GB, Orange) (China Spec)"
    search_and_extract_combined_descriptions(product_name)
