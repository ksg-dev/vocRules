from PyPDF2 import PdfReader
from pprint import pprint
import re

reader = PdfReader("rules/r1113.pdf")
pages = reader.pages
outline = reader.outline

# for page in pages:
#     print(page.extract_text())



# def get_def_destination():
#     for head in outline:
#         if "Definitions" in head["/Title"]:
#             dest_data = {
#                 "page": head["/Page"],
#                 "title": head["/Title"]
#             }
#             return dest_data


def get_text():
    with open("1113.txt", "w", encoding='utf8') as file:
        for page in pages:
            file.write(page.extract_text())

    print("All Done!")

def process_file():
    my_terms = []
    with open("1113.txt", "r", encoding="utf8") as file:
        lines = file.read()
        defs = re.split('\([0-9]{1,2}\)', lines)
    print(f"LENGTH: {len(defs)}")
    for definition in defs:
        definition.strip()
        # print('+++++', repr(definition))
        pattern = re.compile('[a-z]')
        print(f"def:{definition}")
        split_index = pattern.search(definition).span()
        print(pattern.search(definition))
        print(f"SPLIT INDEX: {split_index}")
        print("------------------")
    #     new_term = {
    #         "term": term,
    #         "text": text
    #     }
    #     my_terms.append(new_term)
    #
    # print(my_terms)



# get_text()
process_file()

