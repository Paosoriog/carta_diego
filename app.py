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
    fotos = [
        'IMG_20250421_104044_252.jpg',  # Tu foto actual
        'foto2.jpg',
        'foto3.jpg'
        # ¡Agrega aquí todas tus fotos de la galería general!
    ]
    return render_template('fotos.html', fotos=fotos)

# ¡NUEVA RUTA PARA DARICE AQUÍ!
@app.route('/darice')
def darice():
    fotos_darice = [
        'darice1.jpg', # La primera foto de Darice
        'darice2.jpg'  # La segunda foto de Darice
        # Si tienes más fotos de Darice, añádelas aquí.
    ]
    return render_template('darice.html', fotos_darice=fotos_darice)


if __name__ == '__main__':
    app.run(debug=True)