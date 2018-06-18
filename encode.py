from PIL import Image
import numpy as np
import sys
import scipy.misc

def toAscii(msg):
	listOfAscii = []
	for alphabet in msg:
		binascii = "{0:08b}".format(ord(alphabet))
		listOfAscii.append(binascii)
	listOfAscii.append('01100000') #terminator
	return listOfAscii


def main():
	imgPath = open("tmppath.txt").read().strip()
	print(imgPath)

	try:
		img = Image.open(imgPath)
	except Exception as e:
		print(e)
		print("Try Again..")
		main()


	img = img.convert("L")
	width,height = img.size
	totalPixel = width * height
	alphabetsCapacity = totalPixel//4
	print("Maximum Charachters : " + str(alphabetsCapacity))
	message=open("Encryptedmsg.txt").read().strip()
	lengthOfMessage = len(message)

	if lengthOfMessage > alphabetsCapacity:
		message = message[:alphabetsCapacity]
		print("\nDue to lack of pixels only following message can be encoded :\n"+message)
		print("\n\n")

	listOfAscii = toAscii(message)
	totalPixRequired = len(listOfAscii) * 4


	arr = np.array(img)
	nextPix = listOfAscii[0]
	arrayPointer = 1 #points to encoded msg list
	pixOver = 0
	finish = False

	for i,row in enumerate(arr):
		for j,column in enumerate(row):
			if (totalPixRequired > 0):
				if (pixOver == 4):
					nextPix = listOfAscii[arrayPointer]
					arrayPointer += 1
					pixOver = 0

				#change decimal to binary
				binPix = "{0:08b}".format(column)
				firstFourDigits = binPix[:-2] #actual Pixel Value 4 digits

				twoDigitsForMsg = nextPix[:2] #value from Encoded msg last 2 digits

				nextPix = nextPix[2:]
				pixOver += 1

				encodedPix = firstFourDigits + twoDigitsForMsg

				decPix = int(str(encodedPix),2)
				arr[i][j] = decPix

				totalPixRequired -= 1

			else:
				finish = True
				break
		if(finish):
			pass
			break

	encrypted = Image.fromarray(arr,"L")
	encryptedImage = scipy.misc.toimage(encrypted,cmin=0,cmax=255)
	encryptedImage.save("checkitout.png")
	print("Done! ^_^")


if __name__ == "__main__":
	main()
