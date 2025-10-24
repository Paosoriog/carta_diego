from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def carta():
    carta_texto = """Mi amor 💌

Te amo desde el primer día que te vi, cuando vi tus ojos tan bellos color miel y tu carita tan linda.
estos meses han sido lo mas lindo que me ha pasado, sé que no te puedo comprar cosas caras pero te hice esta pagina dedicada a ti para que veas lo mucho que te amo.
Con todo mi cariño,
[Te amo mi Dieguito hermoso <3] 
"""
    return render_template('carta.html', carta=carta_texto)

@app.route('/fotos')
def galeria():
    # ATENCIÓN: Si 'foto2.jpg' o 'foto3.jpg' NO existen en static/, borra esas líneas o fallará.
    fotos = [
        'IMG_20250421_104044_252.jpg',
        'darice1.jpg.jpg.jpg', # Reemplaza con tus nombres de archivo reales
        'darice2.jpg.webp.webp'
    ]
    return render_template('fotos.html', fotos=fotos)

@app.route('/darice')
def darice():
    # ***IMPORTANTE: USAMOS LOS NOMBRES EXACTOS DE LOS ARCHIVOS QUE ACABAS DE SUBIR***
    # Deben coincidir con los archivos que tienes en la carpeta static/
    fotos_darice = [
        'darice1.jpg.jpg.jpg',     # ¡Triple extensión JPG!
        'darice2.jpg.webp.webp'    # ¡Doble extensión WEBP!
    ]
    return render_template('darice.html', fotos_darice=fotos_darice)


if __name__ == '__main__':
    app.run(debug=True)
