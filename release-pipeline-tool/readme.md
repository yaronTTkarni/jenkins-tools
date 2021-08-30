#Guideline
Create, archive and delete pipelines.

The pipelines are defined by: config/pipeline_to_generate_config.yaml
the key it's the pipeline name.

# Introduction

Support of:
- Create
- Delete
- Archive

##Create
Create jobs and views for the required %new_release_name%

## Delete
Delete job and view by the required %version_prefix_to_delete%

## Archive
Archive job and view by the required %version_prefix_to_archive%

#Usage Example:


Run:
```
poetry shell

poetry check

poetry update

poetry install

poetry build
```
##Create
```
poetry run python MainEntry.py --jenkins_ip 10.0.0.207 --jenkins_port 8080 --command create --jenkins_user imvision --jenkins_password 1 --git_user yaron --git_password 123456 --new_release_name 9.5.8 --version_major 100 --version_minor 1 --version_patch 0
```

In order to create specific pipelines,
use the specific_pipelines tag name, and the pipeline are separated by |
```
poetry run python MainEntry.py --jenkins_ip 10.0.0.207 --jenkins_port 8080 --command create --jenkins_user imvision --jenkins_password 1 --git_user yaron --git_password 123456 --new_release_name 900.1.1 --version_major 100 --version_minor 1 --version_patch 0 --specific_pipelines "a-ms|b-ms|c-ms"
```

##Delete
```
poetry run python MainEntry.py --jenkins_ip 10.0.0.207 --jenkins_port 8080 --command delete --jenkins_user imvision --jenkins_password 1 --version_prefix_to_delete 9.5.8
```
##Archive
```
poetry run python MainEntry.py --jenkins_ip 10.0.0.207 --jenkins_port 8080 --command archive --jenkins_user imvision --jenkins_password 1 --version_prefix_to_archive 9.5.8
```


#Development notes:
in order to publish the tool to nexus, needs to run:
``` poetry publish -r py_nexus_repo ```
