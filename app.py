from flask import Flask, render_template
from functions import *

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    first_name = getUsersInfo.first_name
    last_name = getUsersInfo.last_name
    return render_template('index.html', first_name=first_name, last_name=last_name)


@app.route('/user')
def user():
    first_name = getUsersInfo.first_name
    last_name = getUsersInfo.last_name
    id = getUsersInfo.id
    bdate = getUsersInfo.bdate
    city = getUsersInfo.city
    countFriends = getFriends.countFriends
    AlbumCounts = getAlbumCounts.AlbumCounts

    return render_template('user.html', first_name=first_name, last_name=last_name, id=id, bdate=bdate, city=city,
                           countFriends=countFriends, AlbumCounts=AlbumCounts)


@app.route('/friends')
def friends():
    return render_template('friends.html')


if __name__ == '__main__':
    app.run(debug=True)
