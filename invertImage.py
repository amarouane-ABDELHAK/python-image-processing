from PIL import Image
import sys
import PIL.ImageOps as oper


def invertImage(imageName):
	image = Image.open('/workstation/'+imageName)
	image= image.convert('L')
	inverted_image = oper.invert(image)
	imageNameType = imageName.split('.')
	inverted_image.save('/workstation/out-'+imageName)

if __name__ =="__main__":
	imageName = sys.argv[1]
	if(imageName == '0'):
		print("Please mount the folder image and provide image name")
		exit(0)
	invertImage(imageName)


