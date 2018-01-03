import sys
retry_limit = 3
retry_count = 0

account_file ='account.txt'

lock_file = 'account_lock.txt'
with open(account_file,'w') as l:
    l.write('liwei 123456')
open(lock_file,"w")
while retry_count < retry_limit:
    username = input('Enter your name:')
    lock_check = open(lock_file,'r')

    for line in lock_check.readlines():
        if username in line:
            sys.exit
    passwd = input('password:')
    f = open(account_file,'r')
    match_flag = False
    for line in f.readlines():
        user,password = line.strip('\n').split()
        if user == username and passwd == password:
            print('welcome to beijing')
            match_flag = True
            break
       # else:
        #    print('wrong user name or password')
    f.close()
            
    if match_flag == False:
        print('wrong user name or password')
        retry_count += 1
    else:
        print('北京欢迎你!')
else:
    print('your accont is locked')
    f = open(lock_file,"a")
    f.write(username)
    f.close()
