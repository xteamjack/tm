import ollama

# get data model
print('Reading data model...\r')
file = open("D:/wspc3/github/TalentMap/data/model/candadate.md", "r")
content = file.read()
file.close()
print ("...done")

prompt = "Generate mock data for an Indian candidate resume in the JSON format. Data should exactly match the following structure. Do not generate any extra fields. Generated response should have only JSON data, no extra text or hints\n" + content 

print('Generating mistral response...\r')
response = ollama.generate(model='mistral', prompt=prompt)
f = open("mistral.txt", "w")
f.write("Mistral\n" + response["response"])
f.close()
print ("...done")

print('Generating llama3.2 response...\r')
response = ollama.generate(model='llama3.2', prompt=prompt)
f = open("llama.txt", "w")
f.write("llama3.2\n" + response["response"])
print ("...done")