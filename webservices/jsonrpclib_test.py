import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoodb'
USER = 'admin'
PASS = 'admin'

# server proxy object
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
server = jsonrpclib.Server(url)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])

# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    return server.call(service="object", method="execute", args=args)

# create a new note
args = {
    'name' : 'Course Json created from json webservice',
    'color' : '63',
    'create_uid' : uid,
    'course_id' : 2, #course_id required so we investigate an available course_id and use it
}

def get_course_id(model, method, *args2):
    args2 = [DB, uid, PASS, model, method] + list(args2)
    return server.call(service="object", method="execute", args=args2)

args2 = {
    'name': [('name','ilike', '0')],
}

course_id = get_course_id('openacademy.course', 'search', args2)

note_id = invoke('openacademy.session', 'create', args)
