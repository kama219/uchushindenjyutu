from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birth_year = request.form['year']
        birth_month = request.form['month']
        birth_day = request.form['day']
        # 運命石計算ロジックをここに追加
        return f"あなたの運命石は..."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

