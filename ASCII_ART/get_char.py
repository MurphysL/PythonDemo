class GetChar(object):
    
    def get_char(slef ,r,g,b,alpha = 256):
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        
        if alpha == 0:
            return " "
            
        length = len(ascii_char)
        gray = int(0.2126*r +0.7152*g + 0.0722*b)
        unit = (256.0 + 1)/length

        return ascii_char[int(gray/unit)]
        