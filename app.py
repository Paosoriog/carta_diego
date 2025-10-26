from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def carta():
    # Asumimos que esta foto es la que se muestra en la carta principal (IMG_20250421_104044_252.jpg)
    foto_sorpresa_url = 'IMG_20250421_104044_252.jpg' 
    
    carta_texto = """Mi amor 💌

Te amo desde el primer día que te vi, cuando vi tus ojos tan bellos color miel y tu carita tan linda.
estos meses han sido lo mas lindo que me ha pasado, sé que no te puedo comprar cosas caras pero te hice esta pagina dedicada a ti para que veas lo mucho que te amo.
Con todo mi cariño,
[Te amo mi Dieguito hermoso <3] 
"""
    # Pasamos la URL de la foto principal y el texto a la plantilla
    return render_template('carta.html', carta=carta_texto, foto_url=foto_sorpresa_url)

@app.route('/fotos')
def galeria():
    # Usamos la foto principal para la galería general
    fotos = [
        'IMG_20250421_104044_252.jpg'
    ]
    return render_template('fotos.html', fotos=fotos)

@app.route('/darice')
def darice():
    # Lista de fotos de Darice que se usarán en darice.html
    fotos_darice = [
        '20251004_183124.jpg',     
        'IMG_20250823_112647_607.webp'     
    ]
    return render_template('darice.html', fotos_darice=fotos_darice)

# RUTA AGREGADA PARA LA PÁGINA DE KITTY
@app.route('/kitty')
def kitty_page():
    # Simplemente renderiza la plantilla kitty.html que usa las imágenes directamente
    return render_template('kitty.html')

if __name__ == '__main__':
    app.run(debug=True)