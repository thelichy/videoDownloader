import tkinter as tk
import ttkthemes as th
from tkinter.font import Font
from tkinter import ttk, messagebox, filedialog
from downloader import download_playlist, download_single



def save_data():
    download_type = type_combobox.get()
    url = url_entry.get()
    extension = extension_var.get()
    only_audio = only_audio_var.get()
    path = path_label.cget('text')

    try:
        if download_type == 'Playlist':
            download_playlist(url, extension, only_audio, path)
        else:
            download_single(url, extension, only_audio, path)

        messagebox.showinfo('Concluído', 'Os vídeos foram baixados')
    except:
        messagebox.showinfo('Erro', 'Não foi possível baixar os vídeos')


def clear_url():
    url_entry.delete(0, 'end')


def browse_path():
    file_path = filedialog.askdirectory()
    if file_path:
        path_label.config(text=file_path)


window = th.ThemedTk()
window.set_theme('equilux')
window.title('Baixar vídeos')

style = ttk.Style()
style.configure('TButton', padding=6, relief='flat', foreground='white')
style.configure('TLabel', padding=6)
style.configure('TRadiobutton', padding=6)
style.configure('TCheckbutton', padding=6)

frame = ttk.Frame(window)
frame.pack()

font = tk.font.Font(family='Arial', size=12)

type_label = ttk.Label(frame, text='Tipo:', font=font)
type_label.grid(row=0, column=0, sticky='w')

available_types = ['Playlist', 'Video']
type_combobox = ttk.Combobox(frame, values=available_types)
type_combobox.grid(row=0, column=1)
type_combobox.set(available_types[0])

url_label = ttk.Label(frame, text='URL:', font=font)
url_label.grid(row=1, column=0, sticky='w')

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=1, column=1)

clear_button = ttk.Button(frame, text='Limpar', command=clear_url)
clear_button.grid(row=1, column=2)

extension_label = ttk.Label(frame, text='Extensão:', font=font)
extension_label.grid(row=2, column=0, sticky='w')

extension_var = tk.StringVar()
mp3_radio = ttk.Radiobutton(frame, text='MP3', variable=extension_var, value='mp3')
mp4_radio = ttk.Radiobutton(frame, text='MP4', variable=extension_var, value='mp4')

mp3_radio.grid(row=2, column=1)
mp4_radio.grid(row=2, column=2)

only_audio_var = tk.BooleanVar()
only_audio_checkbox = ttk.Checkbutton(frame, text='Apenas áudio', variable=only_audio_var)
only_audio_checkbox.grid(row=3, columnspan=2, sticky='w')

browse_button = ttk.Button(frame, text='Selecionar Caminho', command=browse_path)
browse_button.grid(row=5, column=0)

path_label = ttk.Label(frame, text='')
path_label.grid(row=5, column=1)

save_button = ttk.Button(frame, text='Baixar', command=save_data)
save_button.grid(row=6, column=0, columnspan=2)

frame.configure()
url_entry.configure(style='TEntry')

type_label.configure(anchor='w')
url_label.configure(anchor='w')
extension_label.configure(anchor='w')

window.mainloop()
