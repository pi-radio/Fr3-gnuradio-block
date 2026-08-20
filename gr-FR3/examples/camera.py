import sys
from PIL import Image
import cv2
from gnuradio import gr, blocks, qtgui
from PyQt5 import Qt
import sip

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

complex_points = []
target_width, target_height = 1920, 1080 


frame_count = 0
while cap.isOpened() and frame_count < 30:
    ret, frame = cap.read()
    if not ret:
        print("Warning: Could not read frame from camera.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (target_width, target_height))

    for y in range(target_height):
        for x in range(target_width):
            pixel_value = resized_frame[y, x]
            if pixel_value < 128: 
                i = (x / (target_width - 1)) * 2.0 - 1.0
                q = -((y / (target_height - 1)) * 2.0 - 1.0)
                complex_points.append(complex(i, q))
                
    frame_count += 1

cap.release()

if not complex_points:
    print("Error: No data captured. Is your camera covered or in a pitch-black room?")
    complex_points = [complex(0,0)] 
class ConstellationDemo(gr.top_block):

  def __init__(self):
    super().__init__('Constellation')
    sample_data = complex_points
    self.src = blocks.vector_source_c(sample_data, True)
    self.throttle = blocks.throttle(gr.sizeof_gr_complex, 32000)
    self.const_sink = qtgui.const_sink_c(100000000, 'Vector Constellation', 1)
    self.const_sink.set_update_time(0.1)
    self.connect(self.src, self.throttle, self.const_sink)


def main():
  app = Qt.QApplication(sys.argv)
  tb = ConstellationDemo()
  tb.start()
  py_widget = sip.wrapinstance(tb.const_sink.qwidget(), Qt.QWidget)
  main_win = Qt.QMainWindow()
  main_win.setCentralWidget(py_widget)
  main_win.resize(600, 600)
  main_win.setWindowTitle('Video Constellation')
  main_win.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
