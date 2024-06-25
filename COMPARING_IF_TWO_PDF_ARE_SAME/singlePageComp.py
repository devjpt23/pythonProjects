from pypdf import PdfReader
from difflib import SequenceMatcher

file1 = PdfReader("file4.pdf")


pagesFile1 = file1.pages[0]
content1 = pagesFile1.extract_text().strip()


file2 = PdfReader("file1.pdf")
pagesFile2 = file2.pages[0]
content2 = pagesFile2.extract_text().strip()



seq = SequenceMatcher(a = content1, b = content2)
ratio = seq.ratio()
print(ratio)

if (ratio == 1):
    print("these are same files")
elif (0.5 < ratio < 1):
    print("the files are similiar, but some content doesnt match")
else:
    print("files are not the same at all")
