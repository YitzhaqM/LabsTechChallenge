from flask import Flask, render_template

app = Flask(__name__)


@app.route('/ytm2102', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/index.html', methods=['GET', 'POST'])
def in1():
    return render_template('index.html')
@app.route('/index2.html', methods=['GET', 'POST'])
def in2():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
