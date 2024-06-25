from pypdf import PdfReader
from difflib import SequenceMatcher
file1 = []
file2 = []
# Change the name of the files to define the files you'd like to compare.
firstFileName = 'file4.pdf'
secondFileName = 'file1.pdf'

def main():
    reader = PdfReader(firstFileName)

    for i in range(reader.get_num_pages()):

        pages = reader.pages[i]
        content = pages.extract_text().strip()
        file1.append(content)
    
    # print(f"this is file 1{file1}")

    reader2 = PdfReader(secondFileName)

    for j in range(reader2.get_num_pages()):

        pages2 = reader2.pages[j]        
        content2 = pages2.extract_text().strip()
        file2.append(content2)
    
    # print(f"this is file 2{file2}")

    string1 = str(file1)
    string2 = str(file2)

    seq = SequenceMatcher(a = string1, b = string2)
    ratio = seq.ratio()

    print(f"the similarity is {round(ratio*100,1)}%")
    
    if(ratio == 1):
         print("Both files are the same")
    elif(0.4 < ratio < 1):
         print("Files some similarities.")
    else:
         print("Both files are unique and have no similarities")   

if __name__ == '__main__':    
        main()