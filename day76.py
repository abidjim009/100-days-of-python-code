from pypdf import PdfWriter, PdfReader

writer=PdfWriter()
num_files=int(input("Enter the number of PDF files to Merge:"))

for i in range(num_files):
    file_name=input(f"Enter the path file {i+1}: ")
    reader=PdfReader(file_name)
    for page in reader.pages:
        writer.add_page(page)

output_file=input("Enter the name for the merged file ")
with open(output_file,'wb') as output:
    writer.write(output)