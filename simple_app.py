import justpy as jp


def app():
    # Initiate a webpage
    wp = jp.QuasarPage()
    # Formmating : https://quasar.dev/style/shadows (refer this link)
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    return wp


jp.justpy(app)
