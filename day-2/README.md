# Artsiom Aksionkin
Lab Work 
# Task. Web Server Provisioning
Review
Using Ansible v2.3.1 for provisioning nginx + tomcat application stack. 
Learning by doing.
Task
On Host Node (Control Machine):
1. Create folder ~/cm/ansible/day-2. All working files are supposed to be placed right there.
2. Spin up clear CentOS6 VM using vagrant (repo with vagrantfile). Verify connectivity to the host using ssh keys (user: vagrant)
3. Create ansible inventory file (name: inventory) with remote host connection details:
Remote VM hostname/ip/port
Remote ssh log in username
Connection type
4. Develop a playbook (name: site.yml) which is supposed to run against any host (specified in inventory)
4.1 Develop roles:
java (installs java)
java_test (does only checks that java installed and running properly)
tomcat (installs tomcat)
tomcat_test (does only checks that tomcat installed and running properly)
nginx (installs nginx)
nginx_test (does only checks that nginx installed and running properly)
4.2 Playbook should consist of 2 Plays:
Installation
Verification
4.3 Use handlers to manage tomcat/nginx configuration changes
4.4 Use module debug to check configuration during the installation 
4.5 Define play/roles variables (at least):
tomcat_version
tomcat_home
tomcat_user
tomcat_group
java_version
4.6 Every task/handler should have a name section with details of task purpose.
5. Software installation requirements:
Tomcat AS should be installed from sources (tar.gz) – download from the official site (http://archive.apache.org/dist/tomcat/).
Tomcat AS should be owned (and run) by user specified in variable (default: tomcat_as:tomcat_as_group).
Tomcat AS version should be 7.x, 8.x (at least 5 versions), exact version to be installed is taken from appropriate variable.
Tomcat installation folder (CATALINA_HOME) is /opt/tomcat/$version, where $version is the version of tomcat defined in playbook.
Java can be installed from CentOS Repositories
Use module yum to install Nginx
Use module template for management of nginx cofigs
Tomcat home page should be available on port 80 (accessible from Control Machile) via nginx.
6. Verification Procedure: playbook will be checked by instructor’s CI system as follows:
6.1 Connect to student’s host by ssh (username “student”) with own ssh key.
6.2 Go into the folder mentioned in point 1
6.3 Destroy/Launch VM: vagrant destroy && vagrant up
6.4 Execute VM provisioning: ansible-playbook site.yml -i inventory -vv 
6.5 If previous steps are done successfully, instructor will check report (pdf-file)
7. Feedback: report issues/problems you had during the development of playbook and time spent for development.