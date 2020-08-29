#!/usr/bin/env python
# coding: utf-8

# In[5]:


#randomize the images size
import string
import os
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
def assignRandomNames(baseDir):
    for filename in os.listdir(baseDir):
        filepath = baseDir + os.sep + filename
        if os.path.isfile(filepath):
            finalFolder = baseDir
            filenameOnly, file_extension = os.path.splitext(finalFolder + os.sep + filename)
            os.rename(filepath, finalFolder + os.sep + id_generator()+file_extension)
            
            
baseDir ="Desktop/Live Detector/images/pepsi"
assignRandomNames(baseDir)


# In[ ]:




