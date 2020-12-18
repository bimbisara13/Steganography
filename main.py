# importing functions from transcode.py
from transcode import preEncode, decode

def main():
    print("\n---This is Steganography---\n\nThis will encode a secret message to an image, as well as decodes the secret message from an encoded image.\n")
    print("What would you like to do?\n\n1. ENCODE")
    print("2. DECODE\n")
    
    choice = int(input("Select an option: "))
    
    if(choice == 1):
        preEncode()
        
    elif(choice == 2):
        print("\nDECODED MESSAGE: "+ decode() + "\n")
        
    else:
        raise Exception("INVALID CHOICE")
    
if __name__ == "__main__":
    main()