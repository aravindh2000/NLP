 
from pyresparser import ResumeParser
import warnings


warnings.filterwarnings("ignore", category=UserWarning)

 
data = ResumeParser("C:/Users/Aravindh Siva/Downloads/MayankVerma_Mtech_Electrical.pdf").get_extracted_data()




print("Skills:", data["skills"])
