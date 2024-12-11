import json
# Function to convert hex color to RGBA
def hex_to_rgba(hex_code):
    # Remove the "0x" prefix if it exists, and ensure the hex string is 8 characters long
    hex_code = hex_code if hex_code.startswith("0x") else "0x" + hex_code
    
    hex_code = hex_code[2:].zfill(8)  # Ensure the hex string is 8 characters long
    hex_value = int(hex_code, 16)

    # Extract the red, green, blue, and alpha components
    r = (hex_value >> 16) & 0xFF
    g = (hex_value >> 8) & 0xFF 
    b = hex_value & 0xFF        
    a = (hex_value >> 24) & 0xFF

    # Normalize RGB to [0, 1] and alpha to [0, 1], and remove the mantissa if it's an integer
    def normalize(val):
        norm = val / 255
        return int(norm) if norm.is_integer() else norm

    rgba = [normalize(r), normalize(g), normalize(b), normalize(a)]

    return rgba

def replace_json_value(json_file,old_color, new_color):
    # Open and load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Recursive function to traverse and modify the JSON structure
    def modify_json(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'ty' and value == 'fl' and isinstance(obj.get('c'), dict):
                    c_dict = obj['c']
                    if 'a' in c_dict and c_dict['a'] == 0 and 'k' in c_dict:
                        # Replace the list after "k"
                        if isinstance(c_dict['k'], list):
                            current_color_rounded = [round(item, 4) for item in c_dict['k']]
                            old_color_rounded     = [round(item, 4) for item in old_color]
                            if current_color_rounded == old_color_rounded:
                               c_dict['k'] = new_color
                else:
                    modify_json(value)
        # Check if the value is a list and recursively call the function
        elif isinstance(obj, list):
            for item in obj:
                modify_json(item)

    # Modify the JSON data
    modify_json(data)

    # Save the modified JSON back to the file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
