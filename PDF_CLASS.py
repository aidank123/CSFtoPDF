#PDF CLASS

#filepath to fonts
font_filepath = '/Users/aidankelley/Library/Fonts/DejaVuSansCondensed.ttf'

#python pdf module
from fpdf import FPDF

pdf = FPDF()

#All measurements are in mm 

WIDTH = 210 #width of page
HEIGHT = 297 #height of page

#VARIABLES USED TO FORMAT THE PAGE CELLS AND GENERAL FORMATTING.
#These can be adjusted to uniformly change the page (to a certain extent)

#margin from left side of page for each storyboard rectangle
x_margin = 2
#y-axis placement of each storyboard rectangle, in order from top, middle, bottom of the page (index 0,1,2)
y_margins = [(2),(HEIGHT/3 + 2),(2*(HEIGHT/3) + 2)]
#width of each storyboard rectangle
rect_width = WIDTH - 4
#height of each storyboard rectangle
rect_height = HEIGHT/3 - 4
#height of frame description cell
description_height =  20
#width of frame caption cell
caption_width = 70
#y-offset when putting text in the frame description cell
#description_y_offset = 75 #val with old cells 
description_y_offset = 80
#y-offset when putting text in the frame caption cell
caption_y_offset = 20
#text spacing value
line_height = 4

class PDF:
    
    def __init__(self,captions_descriptions,output_filename):
        self.captions_descriptions = captions_descriptions
        self.output_filename = output_filename
    def first_frame(self,input):
        #first block on page
        pdf.rect(x_margin,y_margins[0],rect_width,rect_height)
        pdf.line(x_margin + caption_width, y_margins[0],x_margin + caption_width, y_margins[0] + rect_height - description_height)
        pdf.line(x_margin, y_margins[0] + rect_height - description_height , WIDTH - x_margin, y_margins[0] + rect_height - description_height)
        
        #first frame caption
        pdf.set_y(y_margins[0] + caption_y_offset)
        pdf.set_x(x_margin + 2)
        pdf.multi_cell(caption_width - 2, line_height,txt = input[0], border = 0, align = 'L', fill = False)
        #first frame description
        pdf.set_y(y_margins[0] + description_y_offset)
        pdf.set_x(x_margin + caption_width)
        pdf.multi_cell(rect_width  - caption_width, line_height,txt = input[1], border = 0, align = 'L', fill = False)
        
    def second_frame(self,input):
        #second block on page
        pdf.rect(x_margin,y_margins[1],rect_width,rect_height)
        pdf.line(x_margin + caption_width, y_margins[1],x_margin + caption_width, y_margins[1] + rect_height - description_height)
        pdf.line(x_margin, y_margins[1] + rect_height - description_height , WIDTH - x_margin, y_margins[1] + rect_height - description_height)
        
        #second frame caption
        pdf.set_y(y_margins[1] + caption_y_offset)
        pdf.set_x(x_margin + 2)
        pdf.multi_cell(caption_width - 2, line_height,txt = input[0], border = 0, align = 'L', fill = False)
        #second frame description
        pdf.set_y(y_margins[1] + description_y_offset)
        pdf.set_x(x_margin + caption_width)
        pdf.multi_cell(rect_width  - caption_width, line_height,txt = input[1], border = 0, align = 'L', fill = False)
        
    def third_frame(self,input):
        #third block on page
        pdf.rect(x_margin,y_margins[2],rect_width,rect_height)
        pdf.line(x_margin + caption_width, y_margins[2],x_margin + caption_width, y_margins[2] + rect_height - description_height)
        pdf.line(x_margin, y_margins[2] + rect_height - description_height , WIDTH - x_margin, y_margins[2] + rect_height - description_height)
        
        #third frame caption
        pdf.set_y(y_margins[2] + caption_y_offset)
        pdf.set_x(x_margin + 2)
        pdf.multi_cell(caption_width - 2, line_height,txt = input[0], border = 0, align = 'L', fill = False)
        #third frame description
        pdf.set_auto_page_break(False) #necessary because auto page breaks are occuring for some reason 
        pdf.set_y(y_margins[2] + description_y_offset)
        pdf.set_x(x_margin  + caption_width)
        pdf.multi_cell(rect_width - caption_width, line_height,txt = input[1], border = 0, align = 'L', fill = False)   
        pdf.set_auto_page_break(True)
         
    def number_frame_1(self,frame_number):
        pdf.set_y(y_margins[0] + 2)
        pdf.set_x(x_margin + 2)
        pdf.write(line_height,txt = frame_number)
    def number_frame_2(self,frame_number):
        pdf.set_y(y_margins[1] + 2)
        pdf.set_x(x_margin + 2)
        pdf.write(line_height,txt = frame_number)
    def number_frame_3(self,frame_number):
        pdf.set_y(y_margins[2] + 2)
        pdf.set_x(x_margin + 2)
        pdf.write(line_height,txt = frame_number)
        
    def generate_storyboard_frames(self):
        
        num_of_frames = len(self.captions_descriptions)
        
        for i in range(num_of_frames):
            
            if((i == 0) or (i % 3 == 0)):
                # Add a page. A4 format by default.
                pdf.add_page()
                # set style and size of font
                pdf.add_font('DejaVu', '', font_filepath, uni=True)
                pdf.set_font("DejaVu",'', size = 12)
                self.first_frame(self.captions_descriptions[i])
                self.number_frame_1(str(i + 1))
            elif((i == 1) or (i % 3 == 1)):
                self.second_frame(self.captions_descriptions[i])
                self.number_frame_2(str(i + 1))
            elif((i == 2) or (i % 3 == 2)):
                self.third_frame(self.captions_descriptions[i])
                self.number_frame_3(str(i + 1))
            
        self.output_pdf()
        
    def output_pdf(self):
        # save the pdf with the name chosen
        pdf.output(self.output_filename)
        print("Success!")
        