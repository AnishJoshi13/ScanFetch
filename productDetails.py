import pandas as pd
from Utils.extractImage import duckduckgo_image_search
from Utils.getDescription import search_and_extract_combined_descriptions

# Read data from Excel
file_path = 'SampleInput/product_titles.xlsx'
df = pd.read_excel(file_path)

# Extract product titles
product_titles = df['Product Title'].tolist()

# Initialize lists to store image URLs and descriptions
image_urls = []
product_descriptions = []

# Process each product title
for product in product_titles:
    # Extract three image URLs for each product
    product_image_urls = duckduckgo_image_search(product)
    image_urls.append(product_image_urls)

    # Extract product description
    product_description = search_and_extract_combined_descriptions(product)
    product_descriptions.append(product_description)
    print('.', end='', sep='')

# Update DataFrame with image URLs and descriptions
df['Image URLs 1'] = [urls[0] if len(urls) > 0 else '' for urls in image_urls]
df['Image URLs 2'] = [urls[1] if len(urls) > 1 else '' for urls in image_urls]
df['Image URLs 3'] = [urls[2] if len(urls) > 2 else '' for urls in image_urls]
df['Product Descriptions'] = product_descriptions

# Save to a new Excel file
output_file_path = 'SampleOutput/product_details.xlsx'
df.to_excel(output_file_path, index=False)
