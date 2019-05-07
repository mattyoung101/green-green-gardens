from flask import Flask, render_template
import csv
from dataclasses import dataclass
app = Flask(__name__)

@dataclass
class StoreItem:
    item_id: int
    name: str
    in_stock: bool
    image: str
    category: str
    saleprice: str
    prodprice: str
    sku: str

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

@app.route("/browse")
def browse():
    data = []
    with open("GE_data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lines = [x for x in reader]
        for line in lines[1::]:
            data.append(StoreItem(
                item_id=int(line[0]),
                name=line[1],
                in_stock=line[2] == "instock",
                image=line[3],
                category=line[7], # TODO format category,
                saleprice=line[4],
                prodprice=line[5],
                sku=line[6]
                ))
    return render_template("browse.html", data=chunks(data, 3))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/help")
def help():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True)