from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='password',
            database='postgres'
        )
        cursor = connection.cursor()

        # Obtener datos del formulario
        cliente = request.form['cliente']
        proyecto_servicio = request.form['proyecto_servicio']
        contacto = request.form['contacto']
        cargo = request.form['cargo']
        pregunta1 = request.form['pregunta1']
        pregunta2 = request.form['pregunta2']
        pregunta3 = request.form['pregunta3']
        pregunta4 = request.form['pregunta4']
        pregunta5 = request.form['pregunta5']
        pregunta6 = request.form['pregunta6']
        pregunta7 = request.form['pregunta7']
        pregunta8 = request.form['pregunta8']
        pregunta9 = request.form['pregunta9']
        pregunta10 = request.form['pregunta10']
        comentario_recomendacion = request.form['comentario_recomendacion']

        # Insertar datos en la base de datos
        cursor.execute("""
            INSERT INTO ClienteEncu (cliente, proyecto_servicio, contacto, cargo,
                                    pregunta1, pregunta2, pregunta3, pregunta4, pregunta5,
                                    pregunta6, pregunta7, pregunta8, pregunta9, pregunta10,
                                    comentario_recomendacion)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (cliente, proyecto_servicio, contacto, cargo,
              pregunta1, pregunta2, pregunta3, pregunta4, pregunta5,
              pregunta6, pregunta7, pregunta8, pregunta9, pregunta10,
              comentario_recomendacion))

        connection.commit()

        return redirect('/')
    except Exception as ex:
        print("Error al procesar la solicitud:", ex)
        return "Hubo un error al procesar la solicitud."
    finally:
        if connection:
            connection.close()


@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    app.run(debug=True)