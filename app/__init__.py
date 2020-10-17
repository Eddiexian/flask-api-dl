# -*- coding: UTF-8 -*-


from flask import Flask, request, jsonify
from flask_cors import CORS
import app.model as model
import numpy as np



app = Flask(__name__)
CORS(app)


# In[6]:


@app.route('/test')
def fortest():
    return 'hello test'
@app.route('/predict', methods=['POST'])
def postInput():
    insertValues = request.get_json()
    x1 = insertValues['picture']
    input = np.array(x1)
    result = model.predict(input)
    
    return jsonify({'return': str(result)})

@app.route('/posttest',methods=['POST'])
def posttest():
    insertValues = request.get_json()
    x1 = insertValues['picture']
    input = np.array(x1)
    return jsonify({'return': str(input)})






