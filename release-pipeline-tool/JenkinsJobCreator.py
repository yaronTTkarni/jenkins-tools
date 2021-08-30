import jenkins
import YamlObject

from consts import HTTP_S_S

LIB = "lib"

MS = "ms"

LIBRARIES = " Libraries"


class JenkinsJobCreator:
    ms_configs = {"java": "config/templates/jenkins_pipeline_ms_java.xml",
                  "python": "config/templates/jenkins_pipeline_ms_python.xml",
                  "angular": "config/templates/jenkins_pipeline_ms_angular.xml" }

    lib_config = {"java": "config/templates/jenkins_pipeline_lib_java.xml"}

    def __init__(self, data_arg_config):
        self.__data_arg_config = data_arg_config

    def get_data_cmd_config(self):
        return self.__data_arg_config

    def create_config_from_template(self, pipeline_cfg):

        config_file_name = None
        if pipeline_cfg.type == MS:
            config_file_name = self.ms_configs[pipeline_cfg.lang]
        elif pipeline_cfg.type == LIB:
            config_file_name = self.lib_config[pipeline_cfg.lang]

        with open(config_file_name, 'r') as file:
            data = file.read()

            data = data.replace('%git_repo_name%', pipeline_cfg.name) \
                .replace('%git_user%', self.get_data_cmd_config().get_git_user()) \
                .replace('%git_password%', self.get_data_cmd_config().get_git_password()) \
                .replace('%release_name%', self.get_data_cmd_config().get_new_release_name()) \
                .replace('%parent_branch_name%', self.get_data_cmd_config().get_parent_branch()) \
                .replace('%version_major%', self.get_data_cmd_config().get_version_major()) \
                .replace('%version_minor%', self.get_data_cmd_config().get_version_minor()) \
                .replace('%version_patch%', self.get_data_cmd_config().get_version_patch()) \
                .replace('%project_name%', pipeline_cfg.project_name)

            if pipeline_cfg.is_helm_config_enable:
                data = data.replace('%HELM_CLONE_CONFIG_FOLDER_LIST%',"\n\t\tHELM_CLONE_CONFIG_FOLDER_LIST = \'config-prod,config-qa,opt\'")
            else:
                data = data.replace('%HELM_CLONE_CONFIG_FOLDER_LIST%','')

            return data

    @staticmethod
    def create_view(jobs_in_view, view_name, server):

        jobs_string = ''
        for job_name in jobs_in_view:
            jobs_string += '<string>' + job_name + '</string>'

        with open("config/templates/jenkins_pipeline_view.xml", 'r') as file:
            config_data = file.read()

            config_data = config_data.replace('%view_name%', view_name) \
                .replace('%view_projects%', jobs_string)

        print("Create view named: %s with config of [%s]" % (view_name, config_data))
        server.create_view(view_name, config_data)

    def create(self):
        server = jenkins.Jenkins(HTTP_S_S % (self.__data_arg_config.get_jenkins_ip(),
                                      self.__data_arg_config.get_jenkins_port()),
                                 self.__data_arg_config.get_jenkins_user(),
                                 self.__data_arg_config.get_jenkins_password())

        user = server.get_whoami()

        print('You -%- are now connected to Jenkins %s' % (user['fullName'], user['absoluteUrl']))

        doc_pipelines_config = YamlObject.YamlObject.load("config/pipeline_to_generate_config.yaml")

        jobs_in_view_ms = []
        jobs_in_view_lib = []
        for pipeline_cfg in doc_pipelines_config.pipelines:
            config = None

            is_get_config = "false"
            if self.__data_arg_config.get_specific_pipelines_set() is not None:
                if pipeline_cfg.name in self.__data_arg_config.get_specific_pipelines_set():
                    is_get_config = "true"
            else:
               is_get_config = "true"

            if is_get_config == "true":
                config = self.create_config_from_template(pipeline_cfg)
            else:
                continue

            print("create config in jenkins for %s, config is: %s" % (pipeline_cfg.name, config))

            job_name = self.get_data_cmd_config().get_new_release_name() + "-" + pipeline_cfg.name
            server.create_job(job_name, config)

            if pipeline_cfg.type == 'ms':
                jobs_in_view_ms.append(job_name)
            else:
                jobs_in_view_lib.append(job_name)

        if len(jobs_in_view_ms):
            self.create_view( jobs_in_view_ms, self.get_data_cmd_config().get_new_release_name(), server)
            print("All jobs been created, Enjoy.")

        if len(jobs_in_view_lib):
            self.create_view(jobs_in_view_lib, self.get_data_cmd_config().get_new_release_name() + LIBRARIES,
                         server)
            print("All views been created, Enjoy.")