from flask import render_template,request,redirect,url_for,jsonify
from flask_login import login_user, logout_user,current_user,login_required
from models import User


def register_routes(app,db):

    @app.before_request
    def log_request():
        app.logger.info(
            f"IP={request.remote_addr} "
            f"METHOD={request.method} "
            f"PATH={request.path}"
        )

    @app.route('/')
    def index():
      return render_template('index.html')
    
    @app.route('/signup',methods=['GET','POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            #hashed_password = bcrypt.generate_password_hash(password)
            
            user = User(username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/login',methods=['GET','POST'])
    def login():
        app.logger.info(
    f"EVENT=LOGIN_ATTEMPT | IP={request.remote_addr}"
)

        ip = request.remote_addr # get user IP 

        # check if delay is required 
        
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            app.logger.info(
            f"LOGIN ATTEMPT | IP={request.remote_addr} | USER={username}"
        )
            password = request.form.get('password')


            user = User.query.filter(User.username == username).first()

            if user is None: 
                app.logger.warning(f"EVENT=LOGIN_FAIL | IP={ip}")


                return "No user by this name exists"

            if user.password == password:
                app.logger.info(f"EVENT=LOGIN_SUCCESS | IP={request.remote_addr}")

                login_user(user)  
                return redirect(url_for('transfer'))
            else:
                app.logger.warning(
    f"EVENT=LOGIN_FAIL | IP={request.remote_addr}"
)

                return 'Failed'
    

    @app.route('/transfer',methods=['GET'])
    def transfer():
        username = request.form.get('username')
        #return f'Your username is {username}'
        return render_template('dashboard.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))