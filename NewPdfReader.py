# import os
# import PyPDF2

# # source_folder = 'D:\dataset_resume'
# # combined_txt_path = 'D:/FinalTest/finalText.txt'

# # Create a list to store text from all PDF files
# all_pdf_text = []
# #/content/finalTest.json

# # Loop through PDF files in the source folder
# for filename in os.listdir(source_folder):
#     if filename.endswith('.pdf'):
#         pdf_path = os.path.join(source_folder, filename)

#         # Extract text from PDF
#         with open(pdf_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfReader(pdf_file)
#             pdf_text = ' '.join(page.extract_text() for page in pdf_reader.pages)
#             all_pdf_text.append(pdf_text)

# # Combine all PDF text into a single string
# combined_text = '\n\n'.join(all_pdf_text)  # Adding double newline separator

# # Save combined text to a single TXT file
# with open(combined_txt_path, 'w', encoding='utf-8') as combined_txt_file:
#     combined_txt_file.write(combined_text)