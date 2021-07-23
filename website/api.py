from flask import Blueprint, render_template, request, flash, jsonify

api = Blueprint('api', __name__)

api_key = "shahrukh123"
api_link = '/api_key='+api_key

@api.route(api_link)
def api_k():
    file = open('website/static/states.txt')
    state = file.readline()
    state_list = state.split(',')
    print('api=',state_list)
    file.close()

    room1 = {
        # Room 1
        'light1_r1' : state_list[0],
        'light2_r1' : state_list[1],
        'light3_r1' : state_list[2],
        'light4_r1' : state_list[3],
        'fan1_r1' : state_list[4],
        'fan2_r1' : state_list[5]
    }

    room2 = {
        # Room 2
        'light1_r2' : state_list[6],
        'light2_r2' : state_list[7],
        'light3_r2' : state_list[8],
        'fan1_r2' : state_list[9],
        'fan2_r2' : state_list[10]
    }

    result = [room1, room2]

    return jsonify(result)
