# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### La reconnaissance de caractères

Petit exercice sur la reconnaissance de caractères ou OCR
(Optical Character Recognition) dans la langue de Shakespeare.

Cet exemple nécessite l'installation de pas mal de modules
externes (OpenCV, tesseract, etc).

#HSLIDE

### Le pitch

Cet exemple est tiré du blog PyImageSearch d'Adrian Rosebrock
(https://www.pyimagesearch.com) dédié à la vision par ordinateur.

Ici on souhaite l'appliquer à la lecture de tickets de caisse ou 
de factures.

#HSLIDE

### Le code

```python
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

```
@[2-6](Import des modules nécessaires : image, OpenCV, tesseract)
@[8-14](Traitement des arguments du script : le fichier image en entrée et le pré-traitement optionnel)

#HSLIDE

### Le code - suite

```python
# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

```
@[2-3](Chargement de l'image et conversion en niveaux de gris)
@[7-14](Application optionnnelle d'un pré-traitement)
@[18-19](Ecriture dans un fichier de l'image ainsi transformée)

#HSLIDE

### Le code - suite

```python
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
 
# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)

```
@[3](Reconnaissance des caractères avec le module tesseract)
@[4](Suppression du fichier image intermédiaire)
@[5](Affichage du texte découvert dans l'image)
