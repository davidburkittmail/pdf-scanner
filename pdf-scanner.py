# import packages
import PyPDF2
import re
import sys

pdf = sys.argv[1]
term = sys.argv[2]
print("Scanning "+pdf+" for "+term)

# open the pdf file
reader = PyPDF2.PdfReader(pdf)

# get number of pages
num_pages = len(reader.pages)

# extract text and do the search
for page in reader.pages:
    text = page.extract_text()
    # print(text)
    res_search = re.search(term, text)
    #print(res_search)
    if res_search != None:
        print("Match")
