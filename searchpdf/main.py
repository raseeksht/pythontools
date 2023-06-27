import PyPDF2
import os
import threading


class pdfSearch:
    def __init__(self,searchDir):
        self.searchDir = searchDir
        self.found = []
        self.threads = []
        self.allfiles = []

    def _getNestedFiles(self,dir):
        files = os.listdir(dir)
        pdfs = []
        for file in files:
            if os.path.isfile(f"{dir}/{file}"):
                try:
                    pdfs.append(f"{dir}/{file}")
                except Exception:
                    pass
            else: #must be a folder
                pdfs = self._getNestedFiles(f"{dir}/{file}")
        try:
            self.allfiles.extend(pdfs)
        except:
            pass
    
    def _searchInFile(self,file,searchTerm):
        # creating a pdf reader object
        reader = PyPDF2.PdfReader(file)

        # print the number of pages in pdf file
        print(f"searching in {file} pages=> " ,len(reader.pages))
        for index,page in enumerate(reader.pages):
            pagetext = page.extract_text()
            if searchTerm in pagetext.lower():
                # print(pagetext)

                self.found.append((file,index))
                break
    
    def search(self,term):
        print(f"searching for {term}")
        self._getNestedFiles(self.searchDir)
        self.allfiles = list(filter(lambda name: name.endswith(".pdf"),self.allfiles))
        for file in self.allfiles:
            self.threads.append(threading.Thread(target=self._searchInFile,args=(file,term)))
        
        for i,_ in enumerate(self.allfiles):
            self.threads[i].start()
        for i,_ in enumerate(self.allfiles):
            self.threads[i].join()

        if not self.found:
            print("\u001b[32mNot found\u001b[0m")
        else:
            print("\nCheck these pdf:")
            for f in self.found:
                print(f"\u001b[32m[+]\u001b[0m '{f[0]}' page no {f[1]}")


searcher = pdfSearch(".")


searchfor = input("search for : ")

searcher.search(searchfor)
