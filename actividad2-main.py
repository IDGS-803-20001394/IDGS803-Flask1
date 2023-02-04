from flask import Flask, render_template
from flask import request

app=Flask(__name__)

class calculos():
    precioBoleto = 12.000
    nombre = ""
    cantidadCompradores = 0
    cantidadBoletos = 0
    pagoCineco = False

    def validarCompra(self):
        boletosPermitidos = self.cantidadCompradores * 7
        if self.cantidadBoletos <= boletosPermitidos and self.cantidadBoletos > 0:
            return boletosPermitidos
        else:
            return 0

    def realizarCalculo(self):
        res = self.cantidadBoletos * self.precioBoleto
            
        if self.cantidadBoletos > 5:
               res = res - (res * 0.15)
        elif self.cantidadBoletos > 2 and self.pagoCineco < 5 :
            res = res - (res * 0.10)
        if self.pagoCineco == True:
               res = res - (res * 0.10)
        return res


@app.route("/")
def index():
    
    return render_template("actividad2-index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form.get("txtNombre")
    cantidadCompradores = request.form.get("txtCantCompradores")
    cantidadBoletos = request.form.get("txtCantBoletos")
    pagoCineco = request.form.get("opcCineco")
    
    obj = calculos()
    obj.nombre = nombre
    obj.cantidadCompradores = int(cantidadCompradores)
    obj.cantidadBoletos = int(cantidadBoletos)
    if pagoCineco == "1":
        obj.pagoCineco = True
    else:
        obj.pagoCineco = False
    
    maxPermitidos = obj.validarCompra()

    if maxPermitidos != 0:
        res = obj.realizarCalculo()
        print(res)
        return render_template("actividad2-res.html", nombre=nombre, permitidos=maxPermitidos, pedidos =cantidadBoletos, total=res)    
    else:
        boletosPermitidos = int(cantidadCompradores) * 7
        return render_template("actividad2-error.html", permitidos=boletosPermitidos, pedidos =cantidadBoletos)    



if __name__ == "__main__":
    app.run(debug=True)
