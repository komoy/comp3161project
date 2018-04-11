from . import db
from flask_login import UserMixin
from werkzug.security import generate_password_hash, check_password_hash
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.ext.declarative import declarative_base
from app import login_manager



class UserProfile(db.Model):
    """User Profile is a table of personal data assoc w/ a spec. user """
    
    __tablename__ = 'user_profile'
    
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),index=True)
    last_name = db.Column(db.String(80),index=True)
    gender=db.Column(db.String(10))
    username = db.Column(db.String(80),index=True, unique=True)
    meal_preference=db.Column(db.String(80))
    dob=db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    
    def __init__(self,first_name,last_name,gender,meal_preference):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.dob=dob
        self.username=username
        self.meal_preference=meal_preference
    
    @property 
    def password(self):
        
        
        """Prevents db admin or any other user from accessing the password"""
        
        raise AttributeError('Sorry but password cannot be accessed.')
        
    @password.setter
    def password(self,password):
        """ Setting the password to a hashed one"""
        
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self,password):
        """Checking if the hashed pasword matches actual password"""
        
        return check_password_hash(self.password_hash,password)
        
    def __repr__(self):
        return '<User %r>' % (self.username)

        

@login_manager.user_loader
def load_user(user_id):
    return UserProfile.query.get(int(user_id))
        
class HealthProfile(db.model): 
    """Health info is a table of health information assoc. w/ a spec user """
       
    __tablename__= 'healthinfo'
        
    member_weight=db.Column(db.Integer, nullable=False)
    member_healthid=db.Column(db.Integer, unique=True,nullable=False,primary_key=True)
    member_userid=db.Column(db.Integer, db.ForeignKey('UserProfile.user_id'),primary_key=True,unique=True)
    member_bloodtype=db.Column(db.String(80))
    member_height=db.Column(db.Integer)
    
    
    def __repr__(self):
        return '<User %r>' % (self.name)

    

class recipe(db.model):
    """Recipe is a table of all the recipe in the system"""
    
    __tablename__="recipe"
    
    recipe_fname=db.Column(db.String(80), nullable=False)
    recipe_lname=db.Column(db.String(80),nullable=False)
    recipe_userid=db.Column(db.Integer, db.ForeignKey('UserProfile.user_id'),primary_key=True,unique=True)
    recipe_dob=db.Column(db.DateTime, default=datetime.utcnow)
    recipe_gender=db.Column(db.String(10))
    recipe_preferences=db.Colunm(db.String(80), db.relationship('preferences'), backref='pref',lazy='dynamic')
    
    
    def __repr__(self):
        return '<Recipe for:{}>'.format(self.recipe_fname)

class instruction(db.model):
    
    """Instruction has the neccessary steps for the creation of the recipe"""
    
    __tablename__="instructions"
    
    instruct_measurement=db.Column(db.String(50), nullable=False)
    instruct_step=db.Column(db.String(50), nullable=False)
    instruct_recipeid=db.Column(db.Integer, unique=True,nullable=False, primary_key=True)
    instruct_instructionid=db.Column(db.Integer, nullable=False)
    
 
def __repr__(self):
    return '<Instruction for :{}>'.format(self.instruct_recipeid)

Base= declarative_base()

class meal(Base,db.model):
    """ Contains the information about the meals prepared"""
    
    __tablename__="meal"
    meal_calories=db.Column(db.Integer, nullable=False)
    meal=db.Column(db.Integer, nullable=False)
    meal_type=db.Column(db.String(80), nullable=False)
    meal_id=db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    meal_name=db.Column(db.String(80), nullable=False)
    meal_image=image_attachment('mealPicture')
    
    def __repr__(self):
        return '<Meal for :{}>'.format(self.meal_id)

    

class meal_planner(db.model):
    """ contains a daily, weekly schedule of meals"""
    
    __tablename__="meal_planner"
    meal_id=db.Column(db.Integer,db.ForeignKey('meal.meal_id'), nullable=False, unique=True, primary_key=True)
    plan_id=db.Column(db.Integer, nullable=False)
    day=db.Column(db.String(80), nullable=False,unique=True)
    week=db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<Meal Planner for: {}>'.format(self.plan_id)
        
    
class ingredient(db.mdel):
    """ contains all the ingredients"""
    
    __tablename__= "ingredient"
    i_id=db.Column(db.Integer,  unique=True,primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<Ingredient: {}>'.format(self.i_id)

class supermarket_list(db.model):
    
    """ grocery list of the ingredients for the prepared meals"""
    __tablename__="supermarket_list"
    quantity=db.Column(db.Integer,nullable=False)
    ingredient=(db.Column(db.String(80), nullable=False)
    list_id=(db.Column(db.Integer,nullable=False, unique=True, primary_key=True))
    
    def __repr__(self):
        return '<Supermarket List for: {}>'.format(self.list_id)
    
class contains(db.model):
    """ This is a relationship table"""
    
    __tablename__="contains"
    recipe_id=db.Column(db.Integer, nullable=False, db.ForeignKey('instruction.instruct_recipeid'))
    ingredients_id=db.Column(db.Integer, unique=True, nullable=False, db.ForeignKey('ingredient.i_id'))
    
    def __repr__(self):
        return '<Contains for: {}>'.format(self.recipe_id)

class add(db.model):
    """ Addition relationship table"""
    __tablename__="add"
    recipe_id=db.Column(db.Integer, nullable=False, db.ForeignKey('instruction.instruct_recipeid'))
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, db.ForeignKey('UserProfile.user_id'))

    def __repr__(self):
        return '<Addendum for: {}>'.format(self.recipe_id)


        
    
    
    


    
    
    
    
    