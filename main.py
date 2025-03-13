from hdr.lolapi import *
from hdr.pyqt import *

import sys

if __name__ == "__main__":
    # Run Application
    print("Program Start")
    
    app = QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()
    sys.exit(app.exec_())