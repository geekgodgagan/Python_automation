def lvm():
	import os

	def displayDisks():
    		print("fdisk -l")

	os.system("tput setaf 3")
	print("""\t\t\t LVM menu. \n Before starting you need to attach atleast 2 hard disks to your virtual machine.\n
 	Do this by going to setting->storage->add new storage (at the bottom)->hard disk->add or create(virtual hard disk image->dynamic storage->allocate space).\n
 	Do you want to see all the hard disks you have?(y/n)
	""")
	x=input()
	if(x=='y'):
    		displayDisks()
	hd1=input("enter name of harddisk 1 (ex:-sdb)")
	print("{} is hd1".format(hd1))
	hd2=input("enter name of harddisk 2 (ex:-sdc)")
	print("{} is hd1".format(hd1))
	vgname="default"
	lvname="default"
	os.system("tput setaf 7")

	while True:

		print("""
		\n
		Press 1 : Step 1 will compulsory be to convert HardDisk to physical volume
		Press 2 : To display details of physical volume
		Press 3 : To create virtual group
		Press 4 : To create logical volume inside virtual group
		Press 5 : To display details of virtual group
		Press 6 : To display logical volume
		Press 7 : To display specific logical volume
		Press 8 : To increase size of logical volume
		Press 9 : To attach another hard disk to virtual group
        	Press 10 : To display details of hard disks, partition and virtual group (and logical volumes) created
		Press 11 : exit
		""")

		ch = input("Enter ur choice:")

		if int(ch)==1:
			os.system("pvcreate /dev/{}".format(hd1))
			os.system("pvcreate /dev/{}".format(hd2))

		elif int(ch)==2:
			os.system("pvdisplay /dev/{}".format(hd1))
			os.system("pvdisplay /dev/{}".format(hd2))


		elif int(ch)==3:
			vgname=input("Enter the name of you want to give to the virtual group")
			os.system("vgcreate {} /dev/{}   /dev/{}".format(vgname,hd1,hd2))

		elif int(ch)==5:
			os.system("vgdisplay {}".format(vgname))

		elif int(ch)==4:
			lvname=input("Enter the name of you want to give to the logical volume")
			size=input("Enter size/storage capacity you wish to allocate to this volume (ex:-2G)")
			mountdir=input("Enter name of directory to mount. (Will be automatically created")
			print("creating, formatting and mounting partition")
			os.system("lvcreate --size {} --name {}   {}".format(size,lvname,vgname))
			os.system("mkdir /{}".format(mountdir))
			os.system("mkfs.ext4 /dev/{}/{}".format(vgname,lvname))
			os.system("mount /dev/{}/{}  /{}".format(vgname,lvname,mountdir))


		elif int(ch)==6:
			os.system("lvdisplay")

		elif int(ch)==7:
			lvname=input("Enter which logical volume details you want")
			os.system("lvdisplay {}/{}".format(vgname,lvname))

		elif int(ch)==8:
			size=input("Enter extra size you want to extend (ex:-5G)")
			lvname=input("Enter the name of logical volume you want to extend")
			print("Extending storage as well formatting the extended storage")
			os.system("lvextend --size +{}  /dev/{}/{}".format(size,vgname,lvname))
			os.system("resize2fs /dev/{}/{}".format(vgname,lvname))

		elif int(ch)==9:
			print("For this you need to create a different hard disk than {} and {}".format(hd1,hd2))
			print(" Do you want to see all the hard disks you have?(y/n)")
			x=input()
			if(x=='y'):
				displayDisks()
				hd3=input("Enter the name of third hard disk")
				os.system("vgextend {} /dev/{}".format(vgname,hd3))

		elif int(ch)==10:
			displayDisks()

		elif int(ch)==11:
			exit()
		else:
			print("not supported")
