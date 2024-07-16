#Read the configuration file and create and write to a ".txt" file where the URLs and their names will be placed
import os
from colorama import init, Fore, Style
from utils.clear import ClearConsole


def read_conf_file(conf_path):
    config = {}
    with open(conf_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def process_pdfs(DIR, base_url,abbreviation,year):
    print()
    links = [] 
    ArchElements = os.listdir(DIR) 

    for el in ArchElements:
                if abbreviation =='':
                    link = base_url+f'{year}-mon/' + el
                    links.append(link)
                else:
                    link = base_url+f'{abbreviation}/{year}-mon/' + el
                    links.append(link)
                ClearConsole()

    with open(os.path.join(DIR,'all_links.txt'), 'w') as links_file:
            for link in links:
                links_file.write(link + '\n')

        
    

