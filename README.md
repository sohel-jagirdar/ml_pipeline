

The data contains information from the California census. So although it may help you with predicting current housing prices.

**Content:**
The data pertains to the houses found in a given California district and some summary stats about them based on the census data. The data was not cleaned so there are some pre-processing steps performed using MLOPS.  We have used automation of pipeline where one run required to perform all the steps as mentioned Below. 

**ML Life cycle Operations as per requirement :**

-  Data Ingestion
- Data Validation 
- Data Transformation 
- Model training
- Model Evaluation
- Model Pusher

**MLOPS** Operations are performed during **Phase 1** : 

- [ ]  **CI** : Continues Integration
- [ ] **CD** : Continues Deployment 
- [ ]  **CT** : Continues Training
- [ ] **DVC** : Data Versioning maintaining
- [ ] **Model Versioning** 

**Using Github, Github Action and Cloud platfrom Like Heroku to Provide an API to Client **



## Application URL ( STATUS : TURNED OFF )

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = sohel.jagirdar@outlook.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-housing-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```

Install Evidently to find Data Drift :

Note: Data Drift is When your dataset stats gets change we call it as data drift

```
pip install Evidently
```


Install Matplotlib

```
pip install Matplotlib
```

**Project Architecture :**

![project arch](https://github.com/sohel-jagirdar/ml_pipeline/assets/52422511/8228dfa2-97c1-4426-ad6f-a8938538705b)

**Data Collection :**

![data collection](https://github.com/sohel-jagirdar/ml_pipeline/assets/52422511/e15ea54b-e263-4fe6-ab01-396ca3fffa1c)

**Deployment :**

![deplyement arch](https://github.com/sohel-jagirdar/ml_pipeline/assets/52422511/92e1ea0a-345e-4df8-87f1-ca5019a4985f)




