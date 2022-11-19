from app import app

@app.route('/')
@app.route('/index')
def index():
    user =  {'username': 'foo'}
    return '''  
<html>
    <head>
        <title>HomePage - Microblog</title>
    </head>

    <body>
        <h1>Hello ''' + user['username'] + '''!</h1>
    </body> 
</html>
    
    '''
