from flask import Blueprint,render_template,request
import joblib



# registering views
views = Blueprint('views', __name__)

# loading the ML models
odimodel = joblib.load("D:\\Ashish\\flask-score-predictor\\website\\odimodel.pkl")
t20model = joblib.load("D:\\Ashish\\flask-score-predictor\\website\\t20model.pkl")


@views.route('/')
def home():

  
  return render_template('base.html') 


@views.route("/", methods=["POST"])
def post():
  # handling the post request
  if request.method == "POST":
    
    current_score = int(request.form["current_score"])
    wickets_fallen = int(request.form["wickets_fallen"])
    overs_completed = float(request.form["overs_completed"])
    runs_last_5 = int(request.form["runs_last_5"])
    wickets_last_5 = int(request.form["wickets_last_5"])
    score_of_striker = int(request.form["score_of_striker"])
    score_of_non_striker = int(request.form["score_of_non_striker"])
    format = request.form["format"]
    # data passing to the template
    
    if format == "odi":
      score = odimodel.predict([[current_score,wickets_fallen, overs_completed,runs_last_5,wickets_last_5,score_of_striker,score_of_non_striker]])

      print(f"Seee here ----->  {type(score)} {score}")
      runrate = float(current_score / overs_completed)
      
      
      return render_template("base.html", x=round(score[0][0]), y=round(runrate,2),match_format=format.upper())

    else:
      score = t20model.predict([[current_score,wickets_fallen, overs_completed,runs_last_5,wickets_last_5,score_of_striker,score_of_non_striker]])
      

      print(f"Seee here ----->  {type(score)} {score}")


      runrate = float(current_score / overs_completed)

      
      return render_template("base.html", x=round(score[0][0]), y=round(runrate,2),match_format=format.upper())
      

    # cur_run_rate = current_score / overs_completed

    

    
    
