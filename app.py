from flask import Flask, render_template, request

app = Flask(__name__)

get_counter = 0
post_counter = 0
put_counter = 0
delete_counter = 0


@app.route('/')
def route_home():
    return render_template('home_page.html',
                           get_counter=get_counter,
                           post_counter=post_counter)


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_request():
    global post_counter
    global get_counter
    global delete_counter
    global put_counter
    if request.method == 'GET':
        get_counter += 1
        return render_template('home_page.html',
                               get_counter=get_counter,
                               post_counter=post_counter,
                               put_counter=put_counter,
                               delete_counter=delete_counter)

    elif request.method == 'POST':
        post_counter += 1
        return render_template("home_page.html",
                               get_counter=get_counter,
                               post_counter=post_counter)
    elif request.method == 'PUT':
        put_counter += 1
        return render_template('home_page.html',
                               get_counter=get_counter,
                               post_counter=post_counter,
                               put_counter=put_counter,
                               delete_counter=delete_counter)
    elif request.method == 'DELETE':
        delete_counter += 1
        return render_template('home_page.html',
                               get_counter=get_counter,
                               post_counter=post_counter,
                               put_counter=put_counter,
                               delete_counter=delete_counter)


@app.route('/statistic')
def route_statistic():
    return render_template('statistic.html',
                           get_counter=get_counter,
                           post_counter=post_counter,
                           put_counter=put_counter,
                           delete_counter=delete_counter)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True)
