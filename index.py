import PySimpleGUI as pg
from functions.actions import *

label1 = pg.Text("Select file to compress: ")
input1 = pg.Input()
choose_button1 = pg.FilesBrowse("Choose", key='files')

label2 = pg.Text("Select destination folder:")
input2 = pg.Input()
choose_button2 = pg.FolderBrowse("Choose", key='compress_folder')
compress_button = pg.Button("Compress")
output_label1 = pg.Text(key="compress_output", text_color='green')

compress_tab = [[label1, input1, choose_button1],
                [label2, input2, choose_button2],
                [compress_button, output_label1]]

label3 = pg.Text("Select file to compress: ")
input3 = pg.Input()
choose_button3 = pg.FileBrowse("Choose", key='archive')

label4 = pg.Text("Select destination folder:")
input4 = pg.Input()
choose_button4 = pg.FolderBrowse("Choose", key='extract_folder')

extract_button = pg.Button("Extract")
output_label2 = pg.Text(key="extract_output", text_color='green')

extract_tab = [[label3, input3, choose_button3],
               [label4, input4, choose_button4],
               [extract_button, output_label2]]

layout = [[pg.TabGroup([[pg.Tab('Compress Files', compress_tab, key='compress'),
                        pg.Tab('Extract Files', extract_tab, key='extract')]],
                       tab_location='centertop',
                       # selected_title_color='Green',
                       tab_background_color='Gray',
                       title_color='White',
                       selected_background_color='White',
                       selected_title_color='Black',
                       border_width=5)]]

window = pg.Window("File Compressor/Extractor", layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    # print(event, values)
    if event == "Compress":
        filepath = values["files"].split(';')
        folder = values['compress_folder']
        make_archive(filepath, folder)
        window['compress_output'].update(value="Compression Completed!")
    if event == "Extract":
        archive_path = values['archive']
        dest_dir = values['extract_folder']
        extract_archive(archive_path, dest_dir)
        window["extract_output"].update(value="Extraction Completed!")

print("Thank you!")
window.close()
