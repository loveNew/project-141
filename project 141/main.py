from flask import Flask,request,jsonify
import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open("articles.csv") as f:
    data1 = csv.reader(f)
    data = list(data1)
    all_articles = data[1:]

app = Flask(__name__)

