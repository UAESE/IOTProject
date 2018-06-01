from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)
teamDB=[
    {
    'id':'1',
    'name':'Ahmad Gamal'
    },
    {
    'id':'2',
    'name':'Ahmad Muammar'
     },
     {
     'id':'3',
     'name':'Andre Agaybe'
     },
     {
     'id':'4',
    'name':'Mohammed Mysara'
     },
     {'id':'5',
    'name':'Yehya Shazli'}            
] 



@app.route('/')
def func():
  
   # return render_template('index.html')
     return jsonify({'team':teamDB})
@app.route('/team/<teamID>',methods=['GET'])
def getTeamID(teamID):
	usr=[emp for emp in teamDB if (emp['id']==teamID)]
	return jsonify ({'emp':usr})

@app.route('/team',methods=['GET'])
def getAllTeam():

   # return render_template('index.html')
     return jsonify({'team':teamDB})




 		
if __name__ == '__main__':
    app.run(host="0.0.0.0",port='5001',debug=True)
