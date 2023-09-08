import PySimpleGUI as pg
import subprocess
import os
import re

#Theme
pg.theme('DarkGrey')

#Layout
layout = [
    [pg.Text("GUI pip", text_color='green')],
    [pg.Text("Enter The Name Of The Package\nAnd Chose The Option You Want")],
    [pg.InputText(do_not_clear=False, size=(28, 5))],
    [pg.Button("Install"), pg.Button("Uninstall")],
    [pg.Button("Show"), pg.Button("Freeze")],
    [pg.Button("Close")]
        
]

version_output = subprocess.check_output("pip --version", shell=True)
v = re.findall(r'(\d\d.\d)', str(version_output))


seclayout = [
    [pg.Text("Your Pip Version:"), pg.Text(v)],
    [pg.Button("Package Lists")]

]

layouts = [
    [pg.Col(layout), pg.Col(seclayout)]
]


#Window
window = pg.Window("GUI pip", layouts)

#Events
while True:
    event, values = window.read()
    if event == 'Close' or event == pg.WIN_CLOSED:
        window.close()
        break

##########################################################################
#Dirty Code

    #install button events
    if event == 'Install':
        if values[0] == '':
            pg.Print('Nothing Has Enternd In Input Box')
        else:
            inp = subprocess.getoutput('pip install' +' '+ values[0])
            warning_out1 = inp[0:19]
            succes_out1 = inp[0:11]
            error_out1 = inp[0:5]
            
            if warning_out1 == 'Requirement already':
                pg.Print(values[0]+ 'is already installed')
                
            if succes_out1 == 'Collecting ':
                pg.Print(values[0]+ ' succesfully installed')
                
            if error_out1 == 'ERROR':
                pg.Print('Error\nthe name of package is wrong')
            


    #uninstall button events          
    if event == 'Uninstall':
        if values[0] == '':
            pg.Print('nothing has enternd in input box')
        else:
            inp = subprocess.getoutput('pip uninstall' +' '+ values[0]+ ' -y')
            warning_out2 = inp[0:7]
            succes_out2 = inp[45:58]
            error_out2 = inp[0:5]
            
            if warning_out2 == 'WARNING':
                pg.Print(values[0]+ ' not installed')
                
            if succes_out2 == 'Uninstalling ':
                pg.Print(values[0]+ ' uninstalled succesfully')
                
            if error_out2 == 'ERROR':
                pg.Print('Error\nthe name of package is wrong')
            



        
    #show button events
    if event == 'Show':
        if values[0] == '':
            pg.Print('Nothing Has Enternd In Input Box')
        else: 
            for i in subprocess.getstatusoutput('pip show'+' '+values[0]):
                pg.Print(i)
            
            
                
    #freeze button events
    if event == 'Freeze':
        for i in subprocess.getstatusoutput('pip freeze\n'):
            pg.Print(i)

      
    #package list button events
    if event == 'Package Lists':
        for i in subprocess.getstatusoutput('pip list'):
            pg.Print(i)


###################################################################################
