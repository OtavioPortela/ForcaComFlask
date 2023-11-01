from app import app
import os

if __name__ == 'main':
    port = int(os.getenv('PORT'), 8000) #Configurando para o Heroko
    app.run(host='0.0.0.0', port=port)
