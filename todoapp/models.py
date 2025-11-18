from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    
    def __init__(self, username, password):
        # super().__init__()
        self.username = username
        self.password = password


    def __repr__(self):
        return f"<User: {self.username}>"


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    
    def __init__(self, user, title, description=None, completed=False, created_at=None):
        # super().__init__()
        self.user = user
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at


    def __repr__(self):
        return f"<TodoItem: {self.title} - Completed: {self.completed}>"