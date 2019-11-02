# Take all the data from user and then calculate average marks , total marks and percentage
Name = input("Enter your name")
Father_name = input("Enter your Father name")
School_name = input("Enter your School name")
Math = int(input("Enter your Math numbers"))
Chemistry = int(input("Enter your Chemistry numbers"))
Physics = int(input("Enter your Physics numbers"))
English = int(input("Enter your English numbers"))
Urdu = int(input("Enter your Urdu numbers"))
Pak_study = int(input("Enter your pak study numbers"))

Average_Marks = (Math + Chemistry + Physics + English + Urdu + Pak_study)/6
Total_Marks = Math + Chemistry + Physics + English + Urdu + Pak_study
Percentage = (Total_Marks/600) * 100

Transcript = """

Name = {}
Father_name = {}
School_name = {}
Math = {}
Chemistry = {}
Physics = {}
English = {}
Urdu = {}
Pak_study = {}
Average_Marks = {}
Total_Marks = {}
Percentage = {}
"""

Transcript = Transcript.format(Name, Father_name, School_name, Math, Chemistry, Physics, English, Urdu, Pak_study, Average_Marks, Total_Marks, Percentage)

print(Transcript)

