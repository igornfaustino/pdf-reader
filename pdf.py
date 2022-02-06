import pdftotext

def create_pdf(path: str):
    with open(path, "rb") as f:
        return pdftotext.PDF(f)

