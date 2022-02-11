from itertools import count
from turtle import width
from pip import main
from flask import Flask, render_template
app = Flask(__name__)

black = '<div class="black"></div>'
red = '<div class="red"></div>'

def maker(width,height):
    table = []
    counter = 0
    for x in range(0,height):
        new_row = []
        for i in range(0,width):
            if i % 2 == counter:
                new_row.append(0)
            else:
                new_row.append(1)
        table.append(new_row)
        if counter == 0:
            counter = 1
        else:
            counter = 0
    return table

@app.route('/')
def lvl1():
    table = maker(8,8)
    return  render_template("index.html",black = black, red = red , table = table)

@app.route('/<int:height>')
def lvl2(height):
    table = maker(8,height)
    return  render_template("index.html",black = black, red = red , table = table)

@app.route('/<int:height>/<int:width>')
def lvl3(height,width):
    table = maker(width,height)
    return  render_template("index.html",black = black, red = red , table = table)

@app.route('/<int:height>/<int:width>/<color1>/<color2>')
def lvl4(height,width,color1,color2):
    table = maker(width,height)
    colored1 = f"background-color:{color1};"
    colored2 = f"background-color:{color2};"
    return  render_template("index.html",black = black, red = red , table = table, colored1 = colored1, colored2 = colored2)




if __name__=="__main__":
    app.run(debug=True)

# do = [[1,2,3,4],[2,4,6,8,8]]
# for i in do:
#     print("br")
#     for x in i:
#         print(x)