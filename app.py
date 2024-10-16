from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def inicio():
    return render_template('inicio.html')

# Ruta para la página de "Quiénes Somos"
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Ruta para la página de "Servicios"
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para la página de "Noticias"
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Ruta para la página de "Contacto"
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Procesa el formulario
        nombre = request.form['nombre']
        email = request.form['email']
        message = request.form['message']
        # Aquí se podría agregar lógica para guardar los datos o enviarlos por email
        return redirect(url_for('inicio'))  # Cambié render_template por redirect
    return render_template('contacto.html')
       

if __name__ == '__main__':
    app.run(debug=True)