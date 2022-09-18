import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("img/willvill.jpeg")
face_locations   = face_recognition.face_locations(image)
numberOfFaces = len(face_locations)
print("Found {} face(s) in this picture.".format(numberOfFaces))

pilImage = PIL.Image.fromarray(image)

for faceLocation in face_locations:
    top, right, bottom, left = faceLocation
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    drawHandle = PIL.ImageDraw.Draw(pilImage)     
    drawHandle.rectangle([left, top, right, bottom], outline="red")

pilImage.show()
pilImage.save("img/willvill-with-rectangle.jpeg")