import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from downloader import download_playlist, download_video



def save_data():
    download_type = type_combobox.get()
    url = url_entry.get()
    extension = extension_var.get()
    only_audio = only_audio_var.get()
    path = path_label.cget('text')

    if download_type == 'Playlist':
        download_playlist(url, extension, only_audio, path)
    else:
        download_video(url, extension, only_audio, path)

    messagebox.showinfo("Concluído", "Os vídeos foram baixados")


def browse_path():
    file_path = filedialog.askdirectory()
    if file_path:
        path_label.config(text=file_path)



window = tk.Tk()
window.title("Form")

frame = tk.Frame(window, padx=20, pady=20)
frame.pack()

type_label = tk.Label(frame, text="Tipo:")
type_label.grid(row=0, column=0, sticky="w")

available_types = ["Playlist", "Video"]
type_combobox = ttk.Combobox(frame, values=available_types)
type_combobox.grid(row=0, column=1)
type_combobox.set(available_types[0])

url_label = tk.Label(frame, text="URL:")
url_label.grid(row=1, column=0, sticky="w")

url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=1, column=1)

extension_label = tk.Label(frame, text="Extensão:")
extension_label.grid(row=2, column=0, sticky="w")

extension_var = tk.StringVar()
mp3_radio = tk.Radiobutton(frame, text="MP3", variable=extension_var, value="mp3")
mp4_radio = tk.Radiobutton(frame, text="MP4", variable=extension_var, value="mp4")

mp3_radio.grid(row=2, column=1)
mp4_radio.grid(row=2, column=2)

only_audio_var = tk.BooleanVar()
only_audio_checkbox = tk.Checkbutton(frame, text="Apenas áudio", variable=only_audio_var)
only_audio_checkbox.grid(row=3, columnspan=2, sticky="w")

browse_button = tk.Button(frame, text="Selecionar Caminho", command=browse_path)
browse_button.grid(row=5, column=0)

path_label = tk.Label(frame, text="")
path_label.grid(row=5, column=1)

save_button = tk.Button(frame, text="Baixar", command=save_data)
save_button.grid(row=6, column=0, columnspan=2)

window.mainloop()
