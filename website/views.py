from flask import Blueprint, render_template, session, url_for, session, redirect, request, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if request.method == 'POST':
        # LIGHT 1 ( ROOM 1 )
        if request.form.get('light1_r1_on') == '1':
            commitChanges(1, 0)
        elif request.form.get('light1_r1_off') == '0':
            commitChanges(0, 0)
        
        # LIGHT 2 ( ROOM 1 )
        elif request.form.get('light2_r1_on') == '1':
            commitChanges(1, 1)
        elif request.form.get('light2_r1_off') == '0':
            commitChanges(0, 1)

        # LIGHT 3 ( ROOM 1 )
        elif request.form.get('light3_r1_on') == '1':
            commitChanges(1, 2)
        elif request.form.get('light3_r1_off') == '0':
            commitChanges(0, 2)

        # LIGHT 4 ( ROOM 1 )
        elif request.form.get('light4_r1_on') == '1':
            commitChanges(1, 3)
        elif request.form.get('light4_r1_off') == '0':
            commitChanges(0, 3)

        # Fan 1 ( ROOM 1 )
        elif request.form.get('fan1_r1_on') == '1':
            commitChanges(1, 4)
        elif request.form.get('fan1_r1_off') == '0':
            commitChanges(0, 4)

        # Fan 2 ( ROOM 1 )
        elif request.form.get('fan2_r1_on') == '1':
            commitChanges(1, 5)
        elif request.form.get('fan2_r1_off') == '0':
            commitChanges(0, 5)

        # Light 1 ( ROOM 2 )
        elif request.form.get('light1_r2_on') == '1':
            commitChanges(1, 6)
        elif request.form.get('light1_r2_off') == '0':
            commitChanges(0, 6)

        # Light 2 ( ROOM 2 )
        elif request.form.get('light2_r2_on') == '1':
            commitChanges(1, 7)
        elif request.form.get('light2_r2_off') == '0':
            commitChanges(0, 7)

        # Light 3 ( ROOM 2 )
        elif request.form.get('light3_r2_on') == '1':
            commitChanges(1, 8)
        elif request.form.get('light3_r2_off') == '0':
            commitChanges(0, 8)
        
        # Fan 1 ( ROOM 2 )
        elif request.form.get('fan1_r2_on') == '1':
            commitChanges(1, 9)
        elif request.form.get('fan1_r2_off') == '0':
            commitChanges(0, 9)
        
        # Fan 2 ( ROOM 2 )
        elif request.form.get('fan2_r2_on') == '1':
            commitChanges(1, 10)
        elif request.form.get('fan2_r2_off') == '0':
            commitChanges(0, 10)

        else:
            pass

    return render_template('dashboard.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

'''
def openFile():
    file = open('website/static/states.txt', 'w')
    state = file.readline()
    state_list = state.split(',')'''

def commitChanges(val, number):
    #global state_list, state
    file = open('website/static/states.txt', 'r+')
    state = file.readline()
    state_list = state.split(',')
    state_list[number] = str(val)
    state = state_list[0]+','+state_list[1]+','+state_list[2]+','+state_list[3]+','+state_list[4]+','+state_list[5]+','+state_list[6]+','+state_list[7]+','+state_list[8]+','+state_list[9]+','+state_list[10]+','
    print("After loop",state)
    state = state.rstrip(state[-1])
    print(state)
    file.truncate(0)
    file.seek(0)
    file.write(state)
    file.close()
    print("PRESSED"+str(val))
    flash("Value updated "+str(val), category='success')

