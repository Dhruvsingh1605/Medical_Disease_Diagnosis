
import cgi
import os
import cgitb

cgitb.enable() 

# Retrieve form data
form = cgi.FieldStorage()
name = form.getvalue('name', 'Not Provided')
age = form.getvalue('age', 'Not Provided')
gender = form.getvalue('gender', 'Not Provided')
blood_group = form.getvalue('blood_group', 'Not Provided')
allergies = form.getvalue('allergies', 'Not Provided')
medical_history = form.getvalue('medical_history', 'Not Provided')
symptoms = form.getvalue('symptoms', 'Not Provided')

data_file = "/media/dhruv/Local Disk/Speech_Trial/Front-End-Trial/form_data.txt"  
with open(data_file, 'a') as file:
    file.write(f"Name: {name}, Age: {age}, Gender: {gender}, Blood Group: {blood_group}, "
               f"Allergies: {allergies}, Medical History: {medical_history}, Symptoms: {symptoms}\n")

print("Content-Type: text/html\n")
print("<html>")
print("<head><title>Form Submission</title></head>")
print("<body>")
print("<h1>Form Submitted Successfully!</h1>")
print(f"<p><strong>Name:</strong> {name}</p>")
print(f"<p><strong>Age:</strong> {age}</p>")
print(f"<p><strong>Gender:</strong> {gender}</p>")
print(f"<p><strong>Blood Group:</strong> {blood_group}</p>")
print(f"<p><strong>Allergies:</strong> {allergies}</p>")
print(f"<p><strong>Medical History:</strong> {medical_history}</p>")
print(f"<p><strong>Symptoms:</strong> {symptoms}</p>")
print("</body></html>")
