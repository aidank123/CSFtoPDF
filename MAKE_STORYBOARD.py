#This code will be used to convert CSV files into the PDF Format specified

#built-in python csv module
import csv
import sys
from PDF_CLASS import PDF

#csv file to convert to pdf
file_name = sys.argv[1]
output_filename = sys.argv[2]

table_data = []
with open(file_name, 'r', encoding = 'utf-8') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        table_data.append(row)

#create pdf_class object using the imported table data
pdf_class_obj = PDF(table_data,output_filename)
#call method that will generate the pdf storyboard frames
pdf_class_obj.generate_storyboard_frames()

# #testing text
# txt = 'start ssssss sssss ss ss   ssssssssssss ssss ss s s s s ssssssss ss s s s s s ssssssssssssssss s s yjgjhghfghjk lhgfdhjklkl hjkgfd sdfgjhjklhjkghfgdf dhfjhgkjhl kj ssssssss ss  ssssssss ssssssss end'
# # variable pdf
# pdf = FPDF()
#         
# 
# 
#  


#drawing template that will contain each storyboard frame










            
            
            
            