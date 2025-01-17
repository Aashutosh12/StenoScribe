#Steganography

import cv2 # pip install opencv-python
import os
def spiltbyte(by): #011 000 01
    first_three_bits = by >> 5
    mid_three_bits = (by >> 2) & 7
    last_two_bits = by & 3
    return first_three_bits, mid_three_bits, last_two_bits

def merge_bits(bits) : #[3,0, 1] => 97
    # result = bits[0] <<3 #make room for 3 bits at the RHS
    # result = result | bits[1] #merge the mid 3 bits
    # result = result << 2 #make room for 2 bits at the RHS
    # result = result | bits[2] #merge the mid 2 bits

    return (((bits[0]<<3) | bits[1]) << 2) | bits[2]

def getMetaData(file_to_embed):
    if os.path.exists(file_to_embed): #check that the file exists
        file_size = os.path.getsize(file_to_embed) #know the file size in bytes
        if file_size > 9999999999:
            return None #More than the max support
        file_size = str(file_size).ljust(10,'*') #Pad * at the RHS to make it of length : 10
        file_name = os.path.basename(file_to_embed) #exclude the parent path
        file_name = file_name.ljust(20, '*') #Pad * at the RHS to make it of len 20, doesnt pad is len is already > 20
        file_name = file_name[len(file_name)-20:] #reduce the len to 20 by slicing
        return file_size+file_name

    else:
        return None

def crypt(src, key):
    crypted = ''
    i =0
    l = len(key)
    for s in src:
        x = key[i]
        crypted += chr(ord(s) ^ ord(x))
        i = (i+1) % l
    return crypted

def embed(vessel_image, target_image):
    #load the vessel_image into memory
    mem_image = cv2.imread(vessel_image)
    print(type(mem_image))
    print(mem_image.shape)

    #dummy data to embed
    data = [x for x in range(65,91)]
    print(data)
    size = len(data)
    indx = 0

    #embedding loop
    r =0
    while r < mem_image.shape[0] and indx < size:
        c =0
        while c < mem_image.shape[1] and indx < size:
            bits = spiltbyte(data[indx])

            #Free 2,3,3 bits of the pixel
            mem_image[r, c, 0] &= 252  #blue band
            mem_image[r, c, 1] &= 248  #green band
            mem_image[r, c, 2] &= 248  #red band

            #Merge the bits into the bands
            mem_image[r, c, 0] |= bits[2]  # blue band
            mem_image[r, c, 1] |= bits[1]  # green band
            mem_image[r, c, 2] |= bits[0]  # red band

            #next val to embed
            indx+=1

            c+=1
        r+=1

    #save back the image
    cv2.imwrite(target_image, mem_image)

def extract(emb_image):
    #load the image in memory
    mem_img = cv2.imread(emb_image)
    #print(mem_img.shape)
    qty_to_extract = 26
    width = mem_img.shape[1]
    indx =0
    buffer = []
    temp = []
    while indx < qty_to_extract:
        r = indx //width
        c = indx % width
        temp.clear()
        for i in range(3): #0,1,2
            temp.append(mem_img[r,c,2-i] & 2 ** (3 - (i+1) // 3) - 1)

        buffer.append(merge_bits(temp))
        indx+=1


    return buffer

def main():
    embed('d:/steganography/snake.jpg', 'd:/steganography/new_snake.png')
    buffer = extract('d:/steganography/new_snake.png')
    # print(buffer)
    data = getMetaData('d:/temp/about_loops.txt')
    passcode = 'strong33'
    result = crypt(data, passcode)

    data_back = crypt(result, passcode)
    print(result, len(result))
    print(data_back, len(data_back))


main()


