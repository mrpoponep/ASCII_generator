import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image,ImageDraw,ImageFont

def main(input_file,output_file,col_nums=200):
    CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    img=cv2.imread(input_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    font=ImageFont.truetype("font/arial-unicode.ttf",size=25)
    _,_,char_width, char_height = font.getbbox("A")
    height,width,channels=img.shape
    cell_width=width/col_nums
    cell_height=2*cell_width
    row_nums=int(height/cell_height)
    out_width = char_width * col_nums
    out_height = char_height * row_nums
    
    out_image = Image.new("RGB", (int(out_width), int(out_height)))
    draw=ImageDraw.Draw(out_image)
    pbar_total =row_nums
    pbar = tqdm(total=pbar_total, desc="Generating")
    if col_nums>width:
        return ValueError("too many column")
    for i in range(0,row_nums):
        for j in range(0,col_nums):
            sub_img=img[int(i*cell_height):int((i+1)*cell_height),int(j*cell_width):int((j+1)*cell_width)]
            avg_color=sub_img.mean(axis=0).mean(axis=0)
            avg_color=tuple(np.int32(avg_color))
            char = CHAR_LIST[int(np.mean(sub_img)/255*len(CHAR_LIST))]
            draw.text((j * char_width, i * char_height), char, fill=(tuple(avg_color)), font=font)
        pbar.update(1)
    pbar.close()    
    out_image.save(output_file)
    print("Generating completed")

if __name__ == '__main__':
    input_file="input/corgi.jpg"
    output_file="data/img2color_output.jpg"
    main(input_file,output_file)