from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
a=''
em=''
pwd=''
id=0
# Create your views here.
def signaction(request):
    global fn,ln,a,em,pwd,id
    if request.method == 'POST':
        m=sql.connect(host='localhost',user='root',passwd='root',database='myapp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='first_name':
                fn=value
            if key=='last_name':
                ln=value
            if key=='age':
                a=value
            if key=='email':
                em=value
            if key=='password':
                pwd=value
        c="insert into user_credentials values('{}','{}','{}','{}','{}','{}')".format(fn,ln,a,em,pwd,id)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')
    




    