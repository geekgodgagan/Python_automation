import os
def aws():
	while True:
		os.system("clear")
		print("""
		\n
		Press 1 : To Download and Configure AWS CLI
		Press 2 : To use the AWS Services
		Press 3 : To get details of the services
		Press 4 : To EXIT
		""")
		ch1=input("Enter Your Choice :- ")

		if ch1=="1" :
			print("""
          		\n
	         	Press 1  : To download AWS CLI 2
		        Press 2  : To configure AWS CLI
			Press 3  : To Go to Main Menu
			""")
			ch2=input("Enter Your Choice :- ")
			if(ch2=="1"):
				print("AWS CLI IS INSTALLING ON YOUR SYSTEM....")
				os.system("pip3 install awscli &> /dev/null")
				print("AWS IS SUCCESSFULLY INSTALLED")

			elif(ch2=="2"):
				print("Create IAM User and provide AWS Access Key ID , Secret Access Key  and Default Region Name below ")
				os.system("aws configure")
			elif(ch2=="3"):
				continue

		elif ch1=="2":
			print("""
			\n
			Press 1  : To create a Key Pair and Save it
			Press 2  : To create a security group
			Press 3  : To launch EC2 Instance
			Press 4  : To create a EBS Volume
			Press 5  : To attach EBS volume to EC2 Instance
		        Press 6  : To create a Snapshot
			Press 7  : To create S3 Bucket
			Press 8  : To upload files in S3 bucket
			Press 9  : To create CloudFront
			Press 10 : To go to Main Menu
			""")
			ch3=input("Enter your choice:- ")

			if(ch3=="1"):
				key=input("Enter name for your key :- ")
				os.system("aws ec2 create-key-pair --key-name {} > {}.pem".format(key,key))
				print("KEY PAIR SUCCESSFULLY CREATED AND SAVED IN YOUR SYSTEM")


			elif(ch3=="2"):
				group=input("Enter Security Group Name :- ")
				desc=input("Enter Description for your Security Group :- ")
				os.system("aws ec2 create-security-group --group-name {}  --description {} &> /dev/null".format(group,desc))
				print("SECURITY GROUP CREATED SUCCESSFULLY")
				inbound=input("Do you want to give inbound rule set ? Yes/No :- ")
				if inbound=="Yes" or inbound=="Y":
					prot=input("Enter the Protocol Name :- ")
					port=input("Enter the Port Number :- ")
					cidr=input("Enter the CIDR :- ")
					os.system("aws ec2 authorize-security-group-ingress   --group-name {}  --protocol {}  --port {}  --cidr {}".format(group,prot,port,cidr))
					print("INBOUND RULE SET CREATED !!")

			elif(ch3=="3"):
				imgid=input("Enter the IMAGE ID :- ")
				instype=input("Enter the Instance type :- ")
				keyname=input("Enter the Key Name :- ")
				secgrp=input("Enter the Security Group :- ")
				os.system("aws ec2 run-instances  --image-id {}  --instance-type {}      --key-name {}   --security-groups {} &> /dev/null".format(imgid , instype , keyname , secgrp))
				print("EC2 INSTANCE SUCCESSFULLY CREATED!!")


			elif(ch3=="4"):
				size=input("Enter Size of Volume (in Gb) :- ")
				availzone=input("Enter the Availability Zone :- ")
				os.system("aws ec2 create-volume  --size {} --availability-zone {}  &> /dev/null".format(size,availzone))
				print("EBS VOLUME SUCCESSFULLY CREATED !!")


			elif(ch3=="5"):
				iid=input("Enter the Instance ID :- ")
				vid=input("Enter the Volume ID :- ")
				device=input("Enter the Device Name :- ")
				os.system("aws ec2 attach-volume  --volume-id {}   --instance-id  {}  --device {} &> /dev/null".format(iid,vid,device))
				print("EC2 VOLUME SUCCESSFULLY ATTACHED")

			elif(ch3=="6"):
				volumeid=input("Enter the Volume ID :- ")
				snapdesc=input("Enter the Description :- ")
				os.system("aws ec2 create-snapshot --volume-id {} --description {} &> /dev/null".format(volumeid,snapdesc))
				print("SNAPSHOT SUCCESSFULLY CREATED!!")


			elif(ch3=="7"):
				bname=input("Enter a unique Bucket Name :- ")
				region=input("Enter the Region for your Bucket :- ")
				os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bname,region,region))
				print("BUCKET SUCCESSFULLY CREATED!!")


			elif(ch3=="8"):
				imgpath=input("Enter the File Path :- ")
				bucketurl=input("Enter the Bucket URL :- ")
				os.system("aws s3 cp {} {} &> /dev/null".format(imgpath,bucketurl))
				print("FILE UPLOADED !!")

			elif(ch3=="9"):
				domain=print("Enter the Origin Domain Name :- ")
				os.system("aws cloudfront create-distribution --origin-domain-name {} &> /dev/null".format(domain))


			elif(ch3=="10"):
				continue

		elif ch1=="3":
			print("""
			\n
			Press 1 : To get details of the EC2 Instances
			Press 2 : To get details of the EBS volumes
			Press 3 : To get details of Snapshots
			Press 4 : To get details of the S3 Bucket
			Press 5 : To get details of the Cloud Front
			Press 6 : To go back to Main Menu
			""")

			ch3=input("Enter your choice :- ")
			if(ch3=="1"):
				os.system("aws ec2 describe-instances")
			elif(ch3=="2"):
				os.system("aws ec2 describe-volumes")
			elif(ch3=="3"):
				os.system("aws ec2 describe-snapshots")

			elif(ch3=="4"):
				os.system("aws s3api list-buckets")

			elif(ch3=="5"):
				os.system("aws cloudfront list-distributions")

			elif(ch3=="6"):
				continue

		elif ch1=="4":
			exit()

		input(" Press Enter to continue .....")
