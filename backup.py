import os
import time
#example on mac os or linux
source = ['/home/dimpleraje/PycharmProjects/prasad2/main.py']
target_dir = '/home/dimpleraje/PycharmProjects/prasad2/backup'
#The name of the zip archive is the current date and time
target = target_dir + os.sep + \
         time.strftime('%y%m%d%h%m%s') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('zip command is:')
print(zip_command)
print('running')
if os.system(zip_command) == 0:
    print('successful backup to',target)
else:
    print('backup failed')