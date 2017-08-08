import os
import time
from lxml import etree


class Tiny:

    @staticmethod
    def xml2list(xml_string):
        """
        Converts Jenkins projects api/xml description into the list of job elements
        :param xml_string: api/xml description as a string
        :return: list of elements
        """
        return etree.fromstring(xml_string).xpath('//job')

    @staticmethod
    def get_name(job_element):
        return job_element.getchildren()[0].text

    @staticmethod
    def get_class(job_element):
        return job_element.attrib['_class']


    @staticmethod
    def get_url(job_element):
        return job_element.getchildren()[1].text

    @staticmethod
    def backup():
        folder = 'jobs%s' % time.strftime("%m-%d-%H-%M")
        print('Yours jobs are going to be stored in: ', os.getcwd())
        os.mkdir(folder)
        os.chdir(folder)


class JenkinsClass:

    FOLDER = 'com.cloudbees.hudson.plugins.folder.Folder'
