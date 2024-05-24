import PyPDF2, re, requests, sys, urllib.request, os
from bs4 import BeautifulSoup

def search_pdf(pdf,term):
    #print("Scanning "+pdf+" for "+term)
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
    fileName = os.path.split(pdfUrl)[1]
    #print("Downloading "+pdfUrl)
    urllib.request.urlretrieve(pdfUrl, fileName)
    return fileName

def find_anchors(aUrl,aTag,aClass):
    html = requests.get(aUrl).text
    page = BeautifulSoup(html,features="html.parser")
    urls = []
    for div in page.find_all(aTag, class_=aClass):
        a = div.find('a') 
        try:
            if 'href' in a.attrs: 
                url = a.get('href') 
                urls.append(url) 
        except: 
            pass
    return urls

def main():
    site = sys.argv[1]
    searchTerm = sys.argv[2]
    depth = int(sys.argv[3])
    index = 1
    baseUrl = os.path.split(site)[0]
    while index <= depth:
        siteAndPage = site + "?page=" + str(index)
        print("Scanning " + siteAndPage)
        urls = find_anchors(siteAndPage,"div","gem-c-document-list__item-title")
        for url in urls:
            #print(baseUrl+url)
            files = find_anchors(baseUrl+url,"span","attachment-inline")
            #print(files[0])
            for file in files:
                pdfFile = download_pdf(file)
                if search_pdf(pdfFile,searchTerm):
                    print("Match - "+file)
                os.remove(pdfFile)
        index = index + 1
    

if __name__ == "__main__":
    main()
