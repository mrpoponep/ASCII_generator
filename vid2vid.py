import cv2
import numpy as np
import timeit
from tqdm import tqdm
from PIL import Image,ImageDraw,ImageFont
        

def main(input_file,output_file,col_nums=150):
    CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    font = ImageFont.truetype("font/arial-unicode.ttf",size=25)
    _,_,char_width, char_height = font.getbbox("A")
    cap = cv2.VideoCapture(input_file)
    fps = 10
    number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Number of frames: ", str(number_of_frames))
    pbar_total =number_of_frames
    pbar = tqdm(total=pbar_total, desc="Generating",ncols=100)
    success, image = cap.read()
    height,width,channels=image.shape
    cell_width=width/col_nums
    cell_height=2*cell_width
    row_nums=int(height/cell_height)
    out_width = char_width * col_nums
    out_height = char_height * row_nums
    while cap.isOpened():
        flag, frame = cap.read()
        
        if flag:
            image = frame
        else:
            break
        
        out_image = Image.new("RGB", (out_width, out_height),)
        draw = ImageDraw.Draw(out_image)
        
        for i in range(0,row_nums):
            for j in range(0,col_nums):
                sub_img=image[int(i*cell_height):int((i+1)*cell_height),int(j*cell_width):int((j+1)*cell_width)]
                avg_color=sub_img.mean(axis=0).mean(axis=0)
                avg_color=tuple(np.int32(avg_color))
                char = CHAR_LIST[int(np.mean(sub_img)/255*len(CHAR_LIST))-1]
                draw.text((j * char_width, i * char_height), char, fill=avg_color, font=font)
        
        out_image = np.array(out_image)
        try:
            out
        except:
            out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps,
                                  ((out_image.shape[1], out_image.shape[0])))
        
        out.write(out_image)
        pbar.update(1)
    pbar.close()
    cap.release()
    out.release()

if __name__ == '__main__':
    start = timeit.default_timer()
    input_file="input/seagull_compressed.mp4"
    output_file="data/vid2vid_output.mp4"
    main(input_file,output_file)
    end = timeit.default_timer()
    print(f"time{end-start}")