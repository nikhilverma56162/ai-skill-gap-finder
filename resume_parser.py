import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = ["Python", "Java", "SQL", "Machine Learning", "Deep Learning",
          "NLP", "TensorFlow", "PyTorch", "Pandas", "NumPy", "API"]

def extract_skills(text):
    doc = nlp(text)
    found_skills = []

    for token in doc:
        if token.text in SKILLS:
            found_skills.append(token.text)

    return list(set(found_skills))