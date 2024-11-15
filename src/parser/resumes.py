import glob
import sys
import os
import time

from dotenv import load_dotenv
load_dotenv()

store_path = os.getenv('STORE_PATH')

print ("Resume parser")
print (f'Parsing {sys.argv[1]}')
dir_path = sys.argv[1] #+ "/*.pdf"
file_names = glob.glob(dir_path)
print (f'... found {len(file_names)} file(s)')

counter = 1
for file in file_names:
    action="[processing]"
    # Generate unique identifier for resume
    import uuid
    profile_id = str(uuid.uuid4())
    sys.stdout.write(f'... {counter:5} : {profile_id} {action:^15} {os.path.basename(file):25} \r')
    profile_path = f'{store_path}/{profile_id}'

    from datetime import date
    current_date = date.today()
    file_stamp = f'{current_date.year}_{current_date.month}_{current_date.day}'

    # Create destination folder
    os.mkdir(profile_path)

    # # Read resume pdf 
    # from PyPDF2 import PdfReader, PdfWriter, PdfFileReader
    # reader = PdfReader(file)

    # writer = PdfWriter()

    # resume_text = []
    # for page in reader.pages:
    #     writer.add_page(page)
    #     resume_text.append(page.extract_text())

    # # save resume with password
    # # writer.encrypt("junkinfo")
    # writer.write(f'{profile_path}/resume_{file_stamp}.pdf')

    # # save resume text
    # with open(f'{profile_path}/resume_{file_stamp}.txt', "w", encoding="utf-8") as resume_text_file:
    #     resume_text_file.write('\n'.join(resume_text))

    with open(file, "r") as resume_md:
        resume_text = resume_md.read()

    print(resume_text)

    with open("D:/wspc3/github/TalentMap/data/model/candadate.md", "r") as candidate_model_file:
        candidate_mode = candidate_model_file.read()
    # Extract data in text format and save to file
    import ollama

    # prompt = f'Given the resume of a candidate that contains various details in markdown format, you need to extract the detail matching with the candidate data model and generate a json structure as per the candidate data model\nResume:{resume_text}\nCandidate Data Model:{candidate_mode}. Final output needs to be expressed as a JSON structure matching the Candidate data model with utmost accuracy.  Leave fields blank if the corresponding data items not found in the resume'

    prompt = f'You are a senior recruiter. Your job is to scans and parsers candidate resumes to validate all the key data provided in them. Given the resume of the candidate in markdown format, you need to extract all the key details as per the candidate data model and generate a JSON file\n Resume:{resume_text}\nCandidate data model:{candidate_mode}\n. Job needs to be performed with utmost accuracy.'

    response = ollama.generate(model='llama3.2', prompt=prompt)
    with open(f'{profile_path}/resume_llama_{file_stamp}.json', "w", encoding="utf-8") as resume_json_file:
        resume_json_file.write(response["response"])

    response = ollama.generate(model='mistral', prompt=prompt)
    with open(f'{profile_path}/resume_mistral_{file_stamp}.json', "w", encoding="utf-8") as resume_json_file:
        resume_json_file.write(response["response"])

    response = ollama.generate(model='gemma', prompt=prompt)
    with open(f'{profile_path}/resume_gemma_{file_stamp}.json', "w", encoding="utf-8") as resume_json_file:
        resume_json_file.write(response["response"])

    # time.sleep(1)
    # action="[parsing]"
    # sys.stdout.write(f'... {counter:5} : {profile_id} {action:^15} {os.path.basename(file):25}\r')
    # time.sleep(1)
    # action="[validating]"
    # sys.stdout.write(f'... {counter:5} : {profile_id} {action:^15} {os.path.basename(file):25}  \r')
    # time.sleep(1)
    # action="[saving]"
    sys.stdout.write(f'... {counter:5} : {profile_id} {action:^15} {os.path.basename(file):25}  \n')
    # time.sleep(1)
    sys.stdout.flush()
    counter=counter+1