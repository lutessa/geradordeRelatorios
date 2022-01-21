from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import csv
import sys 

def main (args):

    infocsv=args[1]
    template=args[2]
    
    with open(infocsv,'r') as csvf:
        op = csv.reader(csvf)
        data=list(op)
    indices=data[0]


    for n in range(1,len(data)):
        doc=DocxTemplate(template)
        context=dict()
        docdata=data[n]
        for i in range(len(docdata)):
            if indices[i].startswith("image"):
                context[indices[i]]=InlineImage(doc, 'images/'+docdata[i],width=Mm(80), height=Mm(80))
            else:
                context[indices[i]]=docdata[i]

        doc.render(context)


        doc.save(f"relatorio{docdata[0]}.docx")

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))