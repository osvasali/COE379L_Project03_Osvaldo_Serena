from flask import Flask, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model_altlenet = tf.keras.models.load_model('models/altlenet.keras')


@app.route('/models', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "models",
      "description": "Classify images containing damaged/undamaged buildings",
      "number_of_parameters": 133280
   }

def preprocess_input(im):
   """
   Converts user-provided input into an array that can be used with the model.
   This function could raise an exception.
   """
   # convert to a numpy array
   d = np.array(im)
   # then add an extra dimension
   return d.reshape(1, 28, 28)

@app.route('/models', methods=['POST'])
def classify_clothes_image():
   im = request.json.get('image')
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "result": model_altlenet.predict(data).tolist()}


# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')