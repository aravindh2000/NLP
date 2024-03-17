from pypdf import PdfReader 
import DataPreProcessor 
import spacy
  

reader = PdfReader('C:/Users/Aravindh Siva/Downloads/MayankVerma_Mtech_Electrical.pdf') 
  

print(len(reader.pages)) 

skillSet = []

exEmployers = []

pages = len(reader.pages)



processorInstance = DataPreProcessor.DataPreProcessor(spacy)


for page in reader.pages:

    print(type(page.extract_text().split("\n")))
    tokens = page.extract_text().split("\n")
    skillSet.append(processorInstance.processSkills(tokens))
    print(set(skillSet[0]))
    print(processorInstance.slikkPoint)
    #exEmployers.append(processorInstance.processEmployers(tokens))
    

  




