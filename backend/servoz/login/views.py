from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method == 'POST':
        m=sql.connect(host='localhost',user='root',passwd='root',database='myapp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='email':
                em=value
            if key=='password':
                pwd=value
        c="select * from user_credentials where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login_page.html')
        else:
            return render(request,'home.html')
    return render(request,'login_page.html')
    


