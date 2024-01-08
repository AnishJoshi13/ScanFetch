import re


def extract_barcode(product_title):
    barcode_pattern = r'\((\d+)\)$'  # Regex pattern to match digits within brackets at the end
    match = re.search(barcode_pattern, product_title)

    if match:
        barcode = match.group(1)  # Extract the barcode from the match
        return barcode
    else:
        return None


# Example usage:
if __name__ == '__main__':
    product_title = "Rode Wireless GO II TX (698813010882)"
    barcode = extract_barcode(product_title)

    if barcode:
        print("Extracted Barcode:", barcode)
    else:
        print("No barcode found")