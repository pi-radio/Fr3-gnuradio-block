from gnuradio import gr, blocks, qtgui
from PyQt5 import Qt
import sys
import sip
from PIL import Image
import cv2

#img_path = 'Untitled.png'  
#img = Image.open(img_path).convert('L').resize((55, 244))

#width, height = img.size
#complex_points = []


for y in range(height):
    for x in range(width):
        pixel_value = img.getpixel((x, y))
        if pixel_value < 128:
            i = (x / (width - 1)) * 2.0 - 1.0
            q = -((y / (height - 1)) * 2.0 - 1.0) 
            complex_points.append(complex(i, q))

class ConstellationDemo(gr.top_block):
    def __init__(self):
        super().__init__("Constellation")
        
        sample_data = complex_points
        
        self.src = blocks.vector_source_c(sample_data, True)
        
        self.throttle = blocks.throttle(gr.sizeof_gr_complex, 32000)
        
        self.const_sink = qtgui.const_sink_c(
            1024,                  
            "Vector Constellation", 
            1                    
        )
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
    main_win.setWindowTitle("window")
    main_win.show()
    
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
