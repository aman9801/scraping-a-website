# Importing required packages
import  requests, bs4
import glob

# Storing the data to res after sending a request
print("Requesting the data from website...")
res = requests.get('https://assignment-1-part-1.amangupta51.repl.co/')

# Parsing the data received
print("Parsing the data...")
parseSoup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = parseSoup.select('#bio')
bio_data = elems[0].getText()

# Storing the final output to a text file
print("Storing the data into a text file - bio_data.txt\n")
file1 = open("bio_data.txt","w")
file1.writelines(bio_data)
file1.close()

# Assigning the file url(s) to variable(s)
url1 = 'https://assignment-1-part-1.amangupta51.repl.co/docs/resume.pdf'
url2 = 'https://assignment-1-part-1.amangupta51.repl.co/docs/certi.pdf'
url3 = 'https://assignment-1-part-1.amangupta51.repl.co/docs/lor.docx'

# Requesting the files from url(s)
print("Requesting the files from website...")
r1 = requests.get(url1, allow_redirects=True)
r2 = requests.get(url2, allow_redirects=True)
r3 = requests.get(url3, allow_redirects=True)

# Storing the files to a folder
print("Storing the files into a folder - docs\n")
open('docs/resume.pdf', 'wb').write(r1.content)
open('docs/certi.pdf', 'wb').write(r2.content)
open('docs/lor.docx', 'wb').write(r3.content)

# Creating an empty list
list_of_files = []

# Retrieving the files name from folder docs
print("Retrieving the files name from a folder")
for name in glob.glob('docs/*'):
    name = name.split("/")[1]
    list_of_files.append(name)

# Storing the files name into a text file
print("Storing the files name into a text file - list_of_files.txt")
with open('list_of_files.txt', 'w') as f:
  for files in list_of_files:
    f.write(files + '\n')
