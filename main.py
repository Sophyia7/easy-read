import pyttsx3
import PyPDF2

# This opens the PDF file
book = open('django-admin-cookbook.pdf', 'rb')
pdfRead = PyPDF2.PdfFileReader(book)
pages = pdfRead.numPages

full_content = ""

# This reads the PDF file
speaker = pyttsx3.init()
speaker.setProperty("rate", 140)
for num in range(pages):
    page = pdfRead.getPage(num)
    text = page.extractText()
    full_content += text

speaker.save_to_file(text, "myaudio.mp3")
speaker.runAndWait()