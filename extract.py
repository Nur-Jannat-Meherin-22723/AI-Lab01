'''import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text = []
        
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
            
        
        return pdf_text

if __name__== '__main__':
    extracted_text = extract_text_from_pdf('download0.pdf')
    for text in extracted_text:
        print(text)
'''

import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []
        
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
            
        return pdf_text

if __name__ == '__main__':
    pdf_path = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download0.pdf'
    extracted_text = extract_text_from_pdf(pdf_path)
    
    for text in extracted_text:
        print(text)
