import schedule
import time
from pathlib import Path

file_type = {
    'IMAGES': 'jpg, png, gif, jpeg',
    'AUDIO': 'mp3, wav, flac',
    'VIDEOS': 'mp4, avi, mkv, webm',
    'SHEETS': 'xls, xlsx, gsheet',
    'DOCS': 'doc, docx, gdoc',
    'BOOKS': 'pdf, epub, mobi',
    'ARCHIVES': 'zip, tar, rar',
    'DATABASES': 'db, sql, csv, json',
    'OTHER_DOCS': 'txt, md, ppt, pptx',
    'PYTHON': 'py, pyw, ipynb',
    'JAVASCRIPT': 'js',
    'HTML': 'html, htm',
}


def organize_files(directory):

    path = Path(f'{str(Path.home())}\{directory}')

    def move(folder):
        folder_path = path / folder
        if not folder_path.exists():
            folder_path.mkdir()
        file.rename(folder_path / file.name)

    for file in path.iterdir():

        if file.is_file():
            file_ext = file.suffix[1:]
            for key, value in file_type.items():
                if file_ext in value:
                    move(key)
                    break
            else:
                move('OTHERS')


schedule.every(1).minutes.do(organize_files, 'Downloads')


while True:
    schedule.run_pending()
    time.sleep(1)
