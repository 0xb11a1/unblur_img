from PIL import Image

def unblur_img(imgName, blur_deg):
    # unblur 
    blur_image = Image.open(imgName)
    w,h = blur_image.size
    blur_image_pixels = blur_image.load()

    rec_img = Image.new("RGB", (w,h), 'white')
    rec_img_pixels = rec_img.load()


    side_shift = int(blur_deg/2)
    hold_value = [ [255.0]*(h) for _ in range(w) ]

    for i in range(side_shift,w-side_shift):
        for j in range(side_shift,h-side_shift):
            hold_value[i][j] = blur_image_pixels[i,j][0]

    for i in range(side_shift,w-side_shift):
        for j in range(side_shift,h-side_shift):
            flag = True
            for ii in range(-1*side_shift,side_shift+1):
                for jj in range(-1*side_shift,side_shift+1):
                    # print(blur_image_pixels[i+ii,j+jj][0])
                    if(hold_value[i+ii][j+jj] >= 255):
                        flag = False

            
            if(flag):
                rec_img_pixels[i,j] = (0,0,0)
                
                for ii in range(-1*side_shift,side_shift+1):
                    for jj in range(-1*side_shift,side_shift+1):
                        new_value = (float(hold_value[i+ii][j+jj])+0.265348595)
                        hold_value[i+ii][j+jj] = new_value

    s_name = "{}_rec.png".format(imgName[:-4])
    print(s_name)
    rec_img.save(s_name)

def blur_img(imgName,blur_deg):
    # load the image
    img  = Image.open(imgName)
    w,h = img.size

    pixels = img.load()

     # blur it 
    new_arr = [ [0]*(w) for _ in range(h) ]
    blur_image = Image.new("RGB", (w,h), 'white')
    blur_image_pixels = blur_image.load()

    side_shift = int(blur_deg/2)

    for i in range(side_shift,w-side_shift):
        for j in range(side_shift,h-side_shift):
            avrg = 0
            for ii in range(-1*side_shift,side_shift+1):
                for jj in range(-1*side_shift,side_shift+1):
                    avrg += pixels[i+ii,j+jj][0]
            avrg /=(blur_deg*blur_deg)
            new_arr[j][i] = int(avrg)
            blur_image_pixels[i,j] = (int(avrg),int(avrg),int(avrg))


    s_name = "{}_blur{}.png".format(imgName[:-4],blur_deg)
    print(s_name)
    blur_image.save(s_name)




if __name__ == "__main__":
    blur_img("./imgs/char_long_padding.png",31)
    unblur_img("./imgs/char_long_padding_blure31.png",31)
