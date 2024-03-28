import pyttsx3,PyPDF2    #imports the two python libraries: pyttsx is a py library that is used for text to speech; PyPDF2 is a py library that is used with pdf files

pdfRead = PyPDF2.PdfReader(open('book.pdf', 'rb'))  #rb is to 'read the file in binary mode'
speak = pyttsx3.init() #initializes the speak from the library


# for loop used to iterate through each page of a PDF document, extract all the text from each page, clean up the text by removing unnecessary whitespaces and line breaks, and then print the cleaned text to the console

for page_num in range(pdfRead.numPages):                
    text = pdfRead.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)


#the clean text is then spoken 
speak.save_to_file(clean_text, 'story.mp3')
#After initiating the saving of the text to an audio file, this line tells the pyttsx3 engine to process the speech conversion and waits for the task to complete.
speak.runAndWait() 


speak.stop()

