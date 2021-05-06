import re
number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    barcode = input()
    pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
    valid_barcodes = re.findall(pattern,barcode)
    if not valid_barcodes:
        print("Invalid barcode")
    else:
        pattern_group = r"\d"
        product_group = re.findall(pattern_group, barcode)
        product_group = ''.join(product_group)
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")