# COE379L_Project03_Osvaldo_Serena
Project Description: You are given a dataset which contains satellite images from Texas after Hurricane Harvey. There are damaged and non-damaged building images organized into respective folders. You can find the project 3 dataset on the course GitHub repository here.

## Using the container
__To run the inference server, pull and run the Docker image with the Alt Lenet model:__  
```
docker pull serenashah/ml-proj03-api
docker run -it --rm -p 5000:5000 serenashah/ml-proj03-api
```

## HTTP requests
__To get information about the model:__ 
```
curl localhost:5000/models
```

This would be the expected output:
```
Content           : {
                      "description": "Classify images containing damaged/undamaged buildings",
                      "name": "models",
                      "number_of_parameters": 133280,
                      "version": "v1"
                    }
```

You may also attempt this commands if the previous one does not work:
```
curl http://localhost:5000/models
```

__To get a prediction for damaged or not on an input picture, run this in a Python script/Jupyter Notebook:__ 
```
rsp = requests.post("http://172.17.0.1:5000/models", json={"image": input_image})
rsp.json()
```
where `input_image` is a serialized image. Note that `Flask` is a required module.  
__The expected output for this is a prediction array that corresponds to an array with labels `[damage, no_damage]` that should look as follows:__   
`[1.0, 0.0]`  
This array response would be interpreted as predicting damage in the input image using the Alt Lenet model.
