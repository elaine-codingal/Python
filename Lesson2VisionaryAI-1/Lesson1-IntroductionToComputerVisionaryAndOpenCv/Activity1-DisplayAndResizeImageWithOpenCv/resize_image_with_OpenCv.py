import cv2

#Load the image
image=cv2.imread('../images/dog.jpg')

#Resize the window to a specified size without resizing the image
cv2.namedWindow('LoadedImage', cv2.WINDOW_NORMAL) #Create a resizable window
cv2.resizeWindow('LoadedImage',800,500)#Set the window size to 800x500(widthxheight)

#Display the image in the resized window
cv2.imshow('LoadedImage', image)
cv2.waitKey(0)#Wait for a key press
cv2.destroyAllWindows() #Close the window

#Print image properties
print(f"Image Dimensions:{image.shape}")#Height, Width, Channels
