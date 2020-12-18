# Steganography
This will encode a secret message to an image, as well as decodes the secret message from an encoded image.

### ALGORITHM

***

#### 1. ENCODING

- For every character in the secret messsage, the first character's ASCII value is taken and converted into a 8-bit binary.
- At a time, 3 pixels are read from an image i.e. 9 RGB values. The first 8 RGB values of the image is used to store 8-bit binary of the first character.
- Then those 8 RGB values are compared against the 8-bit binary data. If the binary digit is 1 then the RGB value is converted to odd by decrementing 1, if it is already odd then it is left as it is. If the binary digit is 0 then RGB value is converted to even by decrementing 1, if it is already even then it is left as it is. 
- The 9th RGB value is used to determine if more pixels should be read or not. If there are more characters to be read then the 9th value is changed to even else it changed to odd. 
- This has to be repeated until the secret message is encoded to an image.

***

#### 2. DECODING (Reverse of Encoding Algorithm)

- Similar to encoding, the first 3 pixels are read at once. The first 8 RGB values indicates the first character of the secret message and the 9th RGB value will tell us if we need to move forward or not. 
- For the first 8 RGB values, if the value is even then the binary bit is 0. If the value is odd then the binary bit is 1. 
- These bits are then concatenated to a string. We get a new character of the secret message with every 3 pixels. 
- We have to continue reading the RGB values if the 9th value is even, else we need to stop.
