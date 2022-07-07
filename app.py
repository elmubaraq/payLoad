from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)
@app.route('/form',methods=['GET','POST'])
def home():
    print("welcome")
    if request.method=='POST':
        # Handle POST Request here

            
            payLoad= {          "uid": request.form.get('uid'),
                    "uidType": request.form.get('uidType'),
                    "title":request.form.get('title') ,
                    "firstName": request.form.get('firstName'),
                    "middleName": request.form.get('middleName'),
                    "lastName":request.form.get('lastName'),
                    "userName":request.form.get('usereName'),
                    "phone":request.form.get('phone'),
                    "emailId": request.form.get('emailId'),
                    "postalCode":request.form.get('postalCode'),
                    "city":request.form.get('city'),
                    "state":request.form.get('state'),
                    "lga":request.form.get('lga'),
                    "address":request.form.get('address'),
                    "countryOfResidence": request.form.get('countryOfResidence'),
                    "customerRiskRating": request.form.get('customerRiskRating'),
                    "tier": request.form.get('tier'),
                    "accountNumber": request.form.get('accountNumber'),
                    "taxIdentificationNumber": request.form.get('taxIdentificationNumber'),
                    "dateOfBirth": request.form.get(''),
                    "countryOfBirth": request.form.get('countryOfBirth'),
                    "stateOfOrigin": request.form.get('stateOfOrigin'),
                    "password": request.form.get('password'),
                    "remarks": request.form.get('remarks'),
                    "instCode": request.form.get('instCode'),
                    "referralCode": request.form.get('referralCode'),
                    "channel": request.form.get('channel')
                    }
            uid = None
            uidType =None
            


            print (request.form.get('uid'))


            
            
            
    return render_template('form.html')
    

    return render_template('form.html')       
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)