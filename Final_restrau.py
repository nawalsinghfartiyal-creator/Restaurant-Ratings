#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np


# In[2]:


st.set_page_config(layout="wide")


# In[3]:


model = joblib.load("mlmodel.pkl")
scaler = joblib.load("scaler.save")


# In[4]:


st.title("Restaurant Ratings Predictor")


# In[5]:


averagecost = st.number_input("Estimated average cost for two", min_value=50, max_value=99999, value=1000)
tablebooking = st.selectbox("Restaurant has Table booking?", ["Yes", "No"])
onlinedelivery = st.selectbox("Restaurant has online delivery?", ["Yes", "No"])
pricerange = st.selectbox("What is the price range (1 Cheapest, 4 Most Expensive)", [1, 2, 3, 4], index=3)


# In[6]:


bookstatus = 1 if tablebooking == "Yes" else 0
deliverystatus = 1 if onlinedelivery == "Yes" else 0


# In[7]:


my_X_values = np.array([averagecost, bookstatus, deliverystatus, pricerange])
my_X_values = my_X_values.reshape(1, -1)


# In[8]:


if st.button("Predict the Review!"):
    # Scale the user input
    X_new = scaler.transform(my_X_values)


# In[11]:


X_new = scaler.transform(my_X_values)


# In[12]:


prediction = model.predict(X_new)[0]
st.write("Raw model prediction:", prediction)


# In[15]:


if prediction < 2.5:
    st.snow()
    st.write("Poor")
elif prediction < 3.5:
    st.snow()
    st.write("Average")
elif prediction < 4.0:
    st.snow()
    st.write("Good")
elif prediction < 4.5:
    st.snow()
    st.write("Very Good")
else:
    st.snow()
    st.write("Excellent")


# In[ ]:





# In[ ]:





# In[ ]:





