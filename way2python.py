# Copyright (c) 2011 NayaabKhan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# usage: python way2python.py --numbers=no1:no2:no3 --message="Your message here"

import sys
import getopt
import random
import urllib
import httplib2

# Fill out the following two account details
USERNAME = 'your login phone number'
PASSWORD = 'your password'

version = '0.1beta'

def main(argv):
    try:
        options, remainder = getopt.getopt(argv, 'hn:m:', ['help', 'numbers=', 'message=', 'version'])
        
        if len(options) == 0:
            print_usage()
            sys.exit(2)
        
        for opt, arg in options:
            if opt in ('-h', '--help'):
                print_usage()
                sys.exit(0)
            elif opt in ('-n', '--numbers'):
                numbers = arg.split(':')
            elif opt in ('-m', '--message'):
                message = arg
            elif opt == '--version':
                print 'Way2Python Version', version
                sys.exit(0)
                
        if valid_numbers(numbers) and valid_message(message):
            send_sms(numbers, message)
    except getopt.GetoptError, e:
        print sys.argv[0] + ':', e.msg
        print_usage()
        sys.exit(2)

def valid_numbers(numbers):
    for number in numbers:
        if len(number) <> 10:
            print 'Number', number, 'isn\'t a valid Indian mobile number.'
            return False
    return True

def valid_message(message):
    if len(message) > 140:
        print 'Your message exceeds the limit of 140 characters.'
        return False
    return True

def send_sms(numbers, message):
    server_list = ['site1', 'site2', 'site3', 'site4', 'site5', 'site6']
    server = server_list[random.randint(0, len(server_list) - 1)]
    
    AUTH_URL = 'http://' + server + '.way2sms.com:80/auth.cl'
    SMS_URL = 'http://' + server + '.way2sms.com/FirstServletsms?custid='
    
    http_conn = httplib2.Http()
    
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'}
    body = {'username': USERNAME, 'password': PASSWORD, 'login': 'Login'}
    
    try:
        response, content = http_conn.request(AUTH_URL, 'POST', headers=headers, body=urllib.urlencode(body))
    except:
        print 'Authentication failed, check your login details again.'
        return False
    else:
        print 'Were hooked on to the Way2SMS server!'

    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
               'Cookie': response['set-cookie']}
    
    for number in numbers:
        body = {'custid': 'undefined',
               'HiddenAction': 'instantsms',
               'Action': 'sa65sdf656fdfd',
               'login': '',
               'pass': '',
               'MobNo': number,
               'textArea': message}
           
        try:
            response, content = http_conn.request(SMS_URL, 'POST', headers=headers, body=urllib.urlencode(body))
        except:
            print 'Failed to send to', number
            return False
    
        if content.find('successfully') <> -1:
            print 'Message sent to', number
        else:
            print 'Failed to send to', number

def print_usage():
    print 'usage: python', sys.argv[0], '--numbers=no1:no2:no3 --message="Your message here"'
    
if __name__ == '__main__':
    main(sys.argv[1:])
