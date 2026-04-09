from flask import Flask,render_template

#initializing the flask app,,mtlb flask ki chezon ko agay use krna hai
app = Flask(__name__)

#routing: path un pages ka jo browser mn open hny chahiye,,,is se path set krty hyn
@app.route("/")
def test():
    page_title = "My Main Page"
    return render_template("test.html",title = page_title)
 #ye text browser mn show hoga

@app.route("/about")   #http://127.0.0.1:5000/sample  is path pr jany pr sample function run hoga
def sample():
    page_title = "About Us"
    return render_template("about.html",) #ye text browser mn show hoga
#run the flask app
if __name__ == "__main__": #is line se auto ee run hon gy funtion manually call krny ki zarurat nahi
    app.run(debug=True)