from logging import info
from os import name
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('select.html')

@app.route('/select_index',methods=['POST','GET'])
def select():
    select=request.form['task']
    if select == "encrypt":
        return render_template('encrypt.html')
    else:
        return render_template('decrypt.html')


@app.route('/encrypt_index',methods=['POST','GET'])
def encrypt():
    a=request.form['pass']
    
    l = []                          # To store the each encrypted chracter
    const=len(a)                    # Add/Sub from ascii value of each character 
    for i in range(len(a)):
        if i==0:
            ascii = ord(a[i])+const
            if ascii > 127:
                ascii = (ascii - 127) + 32     # 127: end of ascii | 33: beginning of ascii
            l.append(chr(ascii))
        
        elif (i%2)!=0:
            ascii = ord(a[i])-const
            if ascii < 33:
                ascii = 128 - (33 - ascii)     # 127: end of ascii | 33: beginning of ascii
            l.append(chr(ascii))
            
        else:
            ascii = ord(a[i])+const
            if ascii > 127:
                ascii = ascii - 127 + 32     # 127: end of ascii | 32: beginning of ascii
            l.append(chr(ascii))

        const-=1

    e ="".join(l)      
    return render_template('output.html',key = e)

@app.route('/decrypt_index',methods=['POST','GET'])
def decrypt():
    e = request.form['pass']
    l = []
    const=len(e)
    for i in range(len(e)):
        if i==0:
            ascii = ord(e[i])-const
            if ascii < 33:
                ascii = 128 - (33 - ascii)
            l.append(chr(ascii))
        
        elif (i%2)!=0:
            ascii = ord(e[i])+const
            if ascii > 127:
                ascii = (ascii - 127) + 32
            l.append(chr(ascii))
            
        else:
            ascii = ord(e[i])-const
            if ascii < 33:
                ascii = 128 - (33 - ascii)
            l.append(chr(ascii))

        const-=1

    d = "".join(l)
    return render_template('output.html',key = d)

if __name__ == '__main__':
    app.run(debug=True)