
import os

rootdir = '/Users/mcbobs/projects/python/'

def travel(mode=True):
    for dir_name, sub_dir, file_list in os.walk(rootdir, topdown=mode):
        print "Directory name is %s " % dir_name
        for fl in file_list:
            print "\t%s" % fl

travel()
travel(False)

