import easyocr
reader = easyocr.Reader(lang_list=['ch_sim','en'], download_enabled=False) # this needs to run only once to load the model into memory
result = reader.readtext('chinese.jpg')
print(result)