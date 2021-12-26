#This code will be used to convert CSV files into the PDF Format specified

#built-in python csv module
import csv
import sys
from PDF_CLASS import PDF

#csv file to convert to pdf
#ERROR HANDLING: Checks if the terminal command is propery formatted
try:
    file_name = sys.argv[1]
    output_filename = sys.argv[2]
    #ERROR HANDLING: Checks if the output file has the .pdf file extension.
    if not (output_filename.endswith('.pdf')):
        print("Remember to add the .pdf file extension!")
        exit()

except:
    print("The format of this terminal command is incorrect. Check the README file for the format.")
    exit()
    
table_data = []

#ERROR HANDLING: Checks if the CSV file specified exists
try:
    with open(file_name, 'r', encoding = 'utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            #ERROR HANDLING: Checks if the formatting is correct. Only two columns, one for captions and one for frame descriptions
            if (len(row) != 2):
                print("The CSV file doesn't appear to be formatted correctly. There may be too many, or too few, columns. Check the README file for the format.")
                exit()
            else:
                table_data.append(row)
except FileNotFoundError:
    print("Could not find this CSV file.")
    exit()
    
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










            
            
            
            