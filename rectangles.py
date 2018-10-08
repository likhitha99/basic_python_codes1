
# coding: utf-8

# In[31]:


import cv2
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import imutils
import ctypes


# In[15]:


img=np.zeros((600,600,3),np.uint8)
img[:]=255
l,w=100,150
for angle in np.arange(0,90,20):
    x,y=np.random.randint(200,400,2)
    s,t=np.random.randint(200,400,2)
    
    phi=angle
    rho = 100
    
    m = rho * np.cos(phi)
    b = rho * np.sin(phi)
    o=x+m
    p=y+b
    q=s-m
    r=t-b
    vrx=np.array(([x,y],[q,r],[s,t],[o,p]))
    
    
    img=cv2.polylines(img,np.int32([vrx]), True, (0,0,0),3)
    
    #img=cv2.rectangle(img,(x,y),(s,t),(0,0,0),3)
    plt.imshow(img)

    #filename="rect"+str(i)+".png"
    #cv2.imwrite(filename,img)
    #cv2.imwrite()
    plt.show()
    img[:]=255



# In[18]:



img=np.zeros((600,600,3),np.uint8)
img[:]=255

for angle in np.arange(0,360,20):
    
    x,y=np.random.randint(200,400,2)
    s,t=np.random.randint(200,400,2)
    
    phi=angle
    rho = 100
    
    m = rho * np.cos(phi)
    n = rho * np.sin(phi)
    o=x+m
    p=y+n
    q=s-m
    r=t-n
    #dist = numpy.linalg.norm(a-b)
    
    vrx=np.array(([x,y],[q,r],[s,t],[o,p]))
    vrx=vrx.reshape((-1,1,2))
    img=cv2.polylines(img,np.int32([vrx]), True, (0,0,0),3)
    
    #img=cv2.rectangle(img,(x,y),(s,t),(0,0,0),3)
    plt.imshow(img)

    #filename="rect"+str(i)+".png"
    #cv2.imwrite(filename,img)
    #cv2.imwrite()
    plt.show()
    img[:]=255


# In[43]:


img=np.zeros((600,600,3),np.uint8)
img[:]=255
for angle in np.arange(0,360,20):
    x,y=np.random.randint(1,400,2)
    s,t=np.random.randint(1,400,2)
    a,b=np.random.randint(1,400,2)
    c,d=np.random.randint(1,400,2)
    
    phi=angle
    x=(x*np.cos(phi)-y*np.sin(phi))+a
    y=(x*np.sin(phi)+y*np.cos(phi))+b
    s=(s*np.cos(phi)-t*np.sin(phi))+c
    t=(s*np.sin(phi)+t*np.cos(phi))+d
    rho = 100
    
    m = rho * np.cos(phi)
    n = rho * np.sin(phi)
    o=x+m
    p=y+n
    q=s-m
    r=t-n
    dist=
    vrx=np.array(([x,y],[q,r],[s,t],[o,p]))
    vrx=vrx.reshape((-1,1,2))
    img=cv2.polylines(img,np.int32([vrx]), True, (0,0,0),3)
    
    
    
    #img=cv2.rectangle(img,(x,y),(s,t),(0,0,0),2)
    plt.imshow(img)
    plt.show()
    img[:]=255
    
    
    


# In[51]:



x,y=np.random.randint(1,400,2)
s,t=np.random.randint(1,400,2)
a,b=np.random.randint(1,400,2)
c,d=np.random.randint(1,400,2)
    
phi=angle
x=(x*np.cos(phi)-y*np.sin(phi))+a
y=(x*np.sin(phi)+y*np.cos(phi))+b
s=(s*np.cos(phi)-t*np.sin(phi))+c
t=(s*np.sin(phi)+t*np.cos(phi))+d
rho = 100
    
m = rho * np.cos(phi)
n = rho * np.sin(phi)
o=x+m
p=y+n
q=s-m
r=t-n
g=[x,y]
h=[q,r]
distance = np.sqrt(np.sum(np.square(g-h)))
    
    
    
    

