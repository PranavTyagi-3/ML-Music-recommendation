from flask import Flask,render_template,request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Authentication
client_credentials_manager = SpotifyClientCredentials(client_id='4b4cb4f8525543959104a2168e29e1c9', client_secret='8ea4d3b6032c4a35ba22999240e6859d')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

app=Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
    if request.method=="POST":
        song=request.form.get('song')
        s=sp.search(song,limit=1)['tracks']['items'][0]
        sname=s['album']['name']
        try:
            aname=s['album']['artists'][0]['name']+", "+s['album']['artists'][1]['name']
        except:
            aname=s['album']['artists'][0]['name']
        img=s['album']['images'][1]['url']
        return render_template('index.html',sname=sname,aname=aname,img=img)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)
