from PIL import Image, ImageDraw
import math

def num_to_QR_main(filename):
    f=open(filename).read()
    i=0
    a=255
    wide=int(math.sqrt(len(f)))
    image = Image.new('RGB', (wide,wide), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for x in range(wide):
        for y in range(wide):
            try:
                if(f[i]=='0'):
                    a=255
                else:
                    a=0
                draw.point((x, y), fill=(a,a,a))
                i+=1
            except Exception as e:
                print('发生错误')
    image.save(filename+'_to_QR.png', 'png')
    print('Save as filename+"_to_QR.png"')

if __name__ == "__main__":
    filename=input('filename=')
    num_to_QR_main(filename)