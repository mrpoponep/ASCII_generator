import cv2
import numpy as np

def main(input_file,output_file,col_nums=150,):
    CHAR_LIST = "$@B%8&WM#*zcvunxrjft/\|()1{}[]?-_+~<>i!lI;;::,,,\"\"\"^^^`````'''''.......     "
    img=cv2.imread(input_file)
    height,width,channels=img.shape
    cell_width=width/col_nums
    cell_height=2.5*cell_width
    out_width=cell_width*col_nums
    out_width=2*cell_width*col_nums

    row_nums=int(height/cell_height)
    output=[]

    if col_nums>width:
        return ValueError("too many column")
    for i in range(0,row_nums):
        row=[]
        for j in range(0,col_nums):
            sub_img=img[int(i*cell_height):int((i+1)*cell_height),int(j*cell_width):int((j+1)*cell_width)]
            index = int(np.mean(sub_img)/255*len(CHAR_LIST))
            row.append(CHAR_LIST[index])
        output.append(row)   
    with open(output_file, "w",encoding="utf-8") as file:
        for line in output:
            file.write("".join(line))
            file.write("\n")
    print("Generating completed")

if __name__ == '__main__':
    input_file="input/corgi.jpg"
    output_file="data/img2text_output.txt"
    main(input_file,output_file)