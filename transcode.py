# pillow module is used to get pixels from an image and modify them
from PIL import Image 

# this is used to convert ASCII to 8-bit binary
def generateData(message):
    li = []
    for i in message:
        li.append(format(ord(i), '08b'))

    return li

# pixels will be modified according to 8-bit binary 
def pixel_mod(pix, message):
    messageList = generateData(message)
    length = len(messageList)
    imageData = iter(pix)
    
    # retrieving 9 RGB values i.e. 3 pixels at a time
    for i in range(length):
        pix = [value for value in imageData.__next__()[:3] + imageData.__next__()[:3] + imageData.__next__()[:3]]
        
        # making pixel value 1 for odd and 0 for even
        for j in range(0, 8):
            if(messageList[i][j] == '0' and pix[j]%2 != 0):
                pix[j] -= 1
                
            elif(messageList[i][j] == '1' and pix[j]%2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
            
                else:
                    pix[j] += 1
         
         # if 8th binary-bit is 0 then continue reading the messsage, if it is 1 then return the encoded image      
        if(i == length - 1):
            if(pix[-1] %2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1

                else:
                    pix[-1] += 1

        else:
            if(pix[-1] %2 != 0):
                pix[-1] -= 1

        # holds the entire RGB values in the form of tuple
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
    

def encode(clone, message):
    imgSize = clone.size[0]
    (x, y) = (0, 0)
    
    # inserting new RGB values to the image
    for pixel in pixel_mod(clone.getdata(), message):
        clone.putpixel((x, y), pixel)
        if(x == imgSize - 1):
            x = 0
            y += 1
        else:
            x += 1
    

# taking inputs for encoding
def preEncode():
    f_img = input("\nEnter the full name of the image (with extension): ")
    image = Image.open(f_img, 'r')
    
    # for usser input use: message = input("\nEnter your secret messsage to be encoded: ") 
    
    message = open('message.txt', 'r').read()
    
    if(len(message) == 0):
        raise ValueError("Message cannot be empty")
    
    clone = image.copy()
    encode(clone, message)
    
    newImage = input("\nEnter the name of the output image (with extension): ")
    clone.save(newImage, str(newImage.split(".")[1].upper()))
    
    print("\nSUCCESSFULLY ENCODED\n")
    
    
# decodes secret messsage from output image  
def decode():
    f_img = input("\nEnter the full name of the image (with extension): ")
    image = Image.open(f_img, 'r') 
    
    message = ''
    imageData = iter(image.getdata())
    
    while(True):
        # reading the 9 RGB values from the output image
        pix = [value for value in imageData.__next__()[:3] + imageData.__next__()[:3] + imageData.__next__()[:3]]
        binaryString = ''
        
        #if RGB value is odd it'll return 1 to binary string, if it is even it'll return 0 
        for i in pix[:8]:
            if(i % 2 == 0):
                binaryString += '0'
            else:
                binaryString += '1'
                
        message += chr(int(binaryString, 2))
        
        # if 9th RGB value is odd it will return the encoded message
        if(pix[-1] %2 != 0):
            return message