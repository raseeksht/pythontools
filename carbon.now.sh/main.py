import asyncio
from carbon import Carbon
import os
import argparse

saveTo = "carbonimages"

if not os.path.exists(saveTo):
    os.mkdir(saveTo)

client = Carbon(
    downloads_dir= os.path.join(os.getcwd(),saveTo),  # Defaults to current directory
    colour="rgba(171, 184, 195, 1)",  # Hex or rgba color
    shadow=True,  # Turn on/off shadow
    shadow_blur_radius="68px",
    shadow_offset_y="20px",
    export_size="2x",  # resolution of exported image, e.g. 1x, 3x
    font_size="14px",
    font_family= "Hack",  # font family, e.g. JetBrains Mono, Fira Code.
    first_line_number=1,
    language="auto",  # programing language for properly highlighting
    line_numbers=True,  # turn on/off, line number
    horizontal_padding="56px",
    vertical_padding="56px",
    theme="seti",  # code theme
    watermark=False,  # turn on/off watermark
    width_adjustment=True,  # turn on/off width adjustment
    window_controls= True,  # turn on/off window controls
    window_theme=None
)


async def convert():
    img = await client.create(file=parsedArgs.file)
    print(f"saved at: {img}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser("Convert code to carbon images in bulk")
    parser.add_argument("-d","--dir",help="specify the directory from where all the files need to be carbonated")
    parser.add_argument("-f","--file",help="create carbonation of single file")

    parsedArgs = parser.parse_args()

    if not (parsedArgs.dir or parsedArgs.file):
        print("=================================")
        print("either -d or -f flag is necessary")
        print("=================================")
        parser.print_help()
        exit()

    print(parsedArgs)
    asyncio.run(convert())