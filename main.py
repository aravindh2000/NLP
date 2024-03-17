import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

# nlp = spacy.blank('en')
# db = DocBin()
# import os

# finalData = []
# for filename in os.listdir('D:/jsonData'):
#   data = json.load(open('D:/jsonData/'+str(filename),encoding="mbcs"))
#   print(data)
#   for annotation in data['annotations']:
#      if annotation != None:
#          text = annotation[0]
#          ent= []
#          for entity in annotation[1]['entities']:
#             if entity != None:
#               start = entity[0]
#               end = entity[1]
#               label = entity[2]
#               ent.append((start,end,label))
#          finalData.append((text,{"entities":ent}))
# print(finalData)
#   # Iterate through the data
# for text, annot in tqdm(finalData):
#     doc = nlp.make_doc(text)
#     annot = annot['entities']

#     ents = []
#     entity_indices = []

#   #   # Extract entities from the annotations
#     for start, end, label in annot:
#       skip_entity = False
#       for idx in range(start, end):
#         if idx in entity_indices:
#           skip_entity = True
#           break
#       if skip_entity:
#         continue

#       entity_indices = entity_indices + list(range(start, end))
#       try:
#         span = doc.char_span(start, end, label=label, alignment_mode='strict')
#       except:
#         continue

#       if span is None:
#         # Log errors for annotations that couldn't be processed
#         err_data = str([start, end]) + "    " + str(text) + "\n"
#         print(err_data)
#         #file.write(err_data)
#       else:
#         ents.append(span)

#     try:
#       doc.ents = ents
#       db.add(doc)
#       db.to_disk("./train.spacy")
#     except:
#       pass


nlp = spacy.load('content/output/model-last')
doc = nlp("Python")
for ents in doc.ents:
  print(ents.label_,"--",ents.text)



# import os
# import PyPDF2


# source_folder = './CV_FOR_TEST'
# # combined_txt_path = 'D:/FinalTest/finalText.txt'

# all_pdf_text = []

# singleString = ''


# for filename in os.listdir(source_folder):
#     if filename.endswith('.pdf'):
#         pdf_path = os.path.join(source_folder, filename)


#         with open(pdf_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfReader(pdf_file)
#             pdf_text = ' '.join(page.extract_text() for page in pdf_reader.pages)
#             all_pdf_text.append(pdf_text)
#             for sentences in all_pdf_text:
#               singleString+=str(sentences+" ")
#             nlp = spacy.load('content/output/model-best')

#             doc = nlp(singleString)
#             for ents in doc.ents:
#               print(ents.label_,"--",ents.text)

#             all_pdf_text = []
#             singleString = ''
#             print('========================================================== END OF ONE RESUME =============================================================')




