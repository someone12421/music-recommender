import webbrowser
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)
from PyQt6.QtCore import Qt, QTimer

default = "https://www.youtube.com/watch?v=xvFZjo5PgG0"

genres = {
    "metal": "https://www.youtube.com/watch?v=bkUahLy_8Q4",
    "polka": "https://www.youtube.com/watch?v=vwKSN8pSq8g",
    "hyperpop": "https://www.youtube.com/watch?v=hIw7oeZKpZc",
    "deathcore": "https://youtu.be/8LaTzWMbShY",
    "pop": "https://www.youtube.com/watch?v=pm08v69vG10",
    "trash": "https://www.youtube.com/watch?v=63-ecB03_hI",
    "classical": "https://www.youtube.com/watch?v=b1KGOBttJrA",
    "sludge": "https://www.youtube.com/watch?v=c4KNd0Yv6d0",
    "israeli": "https://www.youtube.com/watch?v=WxhTbxMSvT0",
    "indie": "https://www.youtube.com/watch?v=xMUpyVSUZcY",
    "country": "https://www.youtube.com/watch?v=vf5AMfIOqGw",
    "techno": "https://www.youtube.com/watch?v=ff5lO8TkVX8",
    "kpop": "https://www.youtube.com/watch?v=GpjsgPDM4t8",
    "jazz": "https://youtu.be/h85k-rdiREk?t=18",
    "gangsta rap": "https://youtu.be/46F4smzPfVI",
    "avant garde": "https://youtu.be/UFKf08us2AI",
    "portuguese folk": "https://youtu.be/n2PsMSsOi1M",
    "phonk": "https://www.youtube.com/watch?v=dT4hLudO-is",
    "melodic punk": "https://youtu.be/ce6bIJ-7Ikw",
    "rap": "https://www.youtube.com/watch?v=6JQm5aSjX6g",
    "latin": "https://youtu.be/K2aYY8OpP-Q",
    "turkish jazz": "https://youtu.be/Kx_RIyzJF7A",
    "idol rock": "https://youtu.be/zQLdqnICsS8",
    "rock": "https://www.youtube.com/watch?v=_9DAvdZlt5o",
    "samba rock": "https://youtu.be/ameTtKHP5SA?list=PLTaQ4S5n4CwJMqlIq3jv9qC16tky6Ujev",
    "funk": "https://youtu.be/Ms_rKoyMw8A",
    "dark folk": "https://youtu.be/Qve-mCQcAMk?t=5",
    "edm": "https://www.youtube.com/watch?v=zSwcTiurwwk",
    "blues": "https://youtu.be/ciSdKJh5iVk",
    "dwarf metal": "https://www.youtube.com/watch?v=npjF032TDDQ",
    "nu metal": "https://www.youtube.com/watch?v=cQzMHhRCTYw",
}

class MusicGenreRecommender(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Genre Recommender")
        self.setMinimumSize(400, 250)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.label = QLabel("Pick a genre, and I will recommend a song from it:")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.message = QLabel("")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.message)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.submit_button = QPushButton("Submit")
        layout.addWidget(self.submit_button)

        self.entry.returnPressed.connect(self.open_genre_url)
        self.submit_button.clicked.connect(self.open_genre_url)

        self.resize_widgets()

    def open_genre_url(self):
        genre = self.entry.text().lower()
        if genre == "close":
            self.message.setText("Closing...")
            QTimer.singleShot(1000, self.close_application)
        elif genre in genres:
            if genre.lower() == "edm":
                opening_text = "Opening EDM..."
            else:
                opening_text = f"Opening {genre.title()}..."
            self.message.setText(opening_text)
            QTimer.singleShot(1000, lambda: self.open_link(genres[genre]))
        else:
            self.message.setText("Unknown genre. Playing default.")
            QTimer.singleShot(1000, lambda: self.open_link(default))

    def open_link(self, url):
        webbrowser.open(url)
        self.message.setText("")

    def close_application(self):
        self.close()
        QApplication.quit()

    def resize_widgets(self):
        font_size = max(self.width() // 35, 10)
        font = self.font()
        font.setPointSize(font_size)
        self.label.setFont(font)
        self.message.setFont(font)
        self.entry.setFont(font)
        self.submit_button.setFont(font)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_widgets()

if __name__ == "__main__":
    app = QApplication([])
    window = MusicGenreRecommender()
    window.show()
    app.exec()
