# import PyPDF2
# import os
# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS

# def extract_text_from_pdf(pdf_files: [str]) -> [str]:
#     all_text = []

#     for pdf_file in pdf_files:
#         with open(pdf_file, 'rb') as pdf:
#             reader = PyPDF2.PdfReader(pdf, strict=False)
#             pdf_text = []
            
#             for page in reader.pages:
#                 content = page.extract_text()
#                 pdf_text.append(content)

#             all_text.append(pdf_text)

#     return all_text

# def write_to_text_file(text_list, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for index, extracted_text in enumerate(text_list):
#             file.write(f"Text extracted from {pdf_paths[index]}:\n")
#             for text in extracted_text:
#                 file.write(text)
#             file.write("\n\n")

# def summarize_text(input_file, summary_file, num_sentences=20):
#     nlp = spacy.load("en_core_web_sm")

#     with open(input_file, 'r', encoding='utf-8') as file:
#         text = file.read()

#     doc = nlp(text)

#     sentences = [sent.text for sent in doc.sents if sent.text.strip() != '']

#     # Calculate importance score for each sentence based on token count
#     sentence_scores = {sent: len(sent.split()) for sent in sentences}

#     # Select top N sentences based on importance score
#     top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

#     # Write summarized text to summary file
#     with open(summary_file, 'w', encoding='utf-8') as file:
#         file.write('\n'.join(top_sentences))

# if __name__ == '__main__':
#     pdf_paths = [
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download0.pdf',
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download1.pdf',
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download2.pdf'
#     ]

#     output_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\output_text.txt'
#     summary_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\summary.txt'

#     extracted_text_list = extract_text_from_pdf(pdf_paths)
#     write_to_text_file(extracted_text_list, output_file)

#     summarize_text(output_file, summary_file)

#     print(f"Text summarized and saved to '{summary_file}'.") 

###########################################################################################################################
# import PyPDF2
# import os
# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS

# def extract_text_from_pdf(pdf_files: [str]) -> [str]:
#     all_text = []

#     for pdf_file in pdf_files:
#         with open(pdf_file, 'rb') as pdf:
#             reader = PyPDF2.PdfReader(pdf, strict=False)
#             pdf_text = []
            
#             for page in reader.pages:
#                 content = page.extract_text()
#                 pdf_text.append(content)

#             all_text.append(pdf_text)

#     return all_text

# def write_to_text_file(text_list, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for index, extracted_text in enumerate(text_list):
#             file.write(f"Text extracted from {pdf_paths[index]}:\n")
#             for text in extracted_text:
#                 file.write(text)
#             file.write("\n\n")

# def summarize_text(input_file, summary_file, num_sentences=20):
#     nlp = spacy.load("en_core_web_sm")
    
#     # Increase the max_length limit
#     nlp.max_length = 3000000  # Set this value based on your text length

#     with open(input_file, 'r', encoding='utf-8') as file:
#         text = file.read()

#     doc = nlp(text)

#     sentences = [sent.text for sent in doc.sents if sent.text.strip() != '']

#     # Calculate importance score for each sentence based on token count
#     sentence_scores = {sent: len(sent.split()) for sent in sentences}

#     # Select top N sentences based on importance score
#     top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

#     # Write summarized text to summary file
#     with open(summary_file, 'w', encoding='utf-8') as file:
#         file.write('\n'.join(top_sentences))

# if __name__ == '__main__':
#     pdf_paths = [
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download0.pdf',
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download1.pdf',
#         r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download2.pdf'
#     ]

#     output_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\output_text.txt'
#     summary_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\summary.txt'

#     extracted_text_list = extract_text_from_pdf(pdf_paths)
#     write_to_text_file(extracted_text_list, output_file)

#     summarize_text(output_file, summary_file)

#     print(f"Text summarized and saved to '{summary_file}'.")

###########################################################################################################################

import PyPDF2
import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

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

def summarize_text(input_file, summary_file, max_words=500):
    nlp = spacy.load("en_core_web_sm")
    
    # Increase the max_length limit
    nlp.max_length = 3000000  # Set this value based on your text length

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    doc = nlp(text)

    sentences = [sent.text for sent in doc.sents if sent.text.strip() != '']

    # Calculate importance score for each sentence based on token count
    sentence_scores = {sent: len(sent.split()) for sent in sentences}

    # Select top sentences until the total word count reaches max_words
    total_words = 0
    top_sentences = []

    for sentence in sorted(sentence_scores, key=sentence_scores.get, reverse=True):
        if total_words + len(sentence.split()) <= max_words:
            top_sentences.append(sentence)
            total_words += len(sentence.split())
        else:
            break

    # Write summarized text to summary file
    with open(summary_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(top_sentences))

if __name__ == '__main__':
    pdf_paths = [
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download0.pdf',
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download1.pdf',
        r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\download2.pdf'
    ]

    output_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\output_text.txt'
    summary_file = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\summary.txt'

    extracted_text_list = extract_text_from_pdf(pdf_paths)
    write_to_text_file(extracted_text_list, output_file)

    summarize_text(output_file, summary_file, max_words=500)

    print(f"Text summarized and saved to '{summary_file}'.")

