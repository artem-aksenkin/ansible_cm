#!/bin/bash

# curl --silent -T $war -u $username:$password $url

curl --silent -T "/home/student/cm/ansible/day-4/hello-war/target/mnt-lab.war" -u deploy:123 "127.0.0.1:8080/manager/text/deploy?path=/mnt-lab&update=true"

#deploy: url=... war=… username=… password=…

exit 0