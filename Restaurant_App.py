#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st




# In[9]:


import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


# In[10]:


import joblib
model = joblib.load("mlmodel.pkl")





st.set_page_config(layout = 'wide')


# In[21]:


scaler = StandardScaler()


# In[22]:


from sklearn.preprocessing import StandardScaler
import joblib

joblib.dump(scaler, 'scaler.pkl')


# In[12]:


st.title("Restaurant Rating Prediction App")


# In[23]:


st.caption("This App helps to predict a Restaurant review class")


# In[24]:


st.divider()


# In[25]:


averagecost = st.number_input("Please enter the estimated average cost for two" , min_value = 50 , max_value = 99999 , value = 1000 , step = 200)
st.write("Average Cost Input:", averagecost)

# In[26]:


tablebooking = st.selectbox("Restaurant has Table booking ?" , ["Yes" , "No"])
st.write("Table Booking Input:", tablebooking)

# In[27]:


onlinedelivery = st.selectbox("Restaurant has online delivery ?" , ["Yes" , "No"])
st.write("Online Delivery Input:", onlinedelivery)

# In[28]:


pricerange = st.selectbox("What is the price range (1 Cheapest , 4 Most Expensie)" , [1, 2, 3, 4])
st.write("Price Range Input:", pricerange)

# In[29]:


predictbutton = st.button("Predict the Review!")


# In[30]:


st.divider()


# In[31]:


model = joblib.load("mlmodel.pkl")


# In[32]:


bookingstatus = 1 if tablebooking == 'Yes' else 0


# In[33]:


deliverystatus = 1 if onlinedelivery == 'Yes' else 0


# In[34]:


import numpy as np

def flatten_scalar(x):
    return np.ravel(x)  

averagecost = flatten_scalar(averagecost)
bookingstatus = flatten_scalar(bookingstatus)
deliverystatus = flatten_scalar(deliverystatus)
pricerange = flatten_scalar(pricerange)

my_X_values = np.array([[averagecost, bookingstatus, deliverystatus, pricerange]])

print(my_X_values)
print(my_X_values.shape)


# In[35]:


import joblib

scaler = joblib.load("scaler.save")    
my_X_values = np.array(my_X_values).reshape(1, -1) 
X_new = scaler.transform(my_X_values)  


# In[37]:


if predictbutton:
    st.snow()
    prediction = model.predict(X_new)[0]
    st.write("Raw prediction:", prediction) 
    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:













