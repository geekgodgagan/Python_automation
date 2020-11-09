def dockerManagement():
   import os

   while True:
      print("""\n
      Enter 0 to exit
      Enter 1 for system-wide information
      Enter 2 to see the status of Docker services
      Enter 3 to start the Docker services
      Enter 4 to stop the Docker services
      Enter 5 to list all the images that you have
      Enter 6 to list all the Docker containers that you have
      Enter 7 to search the Docker Hub for images
      Enter 8 to install an image from the Docker Hub
      Enter 9 to launch a new container with an interactive terminal
      Enter 10 to launch an existing container with an interactive terminal
      Enter 11 to display the IP address of a container
      Enter 12 to execute only one command in the container and then return to the base OS
      Enter 13 to rename a container
      Enter 14 to stop a container
      Enter 15 to restart a container
      Enter 16 to kill a container
      Enter 17 to start a container
      Enter 18 to copy a file from the local filesystem to a Docker container
      Enter 19 to copy a file from a Docker container to the local filesystem
      Enter 20 to remove a container
      Enter 21 to remove all the stopped containers
      Enter 22 to remove an image
      Enter 23 to fetch logs of a container
      Enter 24 for the resource usage statistics of a container
      """)
      ch = input("Enter your choice : ")
      print(ch)
      if int(ch) == 0:
         exit()
      elif int(ch) == 1:
         os.system("docker system info")
      elif int(ch) == 2:
         os.system("systemctl status docker")
      elif int(ch) == 3:
         os.system("systemctl start docker")
      elif int(ch) == 4:
         os.system("systemctl stop docker")
      elif int(ch) == 5:
         os.system("docker images")
      elif int(ch) == 6:
         os.system("docker ps -a")
      elif int(ch) == 7:
         se = input("Name of the image that you want to search in the Docker Hub : ")
         cmd = "docker search {0}".format(se)
         os.system(cmd)
      elif int(ch) == 8:
         img_name = input("Name of the image : ")
         version = input("Version of the image (Leave blank for the latest version) : ")
         os.system("docker pull {0}:{1}".format(img_name, version))
      elif int(ch) == 9:
         img_name = input("Name / ID of the image : ")
         c_name = input("Name of the container (Leave blank if you want to use the default name) : ")
         if len(c_name) > 0:
              os.system("docker run -it --name {0} {1}".format(c_name ,img_name))
         else:
              os.system("docker run -it {0}".format(img_name))
      elif int(ch) == 10:
         c_name = input("Name / ID of the container : ")
         os.system("docker attach {0}".format(c_name))
      elif int(ch) == 11:
         c_name = input("Name / ID of the container : ")
         os.system('docker inspect {0}'.format(c_name))
      elif int(ch) == 12:
         c_name = input("Name / ID of the container : ")
         cmd = input("Enter the command that you want to execute : ")
         os.system("docker exec {0} {1}".format(c_name, cmd))
      elif int(ch) == 13:
         curr_name = input("Current Name : ")
         new_name = input("New Name : ")
         os.system("docker rename {0} {1}".format(curr_name, new_name))
      elif int(ch) == 14:
         c_name = input("Name / ID of the container : ")
         os.system("docker stop {0}".format(c_name))
      elif int(ch) == 15:
         c_name = input("Name / ID of the container : ")
         os.system("docker restart {0}".format(c_name))
      elif int(ch) == 16:
         c_name = input("Name / ID of the container : ")
         os.system("docker kill {0}".format(c_name))
      elif int(ch) == 17:
         c_name = input("Name / ID of the container : ")
         os.system("docker start {0}".format(c_name))
      elif int(ch) == 18:
         src = input("File path of the source : ")
         c_name = input("Name / ID of the container : ")
         dest = input("File path of the destination : ")
         os.system("docker cp {0} {1}:{2}".format(src, c_name, dest))
      elif int(ch) == 19:
         c_name = input("Name / ID of the container : ")
         src = input("Path of the source : ")
         dest = input("Path of the destination : ")
         os.system("docker cp {0}:{1} {2}".format(c_name, src, dest))
      elif int(ch) == 20:
         c_name = input("Name / ID of the container : ")
         os.system("docker rm {0}".format(c_name))
      elif int(ch) == 21:
         os.system('docker rm `docker ps -a -q`')
      elif int(ch) == 22:
         img_name = input("Name / ID of the image or images seperated by spaces : ")
         os.system("docker rmi {0}".format(img_name))
      elif int(ch) == 23:
         c_name = input("Name / ID of the container : ")
         os.system("docker logs {0}".format(c_name))
      elif int(ch) == 24:
         c_name = input("Name / ID of the container : ")
         os.system("docker stats {0}".format(c_name))
      else:
         print("Operation not supported")
