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


class DeleteHandler:

    @staticmethod
    def handle(argv):
        try:
            opts, args = getopt.getopt(argv, input_parameters, optional_arguments_name)
        except getopt.GetoptError:
            print
            input_parameters
            sys.exit(2)

        version_prefix_to_delete = None

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
            if opt == '--version_prefix_to_delete':
                version_prefix_to_delete = arg
                if not arg:
                    print
                    'version_prefix_to_delete must be set'
                    sys.exit()

        server = jenkins.Jenkins(HTTP_S_S % (data_config.get_jenkins_ip(),
                                             data_config.get_jenkins_port()),
                                 data_config.get_jenkins_user(),
                                 data_config.get_jenkins_password())

        jobs = server.get_jobs()

        jobs_to_delete = []
        for job in jobs:
            name_ = str(job['name'])
            if name_.startswith(version_prefix_to_delete):
                jobs_to_delete.append(name_)

        if len(jobs_to_delete) > 0:
            for job_to_delete in jobs_to_delete:
                print("Delete job: [%s] from jenkins" % job_to_delete)
                server.delete_job(job_to_delete)
            print("Delete jobs done.")
        else:
            print("no job to delete")

        views = server.get_views()

        views_to_del = []
        for view in views:
            name_ = str(view['name'])
            if name_.startswith(version_prefix_to_delete):
                views_to_del.append(name_)

        if len(views_to_del) > 0:
            for views_to_del in views_to_del:
                print("delete view %s from jenkins" % views_to_del)
                server.delete_view(views_to_del)
        else:
            print("no view to delete")
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
