from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/sub')
def homepage():
    return render_template('sub.html')

@app.route("/final", methods=['POST', 'GET'])
def sub():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        c = request.form.get('city')
        
        return  render_template('final.html',name=n,age=a,city=c)

if __name__ == "__main__":
    app.run(debug=True)