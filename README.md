# CSFtoPDF
This will allow for a CSV file to be converted into a Storyboard PDF file

DEPENDENCIES:

	-Download fpdf for python
	-Download "DejaVu" font family and place into Mac System files

COMMAND LINE:

	Example formatting for the terminal command that will create the Storyboard PDF file:

		python3 MAKE_STORYBOARD.py {csv_file} {output_pdf_name}

CSV FILE FORMATTING:

	The CSV file should be formatted into two columns, the first column for 
	the frame captions and the second for the frame descriptions. There should not be column 
	headers that specify which is which.
	

