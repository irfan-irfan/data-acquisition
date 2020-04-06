# Python based data acquisition program for investigation based on digital forensic procedures (for Linux)

import hashlib
import os
import time

# Prerequisites

# Mount USB :
# - sudo umount /dev/sdb1
# Make the USB in NTFS format :
# - sudo mkfs.ntfs /dev/sdb1
# Make the USB in FAT32 format :
# - sudo mkfs.vfat /dev/sdb1
# Second, install SleuthKit to enable using fls utility :
# - sudo apt install sleuthkit 
# CAUTION : ONLY WORKS ON UBUNTU LINUX (DEBIAN)

# 1. Collection

print("")
print("1. DATA COLLECTION")
print("")

usbpath = input("USB path = ")
diskimagename = input("Disk image name = ")
print("")

start_time = time.time()

os.system("sudo dd if=%s of=/home/asus/Documents/%s" % (usbpath, diskimagename))

# 2. Examination (using MD5 to check integrity)

print("")
print("2. MD5 HASH INTEGRITY CHECK")
print("")

md5_a = os.system("sudo md5sum %s" % (usbpath))

hasher2 = hashlib.md5()
afile2 = open((diskimagename), 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b=(str(hasher2.hexdigest()))
print(md5_b)

print("")
print("If the MD5 hashes are DIFFERENT,")
print("The disk image is not fit for further analysis.")
print("")

# 3. Access (using fls utility from SleuthKit)

print("")
print("3. USING FLS FROM SLEUTHKIT TO LIST REGULAR AND HIDDEN FILES")
print("")

os.system("fls -r %s" % (diskimagename)) 

print("")
print("Total program running time is %s seconds." % (time.time() - start_time))
print("")