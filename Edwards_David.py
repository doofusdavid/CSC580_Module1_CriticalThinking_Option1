"""
David Edwards
CSC580 - Applying Machine Learning and Neural Networks - Capstone
Module 1 - Critical Thinking
Dr Joseph Issa
9/18/2022
"""
from importlib.metadata import files
import PIL.ImageDraw
import face_recognition
import os

# Iternate through the images in the folder, detecting faces, and saving as a new image
for filename in os.listdir("img"):
    # Don't get the already processed images
    if filename.endswith(".jpeg") and "rectangle" not in filename:
        # get the image without the extension for saving
        filestem = filename.split(".")[0]
        image = face_recognition.load_image_file("img/" + filename)
        pilImage = PIL.Image.fromarray(image)
        face_locations = face_recognition.face_locations(image)
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
        for face_location in face_locations:
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            drawHandle = PIL.ImageDraw.Draw(pilImage)     
            drawHandle.rectangle([left, top, right, bottom], outline="red")
        pilImage.show()
        pilImage.save("img/{}-with-rectangle.jpeg".format(filestem))
    else:
        continue

