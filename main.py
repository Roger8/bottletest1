# coding=utf-8

# coding=utf-8
from bottle import route, run, template, static_file, abort, redirect, request
from bottle import response, view
import socket

@route('/')
@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again "
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/myip')
def showip():
	ip = request.environ.get('REMOTE_ADDR')
	return 'youre ip is :{}'.format(ip)
		
@route('/wrongurl')
def wrong():
	redirect('/hello/boy')

@route('/restricted')
def restricted():
	abort(401,'sorry , access denied.')
	
@route('/list')	
@view('listfiles')
def list():
	import os
	fils = os.listdir('c:/bottle/file_form_upload')
	return template('listfiles', folders = fils)

    

@route('/files/<filename:path>')
def send_file(filename):
    return static_file(filename, root='C:/bottle/file_form_upload',download=filename)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
	
@route('/upload')
@view('listfiles')
def upload():
        import os
	fils = os.listdir('c:/bottle/file_form_upload')
	return template('listfiles', folders = fils)
## template : listfiles
##	return '''
##<html>
##<meta charset="UTF-8"> 
##<form action"/upload" method="post" enctype="multipart/form-data">
##                    <input type="file" name="data" />
##                    <input type="submit" value="Upload" />
##</form>
##<hr>
##<h2  > index of files/ </h2>
##
##% for fd in folders:
##	<a click to download > </a>
##	<br>
##	<a href='/files/{{fd}}'>
##	<b>  {{fd}}</b>
##	<br>
##	</a>
##% end
##
##</html>
##	'''
@route('/upload',method = 'POST')
def do_upload():
	save_path = 'C:/bottle/file_form_upload'
	upfile = request.files.get('data')
	upfile.save(save_path,overwrite=True)
	print upfile.filename + 'upload success.'
	redirect('/upload')


myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
run(host=myaddr, port=8080)#localhost
