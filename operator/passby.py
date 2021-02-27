def edit_dict(dict):
    dict["owner"] = "wiracha"
    print("[function]", dict)


cup = {}

print("[1]", cup)  # Output: {}
edit_dict(cup)  # Output: [function] {'owner':'pawornwan'}
print("[2]", cup)  # Output: [function] {'owner':'pawornwan'}
# จริงๆแล้วต้องเป็น {}