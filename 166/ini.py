import configparser
import re


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.config = config

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envs = re.split("[,\n]", self.config["tox"]["envlist"])
        return [env.strip() for env in envs if env != ""]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_python = set()

        sections = self.config.sections()
        for section in sections:
            has_basepython = self.config[section].get("basepython")
            if has_basepython:
                base_python.add(has_basepython)

        if base_python:
            return list(base_python)
        return []