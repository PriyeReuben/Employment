import PySimpleGUI as sg
import pandas as pd
import openpyxl as pxl
import os
import csv

sg.theme('DarkTeal9')
excel_file = r'N:\Data Analysis\test_company_entry.xlsx'

df = pd.read_excel(excel_file)


company_layout = [
    [sg.Text('Company ID:', size=(15,1)), sg.InputText(key='company_id')],
    [sg.Text('Name:', size=(15,1)), sg.InputText(key='company_name')],
    [sg.Text('Type:', size=(15,1)), sg.InputText(key='company_type')],
    [sg.Text('Location:', size=(15,1)), sg.InputText(key='company_location')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]

]


window = sg.Window("Employment Entry", company_layout, element_justification='c')

def clear_input():
    for key in values:
        window[key]('')

def populate_entry():
    pass

def check_previous():
    current_company_id = list(df['company_id'])
    print("Current Company ID", current_company_id)
    current_company_name = list(df['company_name'])
    print("Current Company Name:", current_company_name)

    print('Entry company ID:', entry_df['company_id'][0])
    print('Entry company Name:', entry_df['company_name'][0])

    if entry_df['company_id'][0] in current_company_id:
        sg.popup("This company ID already exists!  Next entry should be {}".format(str(int(current_company_id[-1])+1)))
        return False
    elif entry_df['company_name'][0] in current_company_name:
        sg.popup("This company name already exists!")
        return False
    else:
        return True
def check_valid():

    #check that company id is not blank
    if entry_df['company_id'][0].strip() == "":
        sg.popup("You are missing a company ID")
        return False
    else:
        pass

    #check that company ID is an integer
    try:
        int_comp_id = int(entry_df['company_id'][0].strip())
        if not isinstance(int_comp_id, int):
            sg.popup("Company ID must be an integer")
            return False
        else:
            pass
    except:
        sg.popup("Company ID must be an integer")
        return False

    # check that company name is not blank
    if entry_df['company_name'][0].strip() == "":
        sg.popup("You are missing a company name")
        return False
    else:
        pass

    return True

while True:
    event, values = window.read()
    entry_df = pd.DataFrame([values])
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit' and check_valid() == True and check_previous() == True:
        df = pd.concat([df, entry_df], ignore_index=True)
        df.to_excel(excel_file, index=False)
        clear_input()
        sg.popup('Data Saved?')
window.close()