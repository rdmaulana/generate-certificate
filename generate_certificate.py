from PIL import Image, ImageFont, ImageDraw
import pandas as pd

def main():
    print("Initializing Script!")
    # names = pd.read_csv('name_data.csv')

    list_name = pd.read_excel('list_peserta.xlsx', sheet_name='Sheet1')
    for i,row in list_name.iterrows():
        name = str(row['Nama'])
        name = name.title()
        empty_certi = Image.open("master/blank_certi.jpg")
        font_size = 250
        font = ImageFont.truetype("font/edwardian-script-itc-bold.ttf") 
        W,H = empty_certi.size 
        w, h = font.getsize(name)
        width = ((W-w)/2)
        height = ((H-h)/2)-100

        if W%w >= 2:
            font_size = 200
            width = ((W-w)/2) +75
            height = ((H-h)/2)-40

        font = ImageFont.truetype("font/edwardian-script-itc-bold.ttf", font_size)
        image_editable = ImageDraw.Draw(empty_certi)
        xposition = (empty_certi.size[0] - image_editable.textsize(name, font)[0]) / 2
        image_editable.multiline_text((xposition, 1100), name, (0, 0, 0), font=font)
        empty_certi.save("certificate/{}.pdf".format(name.replace(" ", "_")), "PDF")
        if i % 50 == 0: 
            print('Processed {} Rows'.format(i))
    print("Process Complete!")

if __name__ == '__main__':
    main()