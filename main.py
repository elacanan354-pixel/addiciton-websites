@app.route("//")
def hello_world():
    return render_template("index.html")
@app.route("/MARVEL_facts")
def marvel():
    MARVEL_facts=["Tony would win  ciwil war if the movies name wasnt captain america",
          "captain marvel was strong enough to handle with infinity stones",
           "Steve would choose peggy over bucky all the time and bucky knows it",
            "silvie  is a devil with big hornes", ]
    return f"<p>{random.choice(MARVEL_facts)}</p>"

if __name__ == "__main__":
 app.run(debug=True)
