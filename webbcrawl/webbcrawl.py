import os
from astropy.io import fits
import pandas as pd


class webbcrawl():
    
    def __init__(self,path,include_path=False):
    
        hdr_keywords = ['INSTRUME','MODULE','DETECTOR','FILTER','PUPIL','EFFINTTM','SUBARRAY','TARGNAME','PROGRAM']
        hdr_data = []
    
        for root, dirs, files in os.walk(path):
            for ff in files:
                if ff[-4:]=='fits':
                    ffpath = os.path.join(root,ff)
                    hdr = fits.getheader(ffpath)
                    hdr_dict = {}

                    for keyword in hdr_keywords:
                        if keyword in hdr.keys():
                            hdr_dict[keyword] = hdr[keyword]
                        else:
                            hdr_dict[keyword] = 'none'
                        
                    if include_path:
                        hdr_dict['PATH'] = ffpath
                    hdr_data.append(hdr_dict)
               
            
        df = pd.DataFrame.from_dict(hdr_data,orient='columns')
    
        pd.set_option('display.max_colwidth', None)
        print(df)
    
#webbcrawl('/Users/pontoppi/commissioning/data/NRC899',include_path=True)