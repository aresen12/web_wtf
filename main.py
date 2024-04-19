from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def mass():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>Миссия Колонизация Марса</h1>
</head>
<body>

</body>
</html>'''


@app.route('/index')
def dev():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>И на Марсе будут яблони цвести!</h1>
</head>
<body>

</body>
</html>'''


@app.route('/promotion')
def rek():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>Человечество вырастает из детства.</h1>

<h1>Человечеству мала одна планета.</h1>

<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>

<h1>И начнем с Марса!</h1>

<h1>Присоединяйся!</h1>
</head>
<body>

</body>
</html>'''


@app.route('/image_mars')
def mars():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
    <br>
    Вот она какая, красная планета
</head>
<body>
</body>
</html>'''


@app.route("/promotion_image")
def promotion_image():
    file = open("promotion_image.html", encoding='utf-8', mode='r')
    data = file.read()
    file.close()
    return data


@app.route('/carousel')
def peizag():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
</head>
<body>
<h1 style="margin-right:45vw;">пейзажи марса</h1>
<div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false" data-bs-interval="false" style="width:50vw;">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="static/img/mars1.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="static/img/mars2.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="static/img/mars3.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
</body>
</html>'''


@app.route('/galery', methods=['GET', 'POST'])
def peizag2():
    file = open('config.txt')
    data = file.readlines()
    file.close()
    if request.method == "POST":
        file2 = open(f"static/img/mars{len(data) + 2}.jpg", mode="wb")
        f = request.files['file']
        file2.write(f.read())
        file2.close()
        a = len(data)
        data.append(f"mars{a + 2}.jpg")
        file = open('config.txt', mode="w")
        for _ in data:
            file.write(_)
        file.close()
    return render_template("assas.html", data=data)


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
