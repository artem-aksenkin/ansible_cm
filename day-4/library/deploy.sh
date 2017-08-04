#!/bin/bash

# curl --silent -T $war -u $username:$password $url

curl --silent -T "/home/student/cm/ansible/day-4/hello-war/target/mnt-lab.war" -u deploy:123 "192.168.56.13/manager/text/deploy?path=/mnt-lab&update=true"

#deploy: url=... war=… username=… password=…

