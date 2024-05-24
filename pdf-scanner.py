import PyPDF2, re, sys, urllib.request, os

def search_pdf(pdf,term):
    print("Scanning "+pdf+" for "+term)
    reader = PyPDF2.PdfReader(pdf)
    num_pages = len(reader.pages)
    match = False
    for page in reader.pages:
        text = page.extract_text()
        res_search = re.search(term, text)
        if res_search != None:
            match = True
    return match

def download_pdf(pdfUrl):
    uri, fileName = os.path.split(pdfUrl)
    print("Downloading from "+uri+" to "+fileName)
    urllib.request.urlretrieve(pdfUrl, fileName)
    return fileName

def main():
    pdfUrl = sys.argv[1]
    searchTerm = sys.argv[2]
    pdfFile = download_pdf(pdfUrl)
    if search_pdf(pdfFile,searchTerm):
        print("Match - "+pdfFile)
    os.remove(pdfFile)

if __name__ == "__main__":
    main()
