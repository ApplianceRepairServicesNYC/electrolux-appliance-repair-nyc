#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Replace hero background
content = content.replace(
    "/assets/images/electrolux-logo.png",
    "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1920&q=80"
)

# Find and replace base64 images based on alt text or context
# Logo in header
content = re.sub(
    r'<img src="data:image/png;base64,[^"]+"\s+alt="Electrolux[^"]*Logo[^"]*"',
    '<img src="/assets/images/electrolux-logo.png" alt="Electrolux Appliance Repair NYC Logo"',
    content,
    flags=re.IGNORECASE
)

# Also match logos without explicit Logo in alt
content = re.sub(
    r'<img src="data:image/png;base64,[^"]+" alt="Electrolux Appliance Repair NYC"',
    '<img src="/assets/images/electrolux-logo.png" alt="Electrolux Appliance Repair NYC"',
    content
)

# Service card images - match by alt text patterns
image_mappings = [
    ('Oven', '/assets/images/oven.webp'),
    ('Cooktop', '/assets/images/oven.webp'),
    ('Microwave', '/assets/images/microwave.webp'),
    ('Refrigerator', '/assets/images/refrigerator.webp'),
    ('Dryer', '/assets/images/dryer.webp'),
    ('Washer', '/assets/images/washer.webp'),
    ('Dishwasher', '/assets/images/dishwasher.webp'),
    ('Wine', '/assets/images/refrigerator.webp'),
]

for alt_text, img_path in image_mappings:
    pattern = rf'<img src="data:image/png;base64,[^"]+" alt="Electrolux {alt_text}[^"]*"'
    replacement = f'<img src="{img_path}" alt="Electrolux {alt_text} Repair"'
    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

# Write the file
with open('index.html', 'w') as f:
    f.write(content)

print("Images updated!")
