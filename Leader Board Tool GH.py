##  TZed9
##  V0.02 24/02/2020
##
##  Changelog:
##	Pyinstaller --onedir
##	Message removed : Not Found! 
##	Message added: Searching...

import numpy as np
import pandas as pd
import PySimpleGUI as sg
import datetime as dt
import time
import webbrowser
import MySQLdb
import sys
import time
import datetime as dt

HOST = '****' 
ADR = '****'
USER = '****'
PW = '****'
driver_name = ''
lap_time = ''
url = 'http://www.radicalsimulation.com/'

connection = MySQLdb.connect(host=HOST, user=USER, passwd=PW, database=ADR)
cursor =connection.cursor()

sg.change_look_and_feel('Topanga')

now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


layout = [	[sg.Text('Press Web to open the leader board in a browser window')],
			[sg.Text('To add a new Driver Name and Lap Time,')],
			[sg.Text('fill in the first two fields below and press Update')],
			[sg.Text('\n')],
			[sg.Text('Driver Name: ',size=(12,1)),sg.InputText(key='__driver_name__')],
			[sg.Text('Lap Time    : ',size=(12,1)),sg.InputText(key='__lap_time__')],
			[sg.Button('Update',size=(16,2)),sg.Button('Web', size=(16,2)),sg.Button('Reset', size=(16,2))],
			[sg.Text('\n')],
			[sg.Text('Delete driver: ',size=(12,1)),sg.InputText(key='__driver_search__')],
			[sg.Button('Search',size=(16,2)),sg.Button('Delete',size=(16,2)),sg.Button('Exit',size=(16,2))],
			[sg.Text('Messages:  ',size=(50,1))],
			[sg.Text(key='__MESSAGES__', size=(30,2)),sg.Image(r'C:\\PP\\EVRG.png')]
			]

window = sg.Window('Leaderboard_Genpact_2', layout)

def execute_get_board():
		cursor.execute("SELECT table_id, subject, custom_stat_1 FROM wp_da_lt_table_item WHERE table_id = %(board_id)s ORDER BY custom_stat_1", {'board_id':23})
		myresult = cursor.fetchall()
		#print('\n\n')
		#print(myresult[:][1])
		return myresult

def execute_sql_commit(sql_commit, val_commit):
	cursor.execute(sql_commit, val_commit)
	connection.commit()

def execute_sql_delete(driver_name_delete):
	cursor.execute("DELETE FROM wp_da_lt_table_item WHERE subject=%(sub)s",{'sub':driver_name_delete})
	connection.commit()

def reset_btn():
	window['__driver_name__']('')
	window['__lap_time__']('')
	window['__driver_search__']('')
	
def update_btn():
	sql_commit = "INSERT INTO wp_da_lt_table_item (table_id, subject, custom_stat_1) VALUES (%s, %s, %s)"
	id=23 		# genpact_2
	val_commit = (id, driver_name, lap_time)	
	execute_sql_commit(sql_commit, val_commit)
	reset_btn()
	window['__MESSAGES__']('Added new driver and time to Leaderboard')

def web_page_btn():
	webbrowser.open(url+'genpact_2', new=2)	

def search_btn():
	window['__MESSAGES__']('Searching...')
	global t1
	global found_flag
	t1 = window['__driver_search__'].get()
	found_flag = False
	#print(t1)
	response = execute_get_board()

	for x in response:
		if x[1] == t1:
			#print(x[1], x[2])
			window['__driver_name__'](x[1])
			window['__lap_time__'](x[2])
			window['__MESSAGES__']('Found!')
			found_flag = True
		
def delete_btn():
	try:
		if found_flag:
			button = sg.popup_yes_no('Are you sure you want to delete: '+t1+' ?')
			if button == 'Yes':
				execute_sql_delete(t1)
				reset_btn()
				window['__MESSAGES__']('Deleted driver name and time')
			elif button == 'No':
				pass
			pass
		pass
	except:
		pass
	
'''
def update_data():
		window['_OUTPUT1_'].update(results)
'''
now = time.time()
if now < 1588291200:

	while True:  
		event, values = window.read(timeout=3000)       
		window['__MESSAGES__']('')
		if event is None or event == 'Exit':
			button_2 = sg.popup_yes_no('Are you sure?')
			if button_2 =='Yes':
				break
			elif button_2 == 'No':
				pass

		if event == 'Update':
			driver_name = window['__driver_name__'].get()
			lap_time = window['__lap_time__'].get()
			if driver_name != '':
				if lap_time != '':
					update_btn()
			
		if event == 'Reset':
			reset_btn()
			
		if event == 'Web':
			web_page_btn()
			
		if event == 'Search':
			search_btn()
		
		if event == 'Delete':
			delete_btn()
		
		#results = execute_get_board()
		#update_data()
     	

window.close()
