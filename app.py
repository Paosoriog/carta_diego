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
    # *** CORREGIDO: SOLO LISTAMOS LAS FOTOS QUE SABEMOS QUE EXISTEN ***
    # La foto principal IMG_20250421_104044_252.jpg aparecerá aquí.
    # Eliminamos 'foto2.jpg' y 'foto3.jpg' para que no crashee.
    fotos = [
        'IMG_20250421_104044_252.jpg'
    ]
    return render_template('fotos.html', fotos=fotos)

@app.route('/darice')
def darice():
    # *** CORREGIDO: USAMOS LOS NOMBRES EXACTOS DE LOS ARCHIVOS TRIPLE EXTENSIÓN ***
    # Si los archivos en static/ tienen otros nombres, FALLARÁ.
    fotos_darice = [
        'darice1.jpg.jpg.jpg',     # Usando el nombre con triple extensión
        'darice2.jpg.webp.webp'    # Usando el nombre con doble extensión
    ]
    return render_template('darice.html', fotos_darice=fotos_darice)


if __name__ == '__main__':
    app.run(debug=True)
