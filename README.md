<h3 align="center"><b>Me Adota - Documentations</b></h3>
<p align="center">
    This is the general documentation for Me Adota website.
    <br>
    It runs on MKDocs.
    <br>
    <small><a href="">Versão em PT-BR aqui.</a></small>
</p>
</div>
<hr>

# Me-Adota

### Recommended requirements for application

You must have <code> Python 3.8</code> and <code> Pip 20.2</code> installed on your machine.

### Installing and Running

#### 1. Clone the repository

```
$ git clone https://github.com/Me-Adota/website
```

#### 2. Access the repository directory

```
$ cd website
```

#### 3. You must activate the venv bin, it will be activated using

```
$ virtualenv venv
```
```
$ source venv/bin/activate
```

#### 4. The requirements.txt file should list all Python libraries that your machine depend on, and they will be installed using

```
$ pip install -r requirements.txt
```

#### 5. Run

```
$ python manage.py runserver
```


It should be running on: http://127.0.0.1:8000

#### 5. Login in django Adminnistration Area

visit your admin page throught: http://localhost:8000/admin/

```
login: admin
email: admin@gmail.com
password: admin123 
``` 

#### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

