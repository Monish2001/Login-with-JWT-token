# Login Mechanism with JWT token in Flask

##### Python Version : Python3

##### Packages Used : 

1. flask
2. pymongo
3. jwt

##### Installing Packages :

* pip install Flask
* pip install pymongo
* pip install PyJWT
 
##### How to Execute :

* Download and Run the "app.py" file, using the command "python3 app.py".

* Go to Postman API.

* For **signup** enter the details in form-data which is in Body section.   
**Ex : http://127.0.0.1:5000/api/v1/auth/signup   
    name     : monish  
    email    : monish@gmail.com    
    mobile   : 9999999999  
    password : hello**  
    
* For login enter the details in form-data which is in Body section and it will return a JWT token.  
**Ex : http://127.0.0.1:5000/api/v1/auth/login     
    name     : monish     
    password : hello**   
 
 * For retrieving all the user details enter the token in the header section and it will return all the users.    
 Ex : http://127.0.0.1:5000/api/v1/users        
    x-access-token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoibW9uaXNoIn0.s9Cd1lLFsyy23_zAo6pNk71Cmxkm1c7UXQxfgGx_3ds  
    
 * For retrieving a particular user detail with user user_id, enter the user_id in url and token in header and it will return the particular user detail.   
 Ex : http://127.0.0.1:5000/api/v1/users/5f0f63661684a2c4d950622c      
 x-access-token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoibW9uaXNoIn0.s9Cd1lLFsyy23_zAo6pNk71Cmxkm1c7UXQxfgGx_3ds 
 
 
 
 
 

