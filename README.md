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


#home
![Alt Text](https://github.com/fransiskuscyh/webs-pcb/blob/main/img/home.png)

#pass
![Alt Text](https://github.com/fransiskuscyh/webs-pcb/blob/main/img/pass.png)

#reject
![Alt Text](https://github.com/fransiskuscyh/webs-pcb/blob/main/img/reject.png)
