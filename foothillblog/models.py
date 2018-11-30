from datetime import datetime
from foothillblog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    tweetsPosted = db.relationship('RealTweets', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"


class PostSentiments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyWord = db.Column(db.String(50), nullable=False)
    polarityPercentage = db.Column(db.Float, nullable=False)
    positivePercentage = db.Column(db.Float, nullable=False)
    wpositivePercentage = db.Column(db.Float, nullable=False)
    spositivePercentage = db.Column(db.Float, nullable=False)
    negativePercentage = db.Column(db.Float, nullable=False)
    wnegativePercentage = db.Column(db.Float, nullable=False)
    snegativePercentage = db.Column(db.Float, nullable=False)
    neutralPercentage = db.Column(db.Float, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"PostSentiments('{self.keyword}',\
                                '{self.polarityPercentage}',\
                                '{self.positivePercentage}',\
                                '{self.wpositivePercentage}',\
                                '{self.spositivePercentage}',\
                                '{self.negativePercentage}',\
                                '{self.wnegativePercentage}',\
                                '{self.snegativePercentage}')"


class RealTweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    keyWord = db.Column(db.String(20), nullable=False)
    tweetPost = db.Column(db.Text, nullable=False)
    polarity = db.Column(db.Float, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.keyWord}', '{self.tweetPost}',\
                      '{self.polarity}', '{self.date_posted}')"
