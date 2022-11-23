# DjangoAPP

Clone the repo 

Templates/Frameworks used:
Django4,Boostrap5,SQL

Install virtual env:  alexceban@Alexs-MacBook-Pro DjangoAPP % 

    $ python3 -m venv djangoenv  

Start virtual env:  alexceban@Alexs-MacBook-Pro DjangoAPP % 

    $ source .venv/bin/activate

Install requirement.txt file: (.venv) alexceban@Alexs-MacBook-Pro DjangoAPP % 

    $pip3 install -r requirements.txt

Change directory to src: (.venv) alexceban@Alexs-MacBook-Pro DjangoAPP % 

    $ cd src

Initialize databases: (.venv) alexceban@Alexs-MacBook-Pro src% 

    $ python3 manage.py migrate

Run server: (.venv) alexceban@Alexs-MacBook-Pro src% 

    $ python3 manage.py runserver

(if admin page is missing the css styling) : (.venv) alexceban@Alexs-MacBook-Pro src % 

    $ python3 manage.py collectstatic

Create superuser admin to manage the underlying databases and access the admin page

    $ python3 manage.py createsuperuser
<p>
Enter your desired username and press enter.<br>

Username: admin<br>
You will then be prompted for your desired email address:<br>

Email address: admin@example.com<br>
The final step is to enter your password. You will be asked to enter your password twice, the second time as <br>a confirmation of the first.<br>

Password: **********<br>
Password (again): *********<br>
Superuser created successfully.<br>
    
Run server: (.venv) alexceban@Alexs-MacBook-Pro src% 

    $ python3 manage.py runserver    
    
</p>

<p>Navigate to the localhost admin page: http://localhost:8000/admin/</p>
<p>Navigate to the localhost register page to begin: http://localhost:8000/register</p>

<p> sent_emails folder will contain the request to the reset-password </p>

When submitting a contact form: 

<p>[22/Nov/2022 23:19:23] "GET /contact/ HTTP/1.1" 200 1261 <br>
Content-Type: text/plain; charset="utf-8"<br>
MIME-Version: 1.0<br>
Content-Transfer-Encoding: 7bit<br>
Subject: Website Inquiry<br>
From: admin@example.com<br>
To: admin@example.com<br>
Date: Tue, 22 Nov 2022 23:19:49 -0000<br>
Message-ID: <166915918905.6793.2195921917549709838@Alexs-MacBook-Pro.local><br>

Miron<br>
Ruben<br>
delta@gmail.com<br>
Message for the company<br>
</p>

<p>Additional features, I track user session in a separate table called User visits</p>
  
<p>SQL QUERY ANSWER<br>

select user_id, <br>
 activity_id,<br>
 count(occurrence) as amount,<br>
 min(occurrence) as first_occurance,<br>
 max(occurrence) as last_occurance <br>
from user_activity join user on user_activity.user_id = user.id<br>
join activity on user_activity WHERE user_activity.activity_id = activity.id<br>
group by user_id, activity_id<br>
</p>

<p> Add Functionality: a user can register, log in, log out, edit his information like first name, last name, email address. User can reset his password. User can contact the company via a contact form and using his email.</p>




*Problems to be fixed, 
cache management (I am still able to go back after logout) is not implementd, 
testing is not implemented, 
fully imnplementing the email communication feature.*


