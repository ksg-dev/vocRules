from PyPDF2 import PdfReader
from pprint import pprint

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
    with open("1113.txt", "w") as file:
        for page in pages:
            file.write(page.extract_text())

    print("All Done!")

get_text()

