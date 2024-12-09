import subprocess
from PIL import Image

def images_to_pdf(image_list, output_pdf_path):
    # Open each image file and ensure all are in RGB mode
    images = []
    for img_path in image_list:
        with Image.open(img_path) as img:
            images.append(img.convert('RGB'))
    
    # Save all images as a single PDF
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    else:
        print("No images provided!")

    subprocess.Popen([output_pdf_path],shell=True)