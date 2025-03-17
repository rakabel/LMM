from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    portfolio = [
        {'title': 'Survei Lapangan Pemilu 2019', 'image': 'static/img/pemilu2019.jpg', 'description': 'Survei untuk memetakan preferensi politik masyarakat menjelang Pemilu 2019.'},
        {'title': 'Survei Lapangan Pemilu 2024', 'image': 'static/img/pemilu2024.jpg', 'description': 'Survei terkini dalam rangka Pemilu 2024 untuk memahami tren dan dinamika politik.'},
        {'title': 'Survei Pemilihan Gubernur DKI Jakarta 2024', 'image': 'static/img/pilgubdki2024.jpg', 'description': 'Survei terkait calon gubernur dan preferensi publik di DKI Jakarta tahun 2024.'}
    ]
    return render_template('index.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True)

