"""
Practicing implementation using the code found below:
https://towardsdatascience.com/face-detection-with-deep-learning-using-multi-tasked-cascased-cnn-8721435531d5
"""

from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

filename = 'testImage.jpeg'

pixels = pyplot.imread(filename)


detector = MTCNN()

faces = detector.detect_faces(pixels)

for face in faces:
    print(face)