import ollama
from  report_creator import create_pdf

def prompt(value1,value2):
    desired_model = 'llama3.2:3b'
    ask = "How much will you rate this resume and if any link present, open and look it and provide ratings in aspect of Character,Knowledge,Experience,Overall.Provide rating to all at scale of 10.Provide output in form of Name: ,Character: ,Knowledge: ,Experience: ,Overall: , and only numeric rating, no text for all aspects and no note.  " + str(value1)+str(value2)
    
   
    response = ollama.chat(model=desired_model, messages=[{
        'role': 'user',
        'content': ask,
    }])

    final = response['message']['content']
    create_pdf('resume_report.pdf',final)
