
from models import ColorChange
from functions import hex_to_rgba, replace_json_value

json_file = 'test.json' # Replace with the path to your JSON file

color_changes = [
    ColorChange('0xFFffa96d', '0xFFff8fb8'),
    ColorChange('0xFF526974', '0xFFf769a3'),
    ColorChange('0xFF5c737f', '0xFFbbbbbb'),
    ColorChange('0xFF526974', '0xFFbbbbbb'),
    ColorChange('0xFF8a9ea6', '0xFFeaeaea'),
    ColorChange('0xFF718b96', '0xFFdedede'),
    ColorChange('0xFF8a9ea6', '0xFFdedede')
]

for color_change in color_changes:
 oldColor = hex_to_rgba(color_change.oldColor)
 newColor = hex_to_rgba(color_change.newColor)

 replace_json_value(json_file, oldColor, newColor)

