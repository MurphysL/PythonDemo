import get_char
from PIL import Image

class ASCII_MAIN(object):
    
    def __init__(self):
        self.getchar = get_char.GetChar()
        
    def output(self , PATH , SAVE_PATH):
        WIDTH = 100
        HIGHT = 50
    
        img = Image.open(PATH)
        img = img.resize((WIDTH , HIGHT))
    
        txt = " "
        for i in range(HIGHT):
            for j in range(WIDTH):
                txt += self.getchar.get_char(*img.getpixel((j , i)))
            txt += '\n'
    
        print(txt)
    
        with open(SAVE_PATH , 'w') as f:
            f.write(txt)

if __name__ == '__main__':
    
    PATH = "d:\\1.jpg"
    SAVE_PATH = 'd:\\10.txt'
    
    obj_ascii = ASCII_MAIN()
    obj_ascii.output(PATH , SAVE_PATH)
    
    
    