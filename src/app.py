from flask import redirect, render_template, request, jsonify, flash, send_file
from db_helper import reset_db
from repositories.book_repository import add_user_book, get_books
from repositories.article_repository import add_user_article, get_articles
from repositories.inproceeding_repository import add_user_inproceeding, get_inproceedings
from config import app, test_env
from util import validate_book
from export import Bibtex

@app.route("/")
def index():

    return render_template("index.html") 

@app.route("/add_reference", methods=["GET"])
def add_reference():

    return render_template("add_reference.html")

@app.route("/add_book", methods=["GET"])
def add_book():
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return render_template("add_book.html", months = months)

@app.route("/add_book", methods=["POST"])
def add_POST_book():

    aut = request.form["author"]
    tit = request.form["title"]
    pub = request.form["publisher"]
    year = request.form["year"]
    edt = request.form.get("editor") or None
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None

    reference = [aut, tit, pub, year, edt, vol, num, pages, month, note]

    try:
        validate_book(reference)
        add_user_book(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Publisher And Year',"")
        return redirect("/add_book")

@app.route("/view_references")
def view_references():

    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    return render_template("view_references.html", books=books, articles=articles, inproceedings=inproceedings)

@app.route("/add_article", methods = ["GET"])
def add_article():

    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return render_template("add_article.html", months = months)

@app.route("/add_article", methods = ["POST"])
def add_POST_article():

    aut = request.form["author"]
    tit = request.form["title"]
    jou = request.form["journal"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None

    reference = [aut, tit, jou, year, vol, num, pages, month, note]

    try:
        validate_book(reference)
        add_user_article(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Journal And Year',"")
        return redirect("/add_article")
    

@app.route("/add_inproceeding", methods = ["GET"])
def add_inproceeding():

    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return render_template("add_inproceeding.html", months = months)

@app.route("/add_inproceeding", methods=["POST"])
def add_POST_inproceeding():

    aut = request.form["author"]
    tit = request.form["title"]
    bti = request.form["booktitle"]
    year = request.form["year"]
    edt = request.form.get("editor") or None
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    series = request.form.get("series") or None
    pages = request.form.get("pages") or None
    address = request.form.get("address") or None
    month = request.form.get("month") or None
    org = request.form.get("organization") or None
    publisher = request.form.get("publisher") or None

    reference = [aut, tit, bti, year, edt, vol, num, series, pages, address, month, org, publisher]

    try:
        validate_book(reference)
        add_user_inproceeding(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Publisher And Year',"")
        return redirect("/add_inproceeding")

@app.route("/export", methods=["GET"])
def export():

    books = get_books()

    bibtex = Bibtex()
    bibtex.create_book_bibtex(books)

    return send_file(
        "bibtex.bib",
        as_attachment = True,
        download_name = "references.bib",
        mimetype = "text/plain"
    )

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
