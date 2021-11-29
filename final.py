from flask import Flask,jsonify,request
from storage import allmovies,likedmovies,notlikedmovies,didnotwatchmovies
from demographicfiltering import output
from contentfiltering import getrecommendations
app=Flask(__name__)

@app.route("/get-movie")
def getmovie():
    moviedata={
        "title":allmovies[0][19],
        "poster_link":allmovies[0][27],
        "release_date":allmovies[0][13] or "N/A",
        "duration":allmovies[0][15],
        "rating":allmovies[0][20],
        "overview":allmovies[0][9],
    }
    return jsonify({
        "data":moviedata,
        "status":"sucess"
    })

@app.route("/liked-movie",methods=["POST"])
def likedmovie():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    likedmovies.append(movie)
    allmovies.pop(0)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/notliked-movie",methods=["POST"])
def notlikedmovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    notlikedmovies.append(movie)
    allmovies.pop(0)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/didnotwatch-movie",methods=["POST"])
def didnotwatchmovie():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    didnotwatchmovies.append(movie)
    allmovies.pop(0)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/popular-movies")
def popularmovies():
    moviedata=[]
    for i in output:
        _d={
            "title":i[0],
            "poster_link":i[1],
            "release_date":i[2],
            "duration":i[3],
            "rating":i[4],
            "overview":i[5],
            
        }
        moviedata.append(_d)
    return jsonify({
        "data":moviedata,
        "status":"sucess"
    })

@app.route("/recommended-movies")
def recommendedmovies():
    allrecommended=[]
    for i in likedmovies:
        output=getrecommendations(i[19])
        for i in output:
            allrecommended.append(data)
    import itertools
    allrecommended.sort()
    allrecommended=list(allrecommended for allrecommended,_ in itertools.groupby(allrecommended))
    moviedata=[]
    for i in recommended:
        _d={
            "title":i[0],
            "poster_link":i[1],
            "release_date":i[2],
            "duration":i[3],
            "rating":i[4],
            "overview":i[5],
            
        }
        moviedata.append(_d)
    return jsonify({
        "data":moviedata,
        "status":"sucess"
    })
if __name__=="__main__":
    app.run()