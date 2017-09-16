from bottle import post, run, request, get

from sample.serialiser import save_samples


@get('/')
def hello():
    return 'Hello!'


@post('/samples')
def output_reading():
    save_samples(request.body.read())


run(host='0.0.0.0', port=8081, debug=True)
