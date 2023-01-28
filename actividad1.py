from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET","POST"])
def operasBas():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        opcion = request.form.get("opcion")

        if(opcion == '1'):
            return "La suma es: {}".format(str(int(num1)+int(num2)))
        elif(opcion == '2'):
            return "La resta es: {}".format(str(int(num1)-int(num2)))
        elif(opcion == '3'):
            return "La multiplicacion es: {}".format(str(int(num1)*int(num2)))
        elif(opcion == '4'):
            return "La division es: {}".format(str(int(num1)/int(num2)))
        else:
            return "No se selecciono una opcion"
    else:
        return '''            
            <form action="/operasBas" method="post">
            <Label>Num 1:</Label>
            <input type="text" name="num1"></br></br>

            <Label>Num 2:</Label>
            <input type="text" name="num2"></br></br>

            <Label>Operacion:</Label></br>
            <input type="radio" name="opcion" value='1' >Suma</br>
            <input type="radio" name="opcion" value='2' >Resta</br>
            <input type="radio" name="opcion" value='3' >Multiplicacion</br>
            <input type="radio" name="opcion" value='4' >Division</br>
            </br>
            <input type="submit" value="Calcular">
            </form
        '''

if __name__ == "__main__":
    app.run(debug=True)