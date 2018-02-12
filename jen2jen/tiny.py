import os
import logging
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

    # @staticmethod
    # def plugins2xml(list):
    #     for plugin in list:
    #


    @staticmethod
    def get_url(job_element):
        return job_element.getchildren()[1].text

    @staticmethod
    def get_to_folder(path=''):
        """
        Create local jenkins data
        :return:
        """
        if not path:
            path = os.getcwd() + '/jen2jen_%s' % time.strftime("%d.%m_%H:%M:%S")
            os.mkdir(path)
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)
        print('Jenkins jobs are being stored in your %s local directory' % path)

    @staticmethod
    def file2xml(file_path):
        """
        Get xml payload from a local file
        :param file_path:
        :return:
        """
        return open(file_path).read()


class JenkinsClass:

    FOLDER = 'com.cloudbees.hudson.plugins.folder.Folder'
