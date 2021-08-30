# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import getopt
import sys

# read & validate arguments
import jenkins

from DataCmdConfig import DataCmdConfig
from JenkinsJobCreator import JenkinsJobCreator
from consts import optional_arguments_name, HTTP_S_S

input_parameters = "s:p:u:q:o" \
                   "x:r:" \
                   "m:a:t:"


class ArchiveHandler:

    @staticmethod
    def handle(argv):
        try:
            opts, args = getopt.getopt(argv, input_parameters, optional_arguments_name)
        except getopt.GetoptError:
            print
            input_parameters
            sys.exit(2)

        version_prefix_to_archive = None

        data_config = DataCmdConfig()

        for opt, arg in opts:
            print('opt: %s, arg: %s' % (opt, arg))
            if opt == '--jenkins_ip':
                data_config.set_jenkins_ip(arg)
                if not arg:
                    print
                    'jenkins_ip must be set'
                    sys.exit()
            if opt == '--jenkins_port':
                data_config.set_jenkins_port(arg)
                if not arg:
                    print('jenkins_port must be set')
                    sys.exit()
            if opt == '--jenkins_user':
                data_config.set_jenkins_user(arg)
                if not arg:
                    print('jenkins_user must be set')
                    sys.exit()
            if opt == '--jenkins_password':
                data_config.set_jenkins_password(arg)
                if not arg:
                    print('jenkins_password must be set')
                    sys.exit()
            if opt == '--version_prefix_to_archive':
                version_prefix_to_archive = arg
                if not arg:
                    print
                    'version_prefix_to_archive must be set'
                    sys.exit()

        server = jenkins.Jenkins(HTTP_S_S % (data_config.get_jenkins_ip(),
                                             data_config.get_jenkins_port()),
                                 data_config.get_jenkins_user(),
                                 data_config.get_jenkins_password())

        jobs = server.get_jobs()

        jobs_to_delete = []
        for job in jobs:
            name_ = str(job['name'])
            if name_.startswith(version_prefix_to_archive):
                jobs_to_delete.append(name_)

        for job_to_delete in jobs_to_delete:
            print("Disable job: [%s] from jenkins" % job_to_delete)
            server.disable_job(job_to_delete)

        print("Disable done.")
        # for each

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print
#     sys.argv
#     if sys.argv.__len__() == 1:
#         print("arguments must be set [ %s ] " % input_parameters)
#         sys.exit(2)
#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
