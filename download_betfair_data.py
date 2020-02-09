import urllib.request
import requests
import re
import glob
import pandas as pd
import os

path = 'C:\\Users\\user\\Desktop\\python\\'
path_data = path + 'betfair_data'
url = 'http://promo.betfair.com/betfairsp/prices'
prices_folder = 'data'



# --------------------- 

request = requests.get(url)
open(path + 'site.txt', 'wb').write(request.content)

with open(path+'site.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
links = re.findall( r'/betfairsp/prices/(.*?).csv', data)

files_list = []
for filename in glob.glob(os.path.join(path_data, '*.csv')):
    files_list.append(filename[filename.rfind('\\')+1:-4])

links_new = list(set(links) - set(files_list))
links_new = [link for link in links_new if link.find('uk')>-1]
i = 0

for link in links_new:
    if i % 1000 == 0:
        print (f'done links: {i}')

    request = requests.get(url+'/'+link+'.csv')
    open(path_data + '\\' + link + '.csv', 'wb').write(request.content)
    i += 1
    
# -----------------------
    
df = pd.DataFrame()
i = 0
for filename in glob.glob(os.path.join(path_data, '*.csv')):
    if filename.find('uk') >= 0:
        if i <1000:
            if i % 1000 == 0:
                print (f'done uploading: {i}')
                
            
            df = pd.concat([df, pd.read_csv(filename, usecols = [i for i in range(16)])])
            
            i += 1
            
            
        
        
        
        
        
        
        
        
        
        
        