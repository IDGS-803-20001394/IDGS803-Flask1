from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET","POST"])
def operasBas():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "La suma es: {}".format(str(int(num1)+int(num2)))
    else:
        return '''            
            <form action="/operasBas" method="post">
            <Label>Num 1:</Label>
            <input type="text" name="num1"></br></br>

            <Label>Num 2:</Label>
            <input type="text" name="num2"></br></br>
            <input type="submit" value="Calcular">
            </form
        '''

if __name__ == "__main__":
    app.run(debug=True)