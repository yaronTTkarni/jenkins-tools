# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import getopt
import sys

# read & validate arguments
from DataCmdConfig import DataCmdConfig
from JenkinsJobCreator import JenkinsJobCreator
from consts import optional_arguments_name

input_parameters = "s:p:u:q:o" \
                   "x:r:" \
                   "m:a:t:z:"


class CreateMain:

    @staticmethod
    def handle(argv):
        try:
            opts, args = getopt.getopt(argv, input_parameters, optional_arguments_name)
        except getopt.GetoptError:
            print
            input_parameters
            sys.exit(2)

        data_config = DataCmdConfig()

        for opt, arg in opts:
            print('opt: %s, arg: %s' % (opt, arg))
            if opt == '--parent_branch':
                data_config.set_parent_branch(arg)
            if opt == '--jenkins_ip':
                data_config.set_jenkins_ip(arg)
                if not arg:
                    print
                    'jenkins_ip must be set.'
                    sys.exit()
            if opt == '--jenkins_port':
                data_config.set_jenkins_port(arg)
                if not arg:
                    print('jenkins_port must be set.')
                    sys.exit()
            if opt == '--jenkins_user':
                data_config.set_jenkins_user(arg)
                if not arg:
                    print('jenkins_user must be set.')
                    sys.exit()
            if opt == '--jenkins_password':
                data_config.set_jenkins_password(arg)
                if not arg:
                    print('jenkins_password must be set.')
                    sys.exit()
            if opt == '--git_user':
                data_config.set_git_user(arg)
                if not arg:
                    print('git_user must be set.')
                    sys.exit()
            if opt == '--git_password':
                data_config.set_git_password(arg)
                if not arg:
                    print
                    'git_password must be set.'
                    sys.exit()
            if opt == '--new_release_name':
                data_config.set_new_release_name(arg)
                if not arg:
                    print
                    'new_release_name must be set.'
                    sys.exit()
            if opt == '--version_major':
                data_config.set_version_major(arg)
                if not arg:
                    print
                    'version_major must be set.'
                    sys.exit()
            if opt == '--version_minor':
                data_config.set_version_minor(arg)
                if not arg:
                    print
                    'version_minor must be set.'
                    sys.exit()
            if opt == '--version_patch':
                data_config.set_version_patch(arg)
                if not arg:
                    print
                    'version_patch must be set.'
                    sys.exit()

            if opt == '--specific_pipelines':
                data_config.set_specific_pipelines(arg)
                if not arg:
                    print
                    'pipelines to be set explicitly must be set, otherwise, use the default config (required no args and use the entire config), and do not set this ''--specific_pipelines'' argument.'
                    sys.exit()

        jenkinsjobcre = JenkinsJobCreator(data_config)
        jenkinsjobcre.create()
        # for each
