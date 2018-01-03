# Repository management plugin

This is a YUM plugin which allows you to store your YUM repository configuration for your 
system on a central webserver.

Managing your repos with the configuration management of your choice (e.g. ansible, puppet) is
pretty unflexible sometimes. This plugin may help you. It is a smart and pretty basic alternative
to Satellite/Katello and the RHSM (subscription-manager).

## Configuration

Copy the repo-management.conf to /etc/yum/pluginconf.d/repo-management.conf and set the parameter
url to your webserver, providing the REST API.

```
[main]
enabled = 1
url = https://api.example.com/repos
```

## Example JSON response

```
{
  "repo1": {
    "name": "repo1",
    "baseurl": "http://repos.example.com/repo1/$basearch",
    "enabled": "1",
    "gpgcheck": "1",
    "gpgkey": "http://repos.example.com/gpg.key"
  },
  "repo2": {
    "name": "repo2",
    "baseurl": "http://repos.example.com/repo2/$basearch",
    "enabled": "1",
    "gpgcheck": "1",
    "gpgkey": "http://repos.example.com/gpg.key"
  },
  "repo3": {
    "name": "repo3",
    "baseurl": "http://repos.example.com/repo3/$basearch",
    "enabled": "1",
    "gpgcheck": "1",
    "gpgkey": "http://repos.example.com/gpg.key"
  }
}
```

## TODOs

- Create a RPM package for this plugin
- Integrate with `facter` and send system information to the server
- Authentication (SSL, Basic, ...)
