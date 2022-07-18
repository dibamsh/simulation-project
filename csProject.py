#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[2]:


pip install simpy


# In[7]:


import simpy
import statistics
import random


# | System                     | Agent       | process
# | -----------                | ----------- | -----------
# | resturants' modirator      | API,Web     | modirate
# | Customer manager           | API         | modirate
# | Order manager              | API,Web     | modirate
# | delivery                   | res & Cust  | delivery
# | payment                    | Order'M     | payment
# | API                        | User        | API
# | Web                        | User        | Web

# ## get inputs

# In[1]:


N_resMod = 1
N_cusMod = 1
N_ordMod = 1
N_delivery = 2
N_payment = 5
N_API = 3
N_web = 2


# ## Goal
# 
# #### 1. Average queue's len
# #### 2. Average queue's time
# #### 3. Utilization
# #### 4. Effect on the numberof sampls
# #### 5. Suggestion for improvement
# 

# In[9]:


waite_times = []

class FoodOnline(object):
    def __init__(self,env,number_of_APIs,number_of_WEBs,number_of_customer_modirators,number_of_order_modirators, number_of_resturant_modirators,number_of_deliverys,number_of_payments ):
        self.env = env
        self.number_of_APIs = simpy.Resource(env, number_of_APIs)
        self.number_of_WEBs = simpy.Resource(env, number_of_WEBs)
        self.number_of_customer_modirators = simpy.Resource(env, number_of_customer_modirators)
        self.number_of_order_modirators = simpy.Resource(env, number_of_order_modirators)
        self.number_of_resturant_modirators = simpy.Resource(env, number_of_resturant_modirators)
        self.number_of_deliverys = simpy.Resource(env, number_of_deliverys)
        self.number_of_payments = simpy.Resource(env, number_of_payments)
        
        
    def __order_using_API(self):
        yield self.env.timeout()
    def __order_using_WEB(self):
        yield self.env.timeout()
        
    def send_msg(self):
        pass
        
    def __view_info_MOBILE(self):
        pass
        
    def __view_info_WEB(self):
        pass
        
    def __order_delivery(self):
        pass
        
    def __order_tracking(self):
        pass
    


# ## Communication with the system through API & Web
# 

# In[ ]:





# ## Get in line to Order using API or Web

# In[ ]:




