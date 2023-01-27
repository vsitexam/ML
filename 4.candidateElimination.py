#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


#Loading data from a csv file.
data = pd.DataFrame(data=pd.read_csv('D:\Set\Important\Downloads\enjoysport.csv'))
print(data)


# In[9]:


#Separating concept features from Target
concepts = np.array(data.iloc[:,0:6])
print(concepts)


# In[10]:


#Isolating target into a separate DataFrame
#Copying last column to target  array
target = np.array(data.iloc[:,6])
print(target)


# In[11]:


#
def learn(concepts, target): 
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and genearal_h")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
                   
        if target[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
        print("Generic Boundary after ", i+1, "Instance is ", general_h)
        print("\n")

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        general_h.remove(['?', '?', '?', '?', '?', '?']) 
    return specific_h, general_h 

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")

