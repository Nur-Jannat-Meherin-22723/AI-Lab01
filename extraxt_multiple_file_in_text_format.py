import PyPDF2
import os

def extract_text_from_pdf(pdf_files: [str]) -> [str]:
    all_text = []

    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)
            pdf_text = []
            
            for page in reader.pages:
                content = page.extract_text()
                pdf_text.append(content)

            all_text.append(pdf_text)

    return all_text

def write_to_text_file(text_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, extracted_text in enumerate(text_list):
            file.write(f"Text extracted from {pdf_paths[index]}:\n")
            for text in extracted_text:
                file.write(text)
            file.write("\n\n")

if __name__ == '__main__':
    pdf_paths = [
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download0.pdf',
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download1.pdf',
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download2.pdf'
    ]

    output_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\output_text.txt'
    extracted_text_list = extract_text_from_pdf(pdf_paths)

    write_to_text_file(extracted_text_list, output_file)

    print(f"Text extracted from PDFs has been saved to '{output_file}'.")
