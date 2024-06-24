import os
from colorama import init, Fore, Style
def read_conf_file(conf_path):
    config = {}
    with open(conf_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def process_pdfs(DIR, base_url):
    print()
    links = [] 
    ArchElements = os.listdir(DIR) 
    for el in ArchElements:
            print(
f'''{Fore.YELLOW}{el} - {Fore.RESET}URL: {Fore.GREEN}{base_url}{Fore.RESET}         
{Fore.CYAN}------------------------------------------------------------------------------------------{Fore.RESET}''')
            abbreviation= input(f'{Fore.MAGENTA}Write abbreviation: {Fore.RESET}')
            year= input(f'{Fore.MAGENTA}Write the year of PDF: {Fore.RESET}')
            if abbreviation =='':
                link = base_url+f'{year}-mon/' + el
                links.append(link)
            else:
                link = base_url+f'{abbreviation}/{year}-mon/' + el
                links.append(link)
            os.system('cls')

    with open(os.path.join(DIR,'all_links.txt'), 'w') as links_file:
        for link in links:
            links_file.write(link + '\n')
    

