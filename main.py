from pdf import create_pdf
from voice import speak

pdf = create_pdf('STEPHEN HAWKING BREVE HISTORIO DO TEMPO.pdf')

for page in pdf:
    speak(page)
