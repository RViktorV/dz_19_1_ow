from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_html():
    # URL на ваш файл web.html в репозитории GitHub
    url = 'https://raw.githubusercontent.com/RViktorV/dz_19_1_ow/main/web.html'
    response = requests.get(url)

    if response.status_code == 200:
        # Возвращаем содержимое файла web.html
        return Response(response.text, mimetype='text/html')
    else:
        return Response('Не удалось загрузить страницу.', status=500)

if __name__ == '__main__':
    app.run(debug=True)