from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import Paciente, Cita

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Configurar Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Usuarios de ejemplo (reemplaza con tu propio sistema de usuarios)
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

# Listas para almacenar pacientes y citas
pacientes = []

citas = []

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(username):
    if username not in users:
        return None
    user = User()
    user.id = username
    return user

@app.route('/')
@login_required
def index():
    return render_template('index.html', pacientes=pacientes, citas=citas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas. Por favor, inténtalo de nuevo.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Cierre de sesión exitoso', 'success')
    return redirect(url_for('login'))

@app.route('/agregar_paciente', methods=['POST'])
@login_required
def agregar_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        dni = request.form['dni']

        paciente = Paciente(nombre, edad, dni)
        pacientes.append(paciente)

    return redirect('/')

@app.route('/agregar_cita', methods=['POST'])
@login_required
def agregar_cita():
    if request.method == 'POST':
        dni = request.form['dni']
        fecha = request.form['fecha']
        motivo = request.form['motivo']

        cita = Cita(dni, fecha, motivo)
        citas.append(cita)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
