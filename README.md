# Monkey Classification


## Overview
This is a Flask web app which predicts the monkey species. The model is trained to identify 10 species of monkey.

Here I have used transfer learning technique using bit/m-r50x1 which is similar to ResNet50-v2. The model was able to acheive 96% accuracy in training.


## Installation

The Code is written in Python 3.9.13. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

```bash
  pip install -r requirements.txt
```


## Dictionary Tree
```
├── static 
│   ├── css
        ├── main.css
    ├── js
        ├── main.js
├── template
    ├── base.html
    ├── index.html
├── Uploads
├── .gitattributes
├── .gitignore
├── Procfile
├── README.md
├── Monkeyapp.py
├── MonkeyClassification.h5
├── MonkeyClassification.ipynb
├── build.sh
├── requirements.txt
```


## Tehnologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)
![](https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png)
![](https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg)


## Troubleshooting
1. Got Server refresh error when tried to perform predict operation in UI. 
2. Created a virtual environment and activated 'activate' file in New_Env/Script.
   Refer [this](https://medium.com/@sawlemon/creating-a-python-virtual-environment-in-windows-4c95bd2e7c56) link to create a virtual enviroment.
3. Use pip install within the virtual environment for 'No module found' errors.


## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/monishbkalmady/Monkey-Classification/issues) here by including your search query and the expected result.


## Future Scope
* Use different transfer learning algorithms
* Memory optimization of Flask app.py for deployment in web servers
* Front-End 
