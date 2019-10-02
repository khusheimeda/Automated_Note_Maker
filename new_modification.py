from docx import *

document = Document('C:/Users/KR/Desktop/Khushei_resume.pdf')
bolds=[]
italics=[]
for para in document.paragraphs:
    for run in para.runs:
        if run.bold :
            bolds.append(run.text)

boltalic_Dict={'bold_phrases':bolds}