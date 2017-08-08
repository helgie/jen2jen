_jen2jen_

This repo contains some code which allows to fetch jobs from some Jenkins instance and store them in the same way the are usually stored in _/var/lib/jenkins/jobs/_ directory. This means one can easily make a backup of current Jenkins jobs setup. To plant jobs on a new Jenkins instance the folder should be either placed to _/var/lib/jenkins/jobs/_ manually or with Jenkins REST API. 

The code is written in Python 3 and is based on Jenkins REST API funcionality with the [requests](http://docs.python-requests.org/en/master/) library. 
