class DataCmdConfig:
    __jenkins_ip = None
    __jenkins_port = None
    __jenkins_user = None
    __jenkins_password = None
    __git_user = None
    __git_password = None
    __new_release_name = None
    __parent_branch = None
    __version_major = None
    __version_minor = None
    __version_patch = None

    __specific_pipelines = None
    __specific_pipelines_set = None

    def get_specific_pipelines(self):
        return self.__specific_pipelines

    def get_specific_pipelines_set(self):
        return self.__specific_pipelines_set

    def set_specific_pipelines(self,specific_pipelines):
        self.__specific_pipelines = specific_pipelines

        if specific_pipelines is not None:
            elems = str(specific_pipelines).split("|")
            self.__specific_pipelines_set = set()
            for elem in elems:
                self.__specific_pipelines_set.add(str(elem).strip())

    def get_parent_branch(self):
        if self.__parent_branch is None:
            return "master"
        return self.__parent_branch

    def get_jenkins_ip(self):
        return self.__jenkins_ip

    def get_jenkins_user(self):
        return self.__jenkins_user

    def get_jenkins_port(self):
        return self.__jenkins_port

    def get_jenkins_password(self):
        return self.__jenkins_password

    def get_git_user(self):
        return self.__git_user

    def get_git_password(self):
        return self.__git_password

    def get_new_release_name(self):
        return self.__new_release_name

    def get_version_major(self):
        return self.__version_major

    def get_version_minor(self):
        return self.__version_minor

    def get_version_patch(self):
        return self.__version_patch

    def set_jenkins_ip(self, jenkins_ip):
        self.__jenkins_ip = jenkins_ip

    def set_jenkins_user(self, jenkins_user):
        self.__jenkins_user = jenkins_user

    def set_jenkins_port(self, jenkins_port):
        self.__jenkins_port = jenkins_port

    def set_jenkins_password(self, jenkins_password):
        self.__jenkins_password = jenkins_password

    def set_git_user(self, git_user):
        self.__git_user = git_user

    def set_git_password(self, git_password):
        self.__git_password = git_password

    def set_new_release_name(self, new_release_name):
        self.__new_release_name = new_release_name

    def set_version_major(self, version_major):
        self.__version_major = version_major

    def set_version_minor(self, version_minor):
        self.__version_minor = version_minor

    def set_version_patch(self, version_patch):
        self.__version_patch = version_patch

    def set_parent_branch(self, parent_branch):
        self.__parent_branch = parent_branch
