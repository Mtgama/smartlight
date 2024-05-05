import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, \
    QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer
import cv2
from PyQt5.QtCore import pyqtSignal


class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()

        self.default_red_time = 10
        self.default_yellow_time = 3
        self.default_green_time = 10

        self.red_on = True
        self.yellow_on = False
        self.green_on = False
        self.timer_count = self.default_red_time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Timer updates every second

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Traffic Light')

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 24, QFont.Bold))

        self.combo_box = QComboBox()
        self.combo_box.addItem("Cloudy")
        self.combo_box.addItem("Snowy")
        self.combo_box.addItem("Sunny")
        self.combo_box.addItem("Icy Roads")
        self.combo_box.addItem("Emergency")
        self.combo_box.currentIndexChanged.connect(self.update_timings)

        self.ip_address_label = QLabel("IP Address:")
        self.port_label = QLabel("Port:")
        self.ip_address_edit = QLineEdit()
        self.port_edit = QLineEdit()

        self.analyze_button = QPushButton("Analyze with Camera")
        self.analyze_button.clicked.connect(self.analyze_with_camera)

        # Label to display number of detected cars
        self.car_count_label = QLabel("Number of Cars: 0")

        # Layout for IP address, port, and button
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.ip_address_label)
        self.input_layout.addWidget(self.ip_address_edit)
        self.input_layout.addWidget(self.port_label)
        self.input_layout.addWidget(self.port_edit)
        self.input_layout.addWidget(self.analyze_button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.car_count_label)
        self.layout.addLayout(self.input_layout)
        self.layout.addStretch(1)  # Add space between countdown and lights
        self.setLayout(self.layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        
        painter.setBrush(QColor(255, 0, 0) if self.red_on else QColor(100, 0, 0))
        painter.drawEllipse(150, 150, 100, 100)

        
        painter.setBrush(QColor(255, 255, 0) if self.yellow_on else QColor(100, 100, 0))
        painter.drawEllipse(150, 250, 100, 100)

        
        painter.setBrush(QColor(0, 255, 0) if self.green_on else QColor(0, 100, 0))
        painter.drawEllipse(150, 350, 100, 100)

    def update_timer(self):
        self.timer_count -= 1

        if self.timer_count == 0:
            if self.red_on:
                self.red_on = False
                self.yellow_on = True
                self.timer_count = self.default_yellow_time
            elif self.yellow_on:
                self.yellow_on = False
                self.green_on = True
                self.timer_count = self.default_green_time
            else:
                self.green_on = False
                self.red_on = True
                self.timer_count = self.default_red_time

        self.update()
        self.label.setText(str(self.timer_count))

    def update_timings(self, index):
        if self.combo_box.currentText() == "یخ زدگی":
            self.default_red_time = 30
            self.default_yellow_time = 6
            self.default_green_time = 30
        elif self.combo_box.currentText() == "اضطراری":
            self.default_red_time = 5
            self.default_yellow_time = 2
            self.default_green_time = 30
        elif self.combo_box.currentText() == "برفی":
            self.default_red_time = 30
            self.default_yellow_time = 5
            self.default_green_time = 30
        else:
            self.default_red_time = 10
            self.default_yellow_time = 3
            self.default_green_time = 10

        self.timer_count = self.default_red_time



class TrafficControlWindow(QWidget):
    # Define a signal to be emitted when the Apply button is clicked
    apply_clicked = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Light Control")
        self.setGeometry(200, 200, 400, 200)

        self.red_label = QLabel("تغییر زمان چراغ قرمز")
        self.green_label = QLabel("تغییر زمان چراغ سبز")
        self.yellow_label = QLabel("تغییر زمان چراغ زرد")

        self.red_edit = QLineEdit()
        self.green_edit = QLineEdit()
        self.yellow_edit = QLineEdit()

        self.apply_button = QPushButton("اعمال")
        self.apply_button.clicked.connect(self.apply_light_times)

        layout = QVBoxLayout()
        layout.addWidget(self.red_label)
        layout.addWidget(self.red_edit)
        layout.addWidget(self.green_label)
        layout.addWidget(self.green_edit)
        layout.addWidget(self.yellow_label)
        layout.addWidget(self.yellow_edit)
        layout.addWidget(self.apply_button)

        self.setLayout(layout)

    def apply_light_times(self):
        # Retrieve the entered light times
        red_time = int(self.red_edit.text())
        green_time = int(self.green_edit.text())
        yellow_time = int(self.yellow_edit.text())

        # Emit the signal with the new light times
        self.apply_clicked.emit(red_time, green_time, yellow_time)


class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()

        self.default_red_time = 10
        self.default_yellow_time = 3
        self.default_green_time = 10

        self.red_on = True
        self.yellow_on = False
        self.green_on = False
        self.timer_count = self.default_red_time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Timer updates every second

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Traffic Light')

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 24, QFont.Bold))

        self.combo_box = QComboBox()
        self.combo_box.addItem("ابری")
        self.combo_box.addItem("برفی")
        self.combo_box.addItem("افتابی")
        self.combo_box.addItem("یخ زدگی")
        self.combo_box.addItem("اضطراری")
        self.combo_box.currentIndexChanged.connect(self.update_timings)

        self.ip_address_label = QLabel("آدرس ip:")
        self.port_label = QLabel("پورت:")
        self.ip_address_edit = QLineEdit()
        self.port_edit = QLineEdit()

        self.analyze_button = QPushButton("آنالیز ترافیک بوسیله دوربین")
        self.analyze_button.clicked.connect(self.analyze_with_camera)

        # Label to display number of detected cars
        self.car_count_label = QLabel("تعداد ماشین:0")

        # Layout for IP address, port, and button
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.ip_address_label)
        self.input_layout.addWidget(self.ip_address_edit)
        self.input_layout.addWidget(self.port_label)
        self.input_layout.addWidget(self.port_edit)
        self.input_layout.addWidget(self.analyze_button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.car_count_label)
        self.layout.addLayout(self.input_layout)
        self.layout.addStretch(1)  # Add space between countdown and lights
        self.setLayout(self.layout)

        # Create an instance of the TrafficControlWindow
        self.traffic_control_window = TrafficControlWindow()
        # Connect the signal from TrafficControlWindow to a slot in TrafficLight
        self.traffic_control_window.apply_clicked.connect(self.update_light_times)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw red light
        painter.setBrush(QColor(255, 0, 0) if self.red_on else QColor(100, 0, 0))
        painter.drawEllipse(150, 150, 100, 100)

        # Draw yellow light
        painter.setBrush(QColor(255, 255, 0) if self.yellow_on else QColor(100, 100, 0))
        painter.drawEllipse(150, 250, 100, 100)

        # Draw green light
        painter.setBrush(QColor(0, 255, 0) if self.green_on else QColor(0, 100, 0))
        painter.drawEllipse(150, 350, 100, 100)

    def update_timer(self):
        self.timer_count -= 1

        if self.timer_count == 0:
            if self.red_on:
                self.red_on = False
                self.yellow_on = True
                self.timer_count = self.default_yellow_time
            elif self.yellow_on:
                self.yellow_on = False
                self.green_on = True
                self.timer_count = self.default_green_time
            else:
                self.green_on = False
                self.red_on = True
                self.timer_count = self.default_red_time

        self.update()
        self.label.setText(str(self.timer_count))

    def update_timings(self, index):
        if self.combo_box.currentText() == "یخ زدگی":
            self.default_red_time = 30
            self.default_yellow_time = 6
            self.default_green_time = 30
        elif self.combo_box.currentText() == "اضطراری":
            self.default_red_time = 5
            self.default_yellow_time = 2
            self.default_green_time = 30
        elif self.combo_box.currentText() == "برفی":
            self.default_red_time = 30
            self.default_yellow_time = 5
            self.default_green_time = 30
        else:
            self.default_red_time = 10
            self.default_yellow_time = 3
            self.default_green_time = 10

        self.timer_count = self.default_red_time

    def analyze_with_camera(self):
        ip_address = self.ip_address_edit.text()
        port = self.port_edit.text()

        camera_url = f"http://{ip_address}:{port}/video"
        cascade_path = 'cars.xml'
        car_cascade = cv2.CascadeClassifier(cascade_path)

        cap = cv2.VideoCapture(camera_url)

        if not cap.isOpened():
            print("Failed to open camera stream.")
            return

        car_count = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                QMessageBox.information(self,'عدم دریافت',"اطلاعاتی دریافت نشد")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cars = car_cascade.detectMultiScale(gray, 1.1, 3)

            car_count = len(cars)
            self.car_count_label.setText(f"Number of Cars: {car_count}")

            if car_count > 10:
                reply = QMessageBox.question(self, 'هشدار ترافیک', 'ترافیک سنگین شناسایی شد!', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Help)
                if reply == QMessageBox.Ok:
                    self.traffic_control_window.show()


            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('Car Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def update_light_times(self, red_time, green_time, yellow_time):
        # Update the default light times with the new values
        self.default_red_time = red_time
        self.default_green_time = green_time
        self.default_yellow_time = yellow_time

        # Restart the timer with the new light times
        self.timer.stop()
        self.timer_count = self.default_red_time
        self.timer.start(1000)  # Restart timer with new intervals


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrafficLight()
    window.show()
    sys.exit(app.exec_())

