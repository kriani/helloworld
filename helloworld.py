#hello world program
#urllib3 package kiprobalasa

import urllib3

print ("Hello world!")
print('urllib3 package: ')
print(dir(urllib3))

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print('status number: ', r.status)
print('data in the robots.txt file from http://httpbin.org/robots.txt:')
print(r.data)
