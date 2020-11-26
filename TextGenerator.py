import easyocr
import torch
L1 =['Bihari','Assamese','Arabic','Bengali','Bhojpuri','Hindi','Maithili','Marathi','Nepali','English','Tamil']
L2 =['bh','as','ar','bn','bho','hi','mai','mr','ne','en','ta']
mp = dict(zip(L1,L2))
def get_label(file_path,lang):
    reader = easyocr.Reader([mp[lang],'en'])
    result = reader.readtext(file_path)
    return result
