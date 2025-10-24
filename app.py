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
    # Usamos la foto principal para la galería general
    fotos = [
        'IMG_20250421_104044_252.jpg'
    ]
    return render_template('fotos.html', fotos=fotos)

@app.route('/darice')
def darice():
    # *** USAMOS LOS NOMBRES EXACTOS DE LAS DOS FOTOS DE DARICE ***
    # Si estos nombres no coinciden exactamente con los archivos en static/ el servidor fallará (error 500).
    fotos_darice = [
        '20251004_183124.jpg',     
        'IMG_20250823_112647_607.webp'    
    ]
    return render_template('darice.html', fotos_darice=fotos_darice)


if __name__ == '__main__':
    app.run(debug=True)