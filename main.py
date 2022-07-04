from bs4 import BeautifulSoup
from time import sleep

print("#######################################################")
with open(input("Enter the name of html file:"),'r',encoding="utf8") as f:
    html_file = f.read()

soup = BeautifulSoup(html_file,'lxml')   
nameTag = soup.find("h1")
titleTag = soup.find("div",class_='text-body-medium')

with open("database.txt","a") as file1:
    file1.write(nameTag.text)
    file1.write(titleTag.text.replace(" ",""))
    file1.write("================================\n")
    file1.close()

print("############Storing the details in Database############")
sleep(2)