import os
from PIL import Image
import matplotlib.pyplot as plt

# Define the directory where images are stored
image_directory = "/Users/jihopark/Desktop/Jiho_IS/Lung_Epithelial_Simulation/EMT_Density_Directed_Migration/Image_Creation/"  # Change this to your local folder path

# List all PNG image files in the directory
image_files = sorted([f for f in os.listdir(image_directory) if f.endswith(".png")])

# Construct full file paths
image_paths = [os.path.join(image_directory, filename) for filename in image_files]

# Load images
images = [Image.open(img) for img in image_paths]

# Determine grid layout: rows = number of unique senescence levels, cols = unique steps
senescence_levels = sorted(set(f.split("_")[3] for f in image_files))  # Extract senescence probabilities
steps = sorted(set(f.split("_")[-1].replace(".png", "") for f in image_files))  # Extract step numbers

rows = len(senescence_levels)
cols = len(steps)

# Ensure all images have the same size
widths, heights = zip(*(img.size for img in images))
max_width = max(widths)
max_height = max(heights)

# Resize images to a uniform size
resized_images = [img.resize((max_width, max_height)) for img in images]

# Create a blank canvas for the final combined image
combined_width = max_width * cols
combined_height = max_height * rows
final_image = Image.new("RGB", (combined_width, combined_height), (255, 255, 255))

# Arrange images in a grid layout
for index, img in enumerate(resized_images):
    row = index // cols
    col = index % cols
    final_image.paste(img, (col * max_width, row * max_height))

# Save the final combined image
output_path = os.path.join(image_directory, "combined_senescent_plot.png")
final_image.save(output_path)

# Display the result
plt.figure(figsize=(12, 10))
plt.imshow(final_image)
plt.axis('off')
plt.show()

# Print file path
print(f"Combined image saved at: {'/Users/jihopark/Desktop/Jiho_IS/Lung_Epithelial_Simulation/EMT_Density_Directed_Migration/Image_Creation/'}")
