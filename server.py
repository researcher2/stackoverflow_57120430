from flask import request, render_template, session

from app import app, db

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        searchQuery = request.form.get("searchQuery")
        print(searchQuery)

        # Avoid SQL Injection Using Bindings
        sql = "SELECT isbn, author, title \
               FROM book \
               WHERE isbn LIKE :x \
               OR author LIKE :y \
               OR title LIKE :z"

        # I spent an hour wondering why I couldnt put the bindings inside the wildcard string...
        # https://stackoverflow.com/questions/3105249/python-sqlite-parameter-substitution-with-wildcards-in-like
        matchString = "%{}%".format(searchQuery)

        stmt = db.text(sql).bindparams(x=matchString, y=matchString, z=matchString)

        results = db.session.execute(stmt).fetchall()
        print(results)

        session["books"] = []

        for row in results:
            # A row is not JSON serializable so we pull out the pieces
            book = dict()
            book["isbn"] = row[0]
            book["author"] = row[1]
            book["title"] = row[2]
            session["books"].append(book)
        return render_template("index.html", searchedFor=searchQuery, books=session["books"])

    return render_template("index.html")