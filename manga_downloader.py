import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import re
import sys


#Some vars.
url = 'https://www.mangareader.net'
mangaLinks = {}
chapterLinks = {}
chapterNames = {}


#Getting manga name.
if len(sys.argv) >= 2:
	manga = " ".join(sys.argv[1:])
else:
	manga = input("Which manga do you want to search?:")

#Searching for the manga in the "alphabetical" section of the site.
def search(manga):
	counter = 1
	r = requests.get(url+'/alphabetical')
	soup = BeautifulSoup(r.text,'html.parser')
	for item in soup.find(class_="content_bloc2").find_all('li'):
		if manga.lower() in item.get_text().lower():
			print("["+str(counter)+"]",item.get_text())
			mangaLinks[counter] = item.a.get('href')
			counter += 1
	manga_choice(counter)

#Choosing which manga to download.
def manga_choice(counter):
	if counter == 1:
		print("Couldn't find manga.")
		quit()
	elif counter == 2:
		choice = 1
		os.system('reset')
	else:	
		choice = int(input("Which one do you want to download?:"))
		while not choice in mangaLinks:
			choice = int(input("Which one do you want to download?:"))
	show_chapters(choice)



#Going through all of the chapters and showing them/saving.
def show_chapters(choice):
	r = requests.get(url+mangaLinks[choice])
	soup = BeautifulSoup(r.text,'html.parser')
	counter = 1
	for item in soup.find_all('table')[1].find_all('tr')[1:]:
		print("["+str(counter)+"]",item.a.text)
		chapterLinks[counter] = item.a.get('href')
		chapterNames[item.a.get('href')] = item.a.text
		counter += 1
	chapter_choosing()


#Choosing which chapter to download.
def chapter_choosing():
	global multiple
	while True:
		try:
			choice = input("Enter which chapter you want to download: ")
			if choice.count(':') == 1:
				global toDownload
				choice == ":"
				multiple = True
				toDownload = []
				if choice.find(":") == 0:#Colon is at the start of the string.
					for item in chapterLinks:
						if item == int(choice.split(':')[1]):
							break
						else:
							toDownload.append(chapterLinks[int(item)])
				elif ":" in choice[-1]:#Colon is at the end of the string.
					start = int(choice.split(":")[0])
					last = sorted(chapterLinks.keys())[-1] + 1
					for item in chapterLinks:
						toDownload.append(chapterLinks[start])
						start += 1
						if start == last:
							break
				elif len(choice.split(":")) == 2:#Colon is at the middle of the string.
					start = int(choice.split(":")[0])
					end = int(choice.split(":")[1])
					for item in chapterLinks:
						toDownload.append(chapterLinks[start])
						start += 1
						if start == end:
							break
			elif choice.count(':') == 0:
				global url
				multiple = False
				url += chapterLinks[int(choice)]
				break
			else:
				print("Try again.")
			break
		except ValueError:
			pass
	create_folders(choice)



#Creating folder(s)
def create_folders(choice):
	print("Creating folders...")
	if multiple:
		counter = 1
		for item in toDownload:
			if os.path.isdir(manga.title()+'/'+chapterNames[item]):
				pass
			else:
				os.makedirs(manga.title()+'/'+chapterNames[item])
				counter += 1
		if counter == 1:
			print("Folders already exist.")
		else:
			print("Folders created.")
	else:
		path = manga.title()+'/'+chapterNames[chapterLinks[int(choice)]]
		if os.path.isdir(path):
			print("Folders already exist")
		else:
			print("Folders created.")
			os.makedirs(path)
		os.chdir(path)
	download()


#Downloads the manga champter(s).
def download():
	counter = 1
	opener = urllib.request.URLopener()
	user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
	opener.addheader('User-Agent',user_agent)
	print("Downloading...")
	if multiple:
		current_dir = os.getcwd() + '/'
		for item in toDownload:
			os.chdir(current_dir+manga.title()+'/'+chapterNames[item])
			while True:
				r = requests.get(url+item+"/"+str(counter))
				soup = BeautifulSoup(r.text,'html.parser')
				if soup.text == "404 Not Found":
					print("Downloaded chapter {}.".format(re.findall('\d+',chapterNames[item])[0]))
					counter = 1
					break
				else:
					imgLink = soup.find(id="img").get('src')
					imgName = soup.find(class_="c1").text.replace("-","").strip()
					opener.retrieve(imgLink,imgName)
					counter += 1
		print("Finished downloading")
		quit()
	else:
		while True:
			r = requests.get(url+"/"+str(counter))
			soup = BeautifulSoup(r.text,'html.parser')
			if soup.text == "404 Not Found":
				print("Chapter downloaded.")	
				quit()
			else:
				imgLink = soup.find(id="img").get('src')
				imgName = soup.find(class_="c1").text.replace("-","").strip()
				opener.retrieve(imgLink,imgName)
				counter += 1

search(manga)