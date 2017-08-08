import yaml

from jen2jen import JenkinsExtractor
from helper.tiny import Tiny as _h

config = yaml.load(open('config.yaml'))

jenkins = JenkinsExtractor(
    config['jenkins_from']['url'],
    config['jenkins_from']['login'],
    config['jenkins_from']['password']
)
_h.backup()
jenkins.extract_jobs()