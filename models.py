from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

class Post(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
<<<<<<< HEAD
    author = db.ReferenceProperty(required = True)
=======
    # TODO - we need an author field here; it should be required
>>>>>>> 6b36ae40ec70b99288934ddd2228d7ec2fccc300
