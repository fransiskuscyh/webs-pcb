<h1>"Website Detection PCB"</h1>

<p>view detection pcb pass or reject on website</p>



## Instalasi
```bash
create database using "raspberry.sql"
git clone https://github.com/fransiskuscyh/webs-pcb.git
cd webs-pcb
py -m venv .venv #create virtual environment
pip install django, mysql-connector
py manage.py runserver #for run server website
