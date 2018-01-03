# repo-management.py
#
# simple centralized repository management for yum
# 
# author: Simon Lauger <simon@lauger.de>
# 
# to install, copy this file to /usr/lib/yum-plugins/repo-management.py
# and then create /etc/yum/pluginconf.d/repo-management.conf
# below.
# 
#  /etc/yum/pluginconf.d/repo-management.conf:
#
#   [main]
#   enabled = 1
#   url = https://api.example.com/repos

import requests

import os
from glob import fnmatch

import yum
from yum.plugins import PluginYumExit, TYPE_CORE

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

def prereposetup_hook(conduit):
  url = conduit.confString('main', 'url', '')
  if url == "":
      conduit.info(2, 'repo-management: url to managed repos not set')
      return False

  conduit.info(2, 'repo-management: managed repos enabled')

  # try to request json file
  try:
    response = requests.get(url)
  except:
    conduit.info(2, 'repo-management: error connecting to remote url')
    return False

  # try to parse json response
  try:
    repos        = response.json()
  except:
    conduit.info(2, 'repo-management: got invalid json response from remote url')
    return False

  # prepare string
  repos_string = ""
  
  # loop over json response and create the managed.repo file
  for repo_id, repo_params in repos.iteritems():
    repos_string += "[" + repo_id + "]\n"
    for key, value in repo_params.iteritems():
      repos_string += key + " = " + value + "\n"

  with open(conduit.confString('main', 'repos_file', '/etc/yum.repos.d/managed.repo'), "w") as file:
    file.write(repos_string)

  return True
