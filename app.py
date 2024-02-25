from flask import Flask,render_template,request,redirect,session
import random
import sqlite3
import datetime
from datetime import datetime,timedelta
app= Flask(__name__)
app.secret_key="teja"

@app.route('/')
def home():
    customerid=str(random.randint(1000000,9999999))
    return render_template('customerRegistration.html',customerid=customerid)

@app.route('/submit',methods=['POST',"GET"])
def submit():
    if request.method=="GET":
        return render_template("customerRegistration.html")

    if request.method=="POST":
        customerId=request.form['customerId']
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        address=request.form['address']
        contact=request.form['contact']
        nomineename=request.form['nomineename']
        relation=request.form['relation']
        session['con']=contact
        session['nomi']=nomineename
        session['rel']=relation
        conn=sqlite3.connect('prashSql12.db')
        cursor=conn.cursor()

        cursor.execute('''create table IF NOT EXISTS customer(customerId integer primary key, name varchar, email varchar,password varchar,address varchar,contact varchar,nomineename varchar,relation varchar);''')
        conn.commit()
        cursor.execute('insert into customer (customerId,name,email,password,address,contact,nomineename,relation) values (?,?,?,?,?,?,?,?)',(customerId,name,email,password,address,contact,nomineename,relation))
        conn.commit()
        conn.close()
        return redirect('succregistration')
    

@app.route('/succregistration')
def succregistration():
    return render_template('sucessRegis.html')

@app.route('/login')
def login():
    return render_template('customerLoginScreen.html')

@app.route('/succlogin',methods=['POST',"GET"])
def succlogin():
    if request.method=="GET":
        return render_template("customerLoginScreen.html")
    
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        conn=sqlite3.connect('prashSql12.db')
        cursor=conn.cursor()
        cursor.execute('select customerId,password,name from customer where customerId= ? And password=? ',(username,password,))
        var=cursor.fetchone()
        if var is not None:
            session['name']=var[2]
            session['cId']=var[0]
            session.permanent=True
        conn.commit()
        conn.close()
        if var is not None:
            name=session.get('name')
            return render_template('succLoginScreen.html',name=name)
        else:
            return redirect('login')
@app.route('/insurence')
def insurence():
    name=session.get('name')
    return render_template('succLoginScreen.html',name=name)


@app.route('/choosepolicy',methods=['POST',"GET"])
def choosepolicy():
    if request.method=="GET":
        return render_template("choosePolicy.html")
    
    if request.method=="POST":
        policyNo=str(random.randint(100000,999999))
        commenceDate=datetime.now().strftime("%d-%m-%Y")
        status="Active"
        type=request.form['title1']
        title=request.form['title2']
        premiumAmount=request.form['premAmount']
        nextDue=datetime.now()+timedelta(days=365)
        nextDueDate=nextDue.strftime("%d-%m-%Y")
        sumAssured=request.form['sumAssured']
        term=request.form['policyTerm']
        nominee="Yes"
        c=session.get('cId')
        contact=session.get('con')
        nomineename=session.get('nomi')
        relation=session.get('rel')
        
        conn=sqlite3.connect("prashSql12.db")
        cursor=conn.cursor()
        cursor.execute('''create table if not exists policyTable(CustomerId integer,policyNo integer,commenceDate varchar,status varchar,type varchar,title varchar,premiumAmount varchar,nextDueDate varchar,sumAssured integer,term varchar,nominee varchar, contact varchar, nomineename varchar, relation varchar)''')
        conn.commit()
        cursor.execute('insert into policyTable (CustomerId,policyNo,commenceDate,status,type,title ,premiumAmount ,nextDueDate ,sumAssured ,term ,nominee,contact,nomineename,relation) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(c,policyNo,commenceDate,status,type,title ,premiumAmount ,nextDueDate ,sumAssured ,term ,nominee,contact,nomineename,relation))
        conn.commit()
        conn.close()
        return redirect('insurence')
@app.route('/v1')
def v1():
    return render_template('viewCustomerPolicies.html')

@app.route('/viewpolicy',methods=['POST',"GET"])
def viewpolicy():
    if request.method=="GET":
        custId=session['cId']
        conn=sqlite3.connect("prashSql12.db")
        cursor=conn.cursor()
        cursor.execute('select * from policyTable where CustomerId= ? ',(custId,))
        customerPolicies=cursor.fetchall()
        conn.commit()
        conn.close()
        return render_template('viewCustomerPolicies.html',customerPolicies=customerPolicies)
    
    if request.method=="POST":
        policyId=request.form["custId"]
        custId=session['cId']
        conn=sqlite3.connect("prashSql12.db")
        cursor=conn.cursor()
        cursor.execute('select * from policyTable where policyNo= ? and CustomerId=? ',(policyId,custId))
        customerPolicies=cursor.fetchall()
        conn.commit()
        conn.close()
        if customerPolicies is not None:
            return render_template('viewCustomerPolicies.html',customerPolicies=customerPolicies)
        else:
            return render_template('viewCustomerPolicies.html')

@app.route('/v2')
def v2():
    name=session.get('name')
    return render_template('deletepolicy.html',name=name)

@app.route('/deletepolicy',methods=['POST',"GET"])
def deletepolicy():
    if request.method=="POST":
        custId=session['cId']
        policyId=request.form["policyid"]
        password=request.form["password"]
        conn=sqlite3.connect("prashSql12.db")
        cursor=conn.cursor()
        cursor.execute('select * from policyTable join customer on policyTable.CustomerId=customer.customerId where policyTable.policyNo= ? and customer.password= ? and customer.CustomerId= ?',(policyId,password,custId) )
        customerPoliciy=cursor.fetchone()
        conn.commit()
        conn.close()
        if customerPoliciy is not None:
            custId=session['cId']
            conn=sqlite3.connect("prashSql12.db")
            cursor=conn.cursor()
            cursor.execute('Delete from policyTable where policyNo= ? and CustomerId=?',(policyId,custId))
            conn.commit()
            conn.close()
            return redirect('insurence')
        else:
            return redirect('v2')

@app.route('/v3')
def v3():
    name=session.get('name')
    return render_template('updatepolicy.html',name=name)

@app.route('/updatepolicy',methods=['POST',"GET"])
def updatepolicy():
    if request.method=="POST":
        custId=session['cId']
        policy_id=request.form["policy_id"]
        nomineename=request.form["nomineename"]
        relation=request.form["relation"]
        contact=request.form["mobile"]
        conn=sqlite3.connect("prashSql12.db")
        cursor=conn.cursor()
        cursor.execute('update policyTable set nomineename=? , relation=?, contact=? where  policyNo= ? and CustomerId=?',(nomineename,relation,contact,policy_id,custId) )
        conn.commit()
        conn.close()
        return redirect('insurence')
    else:
        return redirect('v3')
app.run(debug=True)