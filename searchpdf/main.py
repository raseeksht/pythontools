# importing all the required modules
import PyPDF2
import os


allfiles = os.listdir()

allfiles = list(filter(lambda name: name.endswith(".pdf"),allfiles))

searchfor = input("search for : ")

found = []

for file in allfiles:
    # creating a pdf reader object
    reader = PyPDF2.PdfReader(file)

    # print the number of pages in pdf file
    print(f"searching in {file} pages=> " ,len(reader.pages))
    for index,page in enumerate(reader.pages):
        pagetext = page.extract_text()
        if searchfor in pagetext.lower():
            # print(pagetext)

            found.append((file,index))
            break


if len(found) == 0:
    print("not found")
else:
    print("\nCheck these pdf:")
    for f in found:
        print(f[0],"page no",f[1])


    # print the text of the first page
    # print(reader.pages[0].extract_text())