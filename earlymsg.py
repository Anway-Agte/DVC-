  msg = Message("test message", recipients = [entered_user])
            msg.body = "This is a trial message ! Hope it reaches you "
            token = random.randint(11111,99999) 
            link = url_for("reset" ,token = token , _external = True) 
            print(link)
            
            msg.html = "<h1><a href =" + link  +   ">Click Here to reset password</a></h1>"
            mail.send(msg) 
            mongo.db.users.update_one({"email" : entered_user},{"$set": {"token": token }}) 