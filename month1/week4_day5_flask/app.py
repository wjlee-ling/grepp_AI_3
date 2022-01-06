"""
to-do: 
1. connect to SQL
2. upgrade the echo function 
3. update/delete시 client가 suffix '-s' 붙여서 할 경우 고려
"""

from flask import Flask, jsonify, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from helper import weapons, stocks

app = Flask(__name__)
app.config['SECRET_KEY']= "D343DF"

class My_Form(FlaskForm):
    weapon = StringField("Weapon")
    stock = IntegerField("Stock")
    update = SubmitField("Update")
    delete = SubmitField("Delete")

@app.route("/")
def index():
    return render_template("index.html", template_weapons= weapons)

@app.route("/whoami")
def about():
    return render_template("about.html")

@app.route("/echo")
def echo():
    input_string = request.args.get("string")
    return jsonify({"value": input_string}) ## 세련되게 고치기

@app.route("/weapons", methods=['GET', 'POST'])
def update_weapons():
    weapon_form = My_Form()
    if weapon_form.weapon.data: # 없으면 처음 액세스시 오류
        # update
        if weapon_form.update.data is True:
            if weapon_form.weapon.data.lower() not in weapons.values(): # 새 무기 추가
                new_id = len(weapons)+1
                weapons[new_id] = weapon_form.weapon.data
                stocks[new_id] = weapon_form.stock.data
            else: 
                for id, weapon in weapons.items():
                    if weapon.lower() == weapon_form.weapon.data.lower():
                        print(weapon_form.stock.data)
                        stocks[id] = weapon_form.stock.data
                        print(f'===={stocks}======')
        # or delete 
        elif weapon_form.delete.data is True:
            for id, weapon in weapons.items():
                if weapon.lower() == weapon_form.weapon.data.lower():
                    del(weapons[id])
                    del(stocks[id])
                    break        

    return render_template("weapons.html", template_weapons= weapons, template_stocks=stocks, template_form= weapon_form)

if __name__ == "__main__":
    app.run()
