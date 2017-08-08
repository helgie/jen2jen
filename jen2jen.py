import os
import requests
import yaml

from helper.tiny import Tiny as _h
from helper.tiny import JenkinsClass

config = yaml.load(open('config.yaml'))


def request(func):
    def wrapper(self, param=''):
        response = func(self, param)
        if response.ok:
            return response.text
        else:
            raise Exception(response.status_code, response.reason)
    return wrapper


class JenkinsExtractor:

    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        response = requests.get(self.url + config['crumb-issuer'], auth=(self.login, self.password))
        if response.ok:
            self.crumb = dict([response.text.split(':')])
            print(self.crumb)
        else:
            raise Exception(response.status_code, response.reason)

    @request
    def xml(self, folder=''):
        if folder:
            url = self.url + folder + config['api-link']
        else:
            url = self.url + config['api-link']
        print('xml', url)
        return requests.get(url, auth=(self.login, self.password))

    @request
    def fetch_job(self, project):
        return requests.get(_h.get_url(project) + '/config.xml', auth=(self.login, self.password))

    @staticmethod
    def store_job(project_name, string):
        with open(project_name + 'config.xml', "w") as job_xml:
            job_xml.write(string)

    def extract_jobs(self, folder=''):
        print(folder)
        jobs_api_xml = self.xml(folder)
        list_jobs_elems = _h.xml2list(jobs_api_xml)
        for project in list_jobs_elems:
            project_name = _h.get_name(project) + '/'
            if folder:
                project_name = folder + 'job/' + project_name
            else:
                project_name = 'job/' + project_name
            local_folder = project_name.replace('job/', '')
            os.mkdir(local_folder)
            self.store_job(
                local_folder,
                self.fetch_job(project)
            )
            if _h.get_class(project) == JenkinsClass.FOLDER:
                self.extract_jobs(project_name)
