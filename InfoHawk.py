#welcome to OSINT tool , if there is any bug you can Contact me on instagram : {h7ow_9}

import requests
import wikipedia
from googlesearch import search




print()

def convert_to_username(name):
    lowercase_name = name.lower()
    
    parts = lowercase_name.split()
    
    if len(parts) == 3:
    
        username = parts[0]+ "." + parts[1]+ parts[2]
    
    elif len(parts) == 2:
    
        username = parts[0] + "." + parts[1]
    
    elif len(parts) == 1:  
        username = lowercase_name

    else:
    
        print("Invalid name format. Please provide a name with 2 or 3 parts.")
    
        return None
    
    return username







def FaceBook(username):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        
        # Check if the 'name' field is in the data
        if username in data:
            return f"[+] {inputFiled} in Facebook {url}"
        
   



def INSTA(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        global inputFiled

        if inputFiled in data:
            return f"[+] {inputFiled} in Instagram {url}"
        

def TWITTER(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        
        if username in data:
            return f"[+] {inputFiled} in Twitter {url}"

    else : 
        return f"[+] {inputFiled} in Twitter {url}"
    
    
def YOUTUBE(username):
    url = f"https://www.youtube.com/@{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        
        if username in data:
            return f"[+] {inputFiled} in Youtube {url}"


def GITHUB(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        
        if username in data:
            return f"[+] {inputFiled} in GetHub {url}"
        


def TIKTOK(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        
        if username in data:
            return f"[+] {inputFiled} in Tiktok {url}"        





def search_wikipedia(query):
    try:
        search_results = wikipedia.search(query)

        if search_results:
            page_title = search_results[0]
            
            page_url = wikipedia.page(page_title).url
            
            return page_url
        else:
            return "No results found for the query."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error: {e}"
    except wikipedia.exceptions.PageError:
        return "Page does not exist."



import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=5):
    try:
        search_results = []
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        search_items = soup.find_all("div", class_="tF2Cxc")
        for item in search_items:
            link = item.find("a")["href"]
            title = item.find("h3").get_text()
            search_results.append((title, link))
        return search_results
    except Exception as e:
        return f"An error occurred: {e}"





def draw_infohawk():
    infohawk_art = """
  ___        __       _   _                _     
 |_ _|_ __  / _| ___ | | | | __ ___      _| | __ 
  | || '_ \| |_ / _ \| |_| |/ _` \ \ /\ / / |/ / 
  | || | | |  _| (_) |  _  | (_| |\ V  V /|   <  
 |___|_| |_|_|  \___/|_| |_|\__,_| \_/\_/ |_|\_\ 
    """
    print(infohawk_art)

# Call the function to draw InfoHawk
draw_infohawk()

print("welcome to infohawk v1.0.0 -Hussien Alzaghateet")
print()
print('[0] FaceBook')
print('[1] Instagram')
print('[2] Youtube')
print('[3] Twitter')
print('[4] GitHub')
print('[5] Tiktok')
print('[6] wikipedia search')
print('[7] google search')
print('[8] All platforms')
print('[99] Exit')
print()
print()
print()
print()
option=str(input('[-] select an option : '))

if option == '0' :
    inputFiled = input("[-] Input your Target name :- ")
    username = convert_to_username(inputFiled)
    FaceBook_Result = FaceBook(username)
    print(FaceBook_Result)

elif option == '1' :
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    Instagram_Result = INSTA(inputFiled)
    print(Instagram_Result)
    
elif option =='2' : 
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    YouTube_Result = YOUTUBE(inputFiled)
    print(YouTube_Result)

elif option =='3' :
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    Twitter_Result = TWITTER(inputFiled)
    print(Twitter_Result)

elif option =='4' :
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    GetHub_Result=GITHUB(inputFiled)
    print(GetHub_Result)

elif option =='5' :
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    Tiktok_Result=TIKTOK(inputFiled)
    print(Tiktok_Result)


elif option == '6' :
    print("warning : Put what you want to search for between \"\"  ")
    print()
    print()
    query = input("Enter the word you want to search about on Wikipedia : ")
    result = search_wikipedia(query)
    print(result)

elif option == '7' : 
    print("warning : Put what you want to search for between \"\"  ")
    print()
    print()
   
    Google_search_Result = input("Enter what you want seacrh on Google: ")


    results = google_search(Google_search_Result)


    for i, (title, link) in enumerate(results, start=1):
        print(f"{i}. {title}")
        print(link)
        print()





elif option =='8' :
    inputFiled = input("Input your Target name :- ")
    username = convert_to_username(inputFiled)
    FaceBook_Result = FaceBook(username)
    print(FaceBook_Result)
    Instagram_Result = INSTA(inputFiled)
    print(Instagram_Result)
    Twitter_Result = TWITTER(inputFiled)
    print(Twitter_Result)
    YouTube_Result = YOUTUBE(inputFiled)
    print(YouTube_Result)
    GetHub_Result=GITHUB(inputFiled)
    print(GetHub_Result)
    Tiktok_Result=TIKTOK(inputFiled)

elif option == '99' :
    exit() 

else :
    print("Wrong option")





