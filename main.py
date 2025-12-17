#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_telegram = request.form.get('button_telegram')
    button_unity = request.form.get('button_unity')
    button_web = request.form.get('button_web')
    return render_template('index.html', button_python=button_python, button_telegram=button_telegram,
                           button_unity=button_unity, button_web=button_web)


if __name__ == "__main__":
    app.run(debug=True)