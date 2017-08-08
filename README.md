_**jen2jen**_

This repo contains some code which allows to fetch jobs from some Jenkins instance and store them in the same way the are usually stored in _/var/lib/jenkins/jobs/_ directory. This means one can easily make a backup of current Jenkins jobs setup. To plant jobs on a new Jenkins instance the folder should be either placed to _/var/lib/jenkins/jobs/_ manually or with Jenkins REST API. 

The code is written in Python 3 and is based on Jenkins REST API funcionality with the [requests](http://docs.python-requests.org/en/master/) library. 

To run the code please fetch the repo locally and create a virtualenvironment
```
virtualenv -p python3.5 venv
```
install the requirements
```
pip install -r requirements.txt
```
and update the credentials in the _config.yaml_ file
```python
crumb-issuer: '/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,%22:%22,//crumb)'
api-link: api/xml

jenkins_from:
  url: http://xxx.xx.xx.xx:8080/
  login: yourlogin
  password: yourpassword
```
and then just run the _main.py_
```
python main.py
```
The jobs are going to be stored somewhere inside the repo folder. 
