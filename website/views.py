from flask import Blueprint, render_template, request, flash, redirect, url_for
from foaas import fuck
from .fucks import *
views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    ways = [
        {"type":"awesome", "message": "When something is so awesome that you are pleased to swear..."},
        {"type": "ballmer", "message": "When you are very irritated with someone when his company..."},
        {"type": "because", "message": "When someone asks you why and an obvious answer is there..."},
        {"type": "bus", "message": "Reference from a film"},
        {"type": "bye", "message": "Seems unnecessary but it is not"},
        {"type": "caniuse", "message": "If only you ask for a permission"},
        {"type": "chainsaw", "message": "fucking tired of noraml life"},
        {"type": "diabetes", "message": "Your beloving freind come up to talk to you and..."},
        {"type": "donut", "message": "Fancy The Rolling Donut?"},
        {"type": "everyone", "message": "Poeple do get really annying, do not they?"},
        {"type": "everything", "message": "Yolo"},
        {"type": "fascinating", "message": "bruh you are talking quite a lot"},
        {"type": "king", "message": "You rule the world, your majesty"},
        {"type": "life", "message": "Sometimes people get pessimistic but in a good way"},
        {"type": "nugget", "message": "I do not even know what this exoression truly means. But who does?"},
    ]
    return render_template("home.html", ways=ways)

@views.route("/awesome", methods=["POST", "GET"])
def awesome():
    if request.method == "POST":
        name = request.form.get("name")
        print(name)
        if name:
            message = fuck.awesome(from_=name).text
            return render_template("awesome.html", message=message)
    return render_template("awesome.html")

@views.route("/ballmer", methods=["POST", "GET"])
def ballmer():
    if request.method == "POST":
        name = request.form.get("name")
        company = request.form.get("company")
        from_ = request.form.get("from")

        if name and company and from_:
            message = fuck.ballmer(name=name, company=company, from_=from_).text
            return render_template("ballmer.html", message=message)

    return render_template("ballmer.html")

@views.route("/because", methods=["POST", "GET"])
def because():
    if request.method == "POST":
        name = request.form.get("name")
        print(name)
        if name:
            message = fuck.because(from_=name).text
            return render_template("because.html", message=message)
    return render_template("because.html")

@views.route("/bus", methods=["POST", "GET"])
def bus():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        print(name)
        if name and from_:
            message = fuck.bus(name=name, from_=from_).text
            return render_template("bus.html", message=message)
    return render_template("bus.html")

@views.route("/bye", methods=["POST", "GET"])
def bye():
    if request.method == "POST":
        from_ = request.form.get("from")
        print(from_)
        if from_:
            message = fuck.bye(from_=from_).text
            return render_template("bye.html", message=message)
    return render_template("bye.html")

@views.route("/caniuse", methods=["POST", "GET"])
def caniuse():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        if name and from_:
            message = fuck.caniuse(name=name, from_=from_).text
            return render_template("caniuse.html", message=message)
    return render_template("caniuse.html")

@views.route("/chainsaw", methods=["POST", "GET"])
def chainsaw():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        print(name)
        if name and from_:
            message = fuck.chainsaw(name=name, from_=from_).text
            return render_template("chainsaw.html", message=message)
    return render_template("chainsaw.html")


@views.route("/diabetes", methods=["POST", "GET"])
def diabetes():
    if request.method == "POST":
        from_ = request.form.get("from")
        if from_:
            message = fuck.diabetes(from_=from_).text
            return render_template("diabetes.html", message=message)
    return render_template("diabetes.html")


@views.route("/donut", methods=["POST", "GET"])
def donut():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        print(name)
        if name and from_:
            message = fuck.donut(name=name, from_=from_).text
            return render_template("donut.html", message=message)
    return render_template("donut.html")

@views.route("/everyone", methods=["POST", "GET"])
def everyone():
    if request.method == "POST":
        from_ = request.form.get("from")
        if from_:
            message = fuck.everyone(from_=from_).text
            return render_template("everyone.html", message=message)
    return render_template("everyone.html")

@views.route("/everything", methods=["POST", "GET"])
def everything():
    if request.method == "POST":
        from_ = request.form.get("from")
        if from_:
            message = fuck.everything(from_=from_).text
            return render_template("everything.html", message=message)
    return render_template("everything.html")

@views.route("/fascinating", methods=["POST", "GET"])
def fascinating():
    if request.method == "POST":
        from_ = request.form.get("from")
        if from_:
            message = fuck.fascinating(from_=from_).text
            return render_template("fascinating.html", message=message)
    return render_template("fascinating.html")

@views.route("/king", methods=["POST", "GET"])
def king():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        print(name)
        if name and from_:
            message = fuck.king(name=name, from_=from_).text
            return render_template("king.html", message=message)
    return render_template("king.html")

@views.route("/life", methods=["POST", "GET"])
def life():
    if request.method == "POST":
        from_ = request.form.get("from")
        if from_:
            message = fuck.life(from_=from_).text
            return render_template("life.html", message=message)
    return render_template("life.html")

@views.route("/nugget", methods=["POST", "GET"])
def nugget():
    if request.method == "POST":
        name = request.form.get("name")
        from_ = request.form.get("from")
        print(name)
        if name and from_:
            message = fuck.nugget(name=name, from_=from_).text
            return render_template("nugget.html", message=message)
    return render_template("nugget.html")