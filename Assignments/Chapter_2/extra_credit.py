#Extra Credit
#Maxwell Phillips
#10 March 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Store size Input as Variable
#3)Calculate and store for each type of image
#4)Print and format results
#-------------------------------------------------------------------------------
#Greeting
print("Greeting here.")
#Store input size as Variable
disk_size = int(input("Please enter the size of the disk in GB: "))
#Calculate for each image type
gb = int(disk_size*1000000000)
#GIF
gif = int(800*600*1)/5
gif_result = gb/gif
#JPEG
jpeg = int(800*600*3)/25
jpeg_result = gb/jpeg
#PNG
png = int(800*600*3)/8
png_result = gb/png
#TIFF
tiff = int(800*600*6)
tiff_result = gb/tiff
#Print & Format results
print("")
print(format(gif_result,'0.0f')+" images in gif format can be stored.")
print(format(jpeg_result,'0.0f')+" images in jpeg format can be stored.")
print(format(png_result,'0.0f')+" images in png format can be stored.")
print(format(tiff_result,'0.0f')+" images in tiff format can be stored.")
