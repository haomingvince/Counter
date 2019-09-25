"""
Author: Haoming Zhang
Last edited: 09/24/20119
"""

import sys
import os
from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QApplication, QMessageBox, QDesktopWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QCoreApplication
from datetime import date

class Counter(QWidget):

    def __init__(self):
        super().__init__()

        fname = str(date.today()) + ".txt"
        if os.path.exists(fname):
            self.setCount("r")
        else:
            self.setCount("w")
        self.initUI()
        self.buttonEvent()
        

    def initUI(self):
        self.resize(250, 250)
        self.center()

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # 个体
        self.label_geti = QLabel('个体')
        self.grid.addWidget(self.label_geti, 0, 0)
        # Checkbox
        self.ck_geti_xs = QCheckBox('新设')
        self.ck_geti_xs.setChecked(False)
        self.grid.addWidget(self.ck_geti_xs, 1, 0)
        self.ck_geti_bg = QCheckBox('变更')
        self.ck_geti_bg.setChecked(False)
        self.grid.addWidget(self.ck_geti_bg, 1, 1)
        self.ck_geti_zx = QCheckBox('注销')
        self.ck_geti_zx.setChecked(False)
        self.grid.addWidget(self.ck_geti_zx, 1, 2)
        self.ck_geti_hm = QCheckBox('核名')
        self.ck_geti_hm.setChecked(False)
        self.grid.addWidget(self.ck_geti_hm, 1, 3)

        self.ck_geti_zx = QCheckBox('咨询')
        self.ck_geti_zx.setChecked(False)
        self.grid.addWidget(self.ck_geti_zx, 2, 0)
        self.ck_geti_tda = QCheckBox('提档案')
        self.ck_geti_tda.setChecked(False)
        self.grid.addWidget(self.ck_geti_tda, 2, 1)
        self.ck_geti_nb = QCheckBox('年报')
        self.ck_geti_nb.setChecked(False)
        self.grid.addWidget(self.ck_geti_nb, 2, 2)
        self.ck_geti_ycyc = QCheckBox('移出异常')
        self.ck_geti_ycyc.setChecked(False)
        self.grid.addWidget(self.ck_geti_ycyc, 2, 3)

        self.ck_geti_qy = QCheckBox('迁移')
        self.ck_geti_qy.setChecked(False)
        self.grid.addWidget(self.ck_geti_qy, 3, 0)


        # 公司
        self.label_gongsi = QLabel('公司')
        self.grid.addWidget(self.label_gongsi, 4, 0)
        # Checkbox
        self.ck_gongsi_xs = QCheckBox('新设')
        self.ck_gongsi_xs.setChecked(False)
        self.grid.addWidget(self.ck_gongsi_xs, 5, 0)
        self.ck_gongsi_bg = QCheckBox('变更')
        self.ck_gongsi_bg.setChecked(False)
        self.grid.addWidget(self.ck_gongsi_bg, 5, 1)
        self.ck_gongsi_zx = QCheckBox('注销')
        self.ck_gongsi_zx.setChecked(False)
        self.grid.addWidget(self.ck_gongsi_zx, 5, 2)
        self.ck_gongsi_hm = QCheckBox('核名')
        self.ck_gongsi_hm.setChecked(False)
        self.grid.addWidget(self.ck_gongsi_hm, 5, 3)


        # 分公司
        self.label_fengongsi = QLabel('分公司')
        self.grid.addWidget(self.label_fengongsi, 6, 0)
        # Checkbox
        self.ck_fengongsi_xs = QCheckBox('新设')
        self.ck_fengongsi_xs.setChecked(False)
        self.grid.addWidget(self.ck_fengongsi_xs, 7, 0)
        self.ck_fengongsi_bg = QCheckBox('变更')
        self.ck_fengongsi_bg.setChecked(False)
        self.grid.addWidget(self.ck_fengongsi_bg, 7, 1)
        self.ck_fengongsi_zx = QCheckBox('注销')
        self.ck_fengongsi_zx.setChecked(False)
        self.grid.addWidget(self.ck_fengongsi_zx, 7, 2)

        # Buttons
        self.label_cl = QLabel('今日办理总量(' + str(date.today()) + '):')
        self.grid.addWidget(self.label_cl, 8, 0)
        self.label_count = QLabel(str(self.count))
        self.grid.addWidget(self.label_count, 8, 1)
        self.bt_confirm = QPushButton('确定')
        self.grid.addWidget(self.bt_confirm, 9, 2)
        self.bt_quit = QPushButton('退出')
        self.grid.addWidget(self.bt_quit, 9, 3)

        self.ck_geti = [self.ck_geti_xs, self.ck_geti_bg, self.ck_geti_zx, self.ck_geti_hm,
                   self.ck_geti_zx, self.ck_geti_tda, self.ck_geti_nb, self.ck_geti_ycyc, self.ck_geti_qy]
        self.ck_gongsi = [self.ck_gongsi_xs, self.ck_gongsi_bg,
                     self.ck_gongsi_zx, self.ck_gongsi_hm]
        self.ck_fengongsi = [self.ck_fengongsi_xs,
                        self.ck_fengongsi_bg, self.ck_fengongsi_zx]
        
        self.setWindowTitle('工商咨询计数器')
        self.show()


    def setCount(self, mode="r", count=0):
        fname = str(date.today()) + ".txt"
        if mode == "r":
            with open(fname, mode) as f:
                content = f.readlines()
                self.count = int(content[0])
        elif mode == "r+":
            with open(fname, mode) as f:
                val = int(f.read())
                f.seek(0)
                self.count = val + count
                f.write(str(self.count))
        else:
            with open(fname, "w") as f:
                f.write('0')
                self.count = 0


    def buttonEvent(self):
        self.bt_confirm.clicked.connect(self.calc)
        self.bt_quit.clicked.connect(self.close)


    def calc(self):
        count = 0
        for geti in self.ck_geti:
            if geti.isChecked():
                count += 1
                geti.setChecked(False)
        for gongsi in self.ck_gongsi:
            if gongsi.isChecked():
                count += 1
                gongsi.setChecked(False)
        for fengongsi in self.ck_fengongsi:
            if fengongsi.isChecked():
                count += 1
                fengongsi.setChecked(False)
        self.updateCount(count)


    def updateCount(self, num):
        self.setCount(mode="r+", count=num)
        self.label_count.setText(str(self.count))


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "确定要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Counter()
    sys.exit(app.exec_())
