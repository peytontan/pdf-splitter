import fitz  # PyMuPDF
import os
import sys

file_name=input("What is the file name")

dir_path = os.path.dirname(file_name)
filename=os.path.basename(file_name)
print(dir_path,filename)

# Redirecting stdout to a file
log_file_name = "logs.txt"
log_file_path = os.path.join(dir_path,log_file_name)
sys.stdout = open(log_file_path, "w")

#needs to be words seen in the pdf
# months_to_split=["For the Period January 1-31, 2022",
#                  "For the Period February 1-28, 2022",
#                  "For the Period March 1-31, 2022",
#                  "For the Period April 1-30, 2022",
#                  "For the Period May 1-31, 2022",
#                  "For the Period June 1-30, 2022",
#                  "For the Period July 1-31, 2022",
#                  "For the Period August 1-31, 2022",
#                  "For the Period September 1-30, 2022",
#                  "For the Period October 1-31, 2022",
#                  "For the Period November 1-30, 2022",
#                  "For the Period December 1-31, 2022"]
months_to_split=[]

# accounts_to_split=['235-058442-321',
#                    '235-058584-321',
#                    '235-058586-321',
#                    '235-058587-321',
#                    '235-058588-321',
#                    '235-058627-321',
#                    '235-058628-321',
#                    '235-058629-321']


def split_pdf_by_strings(pdf_path, strings, output_pdf):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Create a new PDF document
    new_pdf = fitz.open()
    
    # Iterate through each page
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text = page.get_text()
        
        # Check if all of the strings exist on this page
        if all(string in text for string in strings):
            print(text, "----- page number ---- ", page_number+1)
            # Append the page to the new PDF
            print("printing from ",page_number+1)
            new_pdf.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)
        
    if new_pdf.page_count > 0:
        new_pdf.save(output_pdf)
        new_pdf.close()
    else:
        print(f"No pages found for the specified strings for '{strings[0]}' and '{strings[1]}'")
    
    pdf_document.close()

# Example usage
# split_pdf_by_strings("example.pdf", ["ABD123", "A#!23"], "output.pdf")


for month in months_to_split:
    for acc in accounts_to_split:
        new_pdf_output = os.path.join(dir_path,f"{acc}_{month}.pdf")
        split_pdf_by_strings(file_name,[acc,month],new_pdf_output)
        print("saved pdf for - "+acc+" - for month of- "+month)