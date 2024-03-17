import re
from typing import Self


class DataPreProcessor:


    def __init__(self,spacy):
        self.spacy = spacy
        self.listOfResults = list()
        self.nlp = spacy.load("content/output/model-last")

    
    def processContext(self,context) -> list:
         tags =[]
         finalStr = str(context).strip()
         specialCharLess = self.removeSpecialChar(finalStr)

         for subString in specialCharLess.split(" "):
            if subString == ' ':
              continue
            tags.append(subString.strip())

         return tags
    


    def removeSpecialChar(self,str) -> str:
       
       filter = ''
       specialChar = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
       for charc in str:
          if charc in specialChar:
             filter+=' '
          else:
             filter+=charc   
       return filter
    

    def loadModelAndProcessPdf(self,context,fileLocation) -> list:
       import os
       import PyPDF2
       source_folder = fileLocation
       all_pdf_text = []
       singleString = ''
       contextTags = self.processContext(context=context)
       result =[]
       for filename in os.listdir(source_folder):
         if filename.endswith('.pdf'):
           pdf_path = os.path.join(source_folder, filename)


         with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ' '.join(page.extract_text() for page in pdf_reader.pages)
            all_pdf_text.append(pdf_text)
            for sentences in all_pdf_text:
              singleString+=str(sentences+" ")
            nlp = self.nlp

            doc = nlp(singleString)
            
            matchCount = 0
            labelFromCV = []
            for ents in doc.ents:
            #   print(ents.label_,"--",ents.text)
              labelFromCV.append((ents.label_,ents.text))
            for tg in contextTags:
               for label, text in labelFromCV:
                  if str(tg).lower() in str(text).lower():
                     matchCount+=1
            if matchCount > 0:     
             result.append({"id":str(filename).split('.')[0],"score":round((matchCount/len(contextTags)),1),"path":filename})
            all_pdf_text = []
            singleString = ''
       self.listOfResults = result
       return result
       
       
       
                 



         

       
 
 











    

    