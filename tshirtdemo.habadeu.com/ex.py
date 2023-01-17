fonts=[]
import re

with open("test.html") as f:
    for line in f:
        # extract font name from data-value="font name"
        font = re.search(r'data-value="([^"]+)"', line)
        if font:
            fonts.append(font.group(1))

print(fonts)

# # now in the fonts directory find the files that match the font names in the list
# import os
# for font in fonts:
#     for file in os.listdir("fonts"):
#         new_font_name = font.replace(" ","-") + ".woff"
#         font=font.replace(" ","_")
#         if font in file.capitalize():
#             # now rename the file to the font name + ".woff"
#             os.rename("fonts/"+file, "fonts/"+new_font_name)


# list files in the fonts directory
# import os

# fonts_to_download = []
# for file in os.listdir("fonts"):
#     print(file)
#     fonts_to_download.append(file)

# # now download the fonts
# url_prefix = "https://assets0.printio.ru/assets/"

# # download the fonts and save to "real" directory
# import http.client
# import urllib.request
# import urllib.parse
# import urllib.error

# for font in fonts_to_download:
#     conn = http.client.HTTPSConnection("assets0.printio.ru")
#     conn.request("GET", "/assets/"+font)
#     res = conn.getresponse()
#     data = res.read()
#     with open("real/"+font, "wb") as f:
#         f.write(data)
#     print("downloaded: "+font)

# list file names in fonts directory
# import os
# fonts=[]
# for file in os.listdir("fonts"):
#     print(file)
#     fonts.append(file)

# # rename file from "font_name.woff" to "font_name.woff" without the hash not using regex
# for font in fonts:
#     try:
#         new_font_name = str(font.split(".")[0]).title() + ".woff"
#         os.rename("fonts/"+font, "fonts/"+new_font_name)
#     except:
#         pass

import os

for f in fonts:
    f=f.replace(" ","_")
    if os.path.isfile("fonts/"+f+".woff"):
        print("file exists: "+f)
