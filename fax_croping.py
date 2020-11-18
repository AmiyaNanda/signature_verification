# Importing Image class from PIL module 
from PIL import Image 
import requests # to get image from the web
import shutil # to save it locally



## Set up the image URL and filename
image_url = "https://faxsignature8360972039.blob.core.windows.net/fax/fax3.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')


img = Image.open(filename)

# Opens a image in RGB mode 
# Size of the image in pixels (size of original image) 
# (This is not mandatory) 
width, height = img.size 
# Setting the points for cropped image 
left = 155
top =  1546
right = 690
bottom = 1760
  
# Cropped image of above dimension 
# (It will not change original image) 
im1 = img.crop((left, top, right, bottom)) 

cr1 = Image.open(im1)
cr1.show()

  
# Shows the image in image viewer 
#im1.show() 

 
