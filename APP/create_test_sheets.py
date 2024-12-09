import sys
import time
import cv2
import numpy as np
import qrcode
from PIL import Image
import os
from APP import pdf 
import random
import subprocess
import itertools
from APP.pdf import images_to_pdf


def create_sheet(data):

    # print(f"this {data}")
    # for key, value in data.items():
    #     print(f"{key}: {value}")
    imagelist = []  
    for item in data:
        # print("Student ID: ", item['Student_id'])

        # read the blank test sheet
        sheet = cv2.imread(r"APP\temp_anssheet.jpg")

        #convert to grayscale
        sheet = cv2.cvtColor(sheet, cv2.COLOR_BGR2GRAY)

        #scaling constants
        x_offset = 0
        y_offset = 0
        name = f"{item['StudentIdNo']} {item['Fullname']}"
        ExamId = f"STUDENT ID : {item['StudentIdNo']}"
        TestId = f"EXAMINATION ID : {item['ExaminationMain']}" 
        ExamName = f"NAME : {item['Fullname']}"

        #make QR code
        qr_img = qrcode.make(name)
        qr_img = np.float32(qr_img)

        #crop and resize QR code
        #qr_img = qr_img[10:350, 10:340]
        qr_img = cv2.resize(qr_img, (0, 0), fx=0.35, fy=0.35)

        #calculate coordinates where the QR code should be placed
        y1, y2 = y_offset, y_offset + qr_img.shape[0]
        x1, x2 = x_offset, x_offset + qr_img.shape[1]

        #place the QR code on the sheet
        sheet[y1:y2, x1:x2] = qr_img * 255 

        font = cv2.FONT_HERSHEY_COMPLEX

        # Define text position
        text_position = (140,30)  # You can change this to where you want the text

        # Define font scale and color
        font_scale = 0.5
        text_color = (0, 0, 0)  # White color, you can change to any BGR value

        # Define thickness of the text
        thickness = 1
        # Add text to image
        cv2.putText(sheet, ExamId, text_position, font, font_scale, text_color, thickness, cv2.LINE_AA)
        

        # Define text position
        text_position = (140,50)  # You can change this to where you want the text

        # Add text to image
        cv2.putText(sheet, TestId, text_position, font, font_scale, text_color, thickness, cv2.LINE_AA)
        

        # Define text position
        text_position = (140,70)  # You can change this to where you want the text

        # Add text to image
        cv2.putText(sheet, ExamName, text_position, font, font_scale, text_color, thickness, cv2.LINE_AA)

        # Convert the image from BGR (OpenCV format) to RGB (Pillow format)
        original_image = cv2.cvtColor(sheet, cv2.COLOR_BGR2RGB)
        original_image = Image.fromarray(original_image)

        # Load the watermark image using Pillow
        watermark = Image.open(r"APP\logo.png")
        # Resize the watermark
        new_size = (200, 50)  # width, height in pixels
        watermark = watermark.resize(new_size)

        # Define the position (x, y) where the watermark will be placed
        # For example, bottom right corner with a 10-pixel offset
        x = original_image.width - watermark.width - 10
        y = 10

        # Paste the watermark image onto the original image
        original_image.paste(watermark, (x, y), watermark)  

        # Convert the image back to BGR format for displaying with OpenCV
        result_image_cv2 = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2BGR)
        # name= str(name) + ".png"
        name=f"{random.randint(100000000, 999999999)}.png"

        save_path = os.getcwd()+rf"\APP\static\imgAnswer\{name}"

        imagelist.append(save_path)
        print(save_path)
        #save_path = rf"{folder}\{name}"
        # Specify the path where you want to save the image
        #save_path = '/path/to/your/directory/output_image.jpg'

        #write the image file
        cv2.imwrite(save_path, result_image_cv2)

    name = f"ans_{random.randint(100000000, 999999999)}.pdf"
    save_path = os.getcwd()+rf"\APP\static\answerSheet\{name}" 
    
    images_to_pdf(imagelist, save_path)
    # subprocess.Popen([save_path],shell=True)
    #pdf.createPDF(imagelist)# Display download link
