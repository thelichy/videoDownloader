import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QFileDialog, QCheckBox, QRadioButton, QMessageBox
from downloader import download_playlist, download_single


class VideoDownloaderApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Baixar vídeos')
		self.setGeometry(100, 100, 500, 300)

		self.initUI()

	def initUI(self):
		self.type_label = QLabel('Tipo:', self)
		self.type_label.setGeometry(20, 20, 80, 30)

		self.type_combobox = QComboBox(self)
		self.type_combobox.setGeometry(110, 20, 120, 30)
		self.type_combobox.addItems(['Playlist', 'Video'])

		self.url_label = QLabel('URL:', self)
		self.url_label.setGeometry(20, 60, 80, 30)

		self.url_entry = QLineEdit(self)
		self.url_entry.setGeometry(110, 60, 280, 30)

		self.clear_button = QPushButton('Limpar', self)
		self.clear_button.setGeometry(400, 60, 80, 30)
		self.clear_button.clicked.connect(self.clear_url)

		self.extension_label = QLabel('Extensão:', self)
		self.extension_label.setGeometry(20, 100, 80, 30)

		self.mp3_radio = QRadioButton('MP3', self)
		self.mp3_radio.setGeometry(110, 100, 80, 30)
		self.mp3_radio.setChecked(True)

		self.mp4_radio = QRadioButton('MP4', self)
		self.mp4_radio.setGeometry(200, 100, 80, 30)

		self.only_audio_checkbox = QCheckBox('Apenas áudio', self)
		self.only_audio_checkbox.setGeometry(20, 140, 200, 30)
		self.only_audio_checkbox.setChecked(True)

		self.browse_button = QPushButton('Selecionar Caminho', self)
		self.browse_button.setGeometry(20, 180, 150, 30)
		self.browse_button.clicked.connect(self.browse_path)

		self.path_label = QLabel('', self)
		self.path_label.setGeometry(180, 180, 300, 30)

		self.save_button = QPushButton('Baixar', self)
		self.save_button.setGeometry(20, 220, 150, 30)
		self.save_button.clicked.connect(self.save_data)

	def clear_url(self):
		self.url_entry.clear()

	def browse_path(self):
		file_path = QFileDialog.getExistingDirectory(self, 'Selecionar Caminho')
		if file_path:
			self.path_label.setText(file_path)

	def validate_fields(self):
		url = self.url_entry.text()
		path = self.path_label.text()

		if not url:
			QMessageBox.warning(self, 'Aviso', 'O campo URL está vazio.')
			return False

		if not path:
			QMessageBox.warning(self, 'Aviso', 'Selecione um caminho para salvar os arquivos.')
			return False

		return True

	def save_data(self):
		if not self.validate_fields():
			return
  
		download_type = self.type_combobox.currentText()
		url = self.url_entry.text()
		extension = 'mp3' if self.mp3_radio.isChecked() else 'mp4'
		only_audio = self.only_audio_checkbox.isChecked()
		path = self.path_label.text()

		try:
			if download_type == 'Playlist':
				download_playlist(url, extension, only_audio, path)
			else:
				download_single(url, extension, only_audio, path)

			QMessageBox.information(self, 'Concluído', 'Os vídeos foram baixados')
		except Exception as e:
			QMessageBox.critical(self, 'Erro', f'Não foi possível baixar os vídeos: {str(e)}')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWin = VideoDownloaderApp()
	mainWin.show()
	sys.exit(app.exec_())
