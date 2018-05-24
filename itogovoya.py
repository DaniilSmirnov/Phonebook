from PyQt5 import QtCore, QtGui, QtWidgets
from pymsgbox import *
from xml.dom import minidom
from yattag import Doc, indent

item = 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.AddButton = QtWidgets.QPushButton(self.layoutWidget)
        self.AddButton.setObjectName("AddButton")
        self.gridLayout.addWidget(self.AddButton, 0, 0, 1, 1)
        self.EditButton = QtWidgets.QPushButton(self.layoutWidget)
        self.EditButton.setObjectName("EditButton")
        self.gridLayout.addWidget(self.EditButton, 0, 1, 1, 1)
        self.DeleteButton = QtWidgets.QPushButton(self.layoutWidget)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 0, 2, 1, 1)
        self.SearchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout.addWidget(self.SearchButton, 0, 3, 1, 1)
        self.DataView = QtWidgets.QTextBrowser(self.layoutWidget)
        self.DataView.setObjectName("DataView")
        self.gridLayout.addWidget(self.DataView, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.LoadData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.EditButton.setText(_translate("MainWindow", "Edit"))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))

        self.AddButton.clicked.connect(self.open_addview)
        self.DeleteButton.clicked.connect(self.open_deleteview)
        self.EditButton.clicked.connect(self.open_editview)
        self.SearchButton.clicked.connect(self.open_searchview)

    def open_addview(self):
        add = Add()
        add.exec_()
        self.updateui()

    def open_editview(self):
        edit = Edit()
        edit.exec_()
        self.updateui()

    def open_deleteview(self):
        delete = Delete()
        delete.exec_()
        self.updateui()

    def open_searchview(self):
        search = Search()
        search.exec_()
        self.updateui()

    def LoadData(self):

        self.DataView.append("Room" +  '{:^24}'.format("Phone") +  '{:^30}'.format("Workers"))

        Data.Close(Data)
        i = int(Data.ReadI(Data))
        j = 1
        while j <= i:
            self.DataView.append((Data.Read(Data, "room", j)) + " " + '{:^30}'.format(Data.Read(Data, "phone",j)) + " "
                                    + '{:^30}'.format(Data.Read(Data, "workers", j)))
            j += 1
        Data.Init(Data)

    def updateui(self):

        self.DataView.close()

        self.DataView = QtWidgets.QTextBrowser(self.layoutWidget)
        self.DataView.setObjectName("DataView")
        self.gridLayout.addWidget(self.DataView, 1, 0, 1, 4)

        self.LoadData()


class Add_Ui(object):
    def setupUi(self, Add_Ui):
        Add_Ui.setObjectName("Add_Ui")
        Add_Ui.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Add_Ui)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 10, 381, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.roomedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.roomedit.setObjectName("roomedit")
        self.gridLayout.addWidget(self.roomedit, 0, 1, 1, 1)
        self.phoneedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.phoneedit.setObjectName("phoneedit")
        self.gridLayout.addWidget(self.phoneedit, 2, 1, 1, 1)
        self.workersedit = QtWidgets.QTextEdit(self.layoutWidget)
        self.workersedit.setObjectName("workersedit")
        self.gridLayout.addWidget(self.workersedit, 3, 1, 1, 1)
        self.roomlabel = QtWidgets.QLabel(self.layoutWidget)
        self.roomlabel.setObjectName("roomlabel")
        self.gridLayout.addWidget(self.roomlabel, 0, 0, 1, 1)
        self.workerslabel = QtWidgets.QLabel(self.layoutWidget)
        self.workerslabel.setObjectName("workerslabel")
        self.gridLayout.addWidget(self.workerslabel, 3, 0, 1, 1)
        self.phonelabel = QtWidgets.QLabel(self.layoutWidget)
        self.phonelabel.setObjectName("phonelabel")
        self.gridLayout.addWidget(self.phonelabel, 2, 0, 1, 1)
        self.okbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 4, 1, 1, 1)
        self.addbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.addbutton.setObjectName("addbutton")
        self.gridLayout.addWidget(self.addbutton, 4, 0, 1, 1)

        self.retranslateUi(Add_Ui)
        QtCore.QMetaObject.connectSlotsByName(Add_Ui)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.roomlabel.setText(_translate("Add_Ui", "room"))
        self.workerslabel.setText(_translate("Add_Ui", "Workers"))
        self.phonelabel.setText(_translate("Add_Ui", "phone"))
        self.okbutton.setText(_translate("Add_Ui", "OK"))
        self.addbutton.setText(_translate("Add_Ui", "Add"))


class Add(QtWidgets.QDialog, Add_Ui):
    def __init__(self, parent=None):
        global cost

        super(Add, self).__init__(parent)
        self.setupUi(self)

        self.okbutton.clicked.connect(self.close)
        self.addbutton.clicked.connect(self.add)

    def add(self):
        room = self.roomedit.text()
        phone = self.phoneedit.text()
        workers = self.workersedit.toPlainText()
        Data.Write(self, room, phone, workers)


class Edit_Ui(object):
    def setupUi(self, Edit_Ui):
        Edit_Ui.setObjectName("Edit_Ui")
        Edit_Ui.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Edit_Ui)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 10, 381, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.roomedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.roomedit.setObjectName("roomedit")
        self.gridLayout.addWidget(self.roomedit, 0, 1, 1, 1)
        self.phoneedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.phoneedit.setObjectName("phoneedit")
        self.gridLayout.addWidget(self.phoneedit, 2, 1, 1, 1)
        self.workersedit = QtWidgets.QTextEdit(self.layoutWidget)
        self.workersedit.setObjectName("workersedit")
        self.gridLayout.addWidget(self.workersedit, 3, 1, 1, 1)
        self.roomlabel = QtWidgets.QLabel(self.layoutWidget)
        self.roomlabel.setObjectName("roomlabel")
        self.gridLayout.addWidget(self.roomlabel, 0, 0, 1, 1)
        self.workerslabel = QtWidgets.QLabel(self.layoutWidget)
        self.workerslabel.setObjectName("workerslabel")
        self.gridLayout.addWidget(self.workerslabel, 3, 0, 1, 1)
        self.phonelabel = QtWidgets.QLabel(self.layoutWidget)
        self.phonelabel.setObjectName("phonelabel")
        self.gridLayout.addWidget(self.phonelabel, 2, 0, 1, 1)
        self.okbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 4, 1, 1, 1)
        self.editbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.editbutton.setObjectName("editbutton")
        self.gridLayout.addWidget(self.editbutton, 4, 0, 1, 1)

        self.retranslateUi(Edit_Ui)
        QtCore.QMetaObject.connectSlotsByName(Edit_Ui)

    def retranslateUi(self, Edit_ui):
        _translate = QtCore.QCoreApplication.translate
        self.roomlabel.setText(_translate("Edit_Ui", "room"))
        self.workerslabel.setText(_translate("Edit_Ui", "Workers"))
        self.phonelabel.setText(_translate("Edit_Ui", "phone"))
        self.okbutton.setText(_translate("Edit_Ui", "OK"))
        self.editbutton.setText(_translate("Edit_Ui", "Edit"))


class Edit(QtWidgets.QDialog, Edit_Ui):
    def __init__(self, parent=None):

        super(Edit, self).__init__(parent)
        self.setupUi(self)

        self.okbutton.clicked.connect(self.close)
        self.editbutton.clicked.connect(self.edit)

    def edit(self):
        try:
            room = self.roomedit.text()
            phone = self.phoneedit.text()
            workers = self.workersedit.toPlainText()
            Data.Delete(Data, room)
            Data.Write(Data, room, phone, workers)
        except BaseException:
            alert(text='Check your input', title='Warning!', button='OK')


class Delete_Ui(object):
    def setupUi(self, Delete_Ui):
        Delete_Ui.setObjectName("DeleteUi")
        Delete_Ui.resize(400, 117)
        self.widget = QtWidgets.QWidget(Delete_Ui)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.deletebutton = QtWidgets.QPushButton(self.widget)
        self.deletebutton.setObjectName("deletebutton")
        self.gridLayout.addWidget(self.deletebutton, 2, 0, 1, 1)
        self.okbutton = QtWidgets.QPushButton(self.widget)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 2, 1, 1, 1)
        self.roomedit = QtWidgets.QLineEdit(self.widget)
        self.roomedit.setObjectName("roomedit")
        self.gridLayout.addWidget(self.roomedit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(Delete_Ui)
        QtCore.QMetaObject.connectSlotsByName(Delete_Ui)

    def retranslateUi(self, DeleteUi):
        _translate = QtCore.QCoreApplication.translate
        DeleteUi.setWindowTitle(_translate("DeleteUi", "Delete"))
        self.deletebutton.setText(_translate("DeleteUi", "Delete"))
        self.okbutton.setText(_translate("DeleteUi", "OK"))
        self.label.setText(_translate("DeleteUi", "Room"))


class Delete(QtWidgets.QDialog, Delete_Ui):
    def __init__(self, parent=None):

        super(Delete, self).__init__(parent)
        self.setupUi(self)

        self.okbutton.clicked.connect(self.close)
        self.deletebutton.clicked.connect(self.Delete)

    def Delete(self):
        try:
            room = self.roomedit.text()
            Data.Delete(Data, room)
        except BaseException:
            alert(text='Check your input', title='Warning!', button='OK')


class Search_Ui(object):
    def setupUi(self, Search_Ui):
        Search_Ui.setObjectName("Dialog")
        Search_Ui.resize(264, 102)
        self.widget = QtWidgets.QWidget(Search_Ui)
        self.widget.setGeometry(QtCore.QRect(10, 10, 241, 81))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.selectbox = QtWidgets.QComboBox(self.widget)
        self.selectbox.setObjectName("selectbox")
        self.gridLayout.addWidget(self.selectbox, 1, 1, 1, 1)
        self.okbutton = QtWidgets.QPushButton(self.widget)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 3, 1, 1, 1)
        self.selectedit = QtWidgets.QLineEdit(self.widget)
        self.selectedit.setObjectName("selectedit")
        self.gridLayout.addWidget(self.selectedit, 1, 0, 1, 1)
        self.searchbutton = QtWidgets.QPushButton(self.widget)
        self.searchbutton.setObjectName("searchbutton")
        self.gridLayout.addWidget(self.searchbutton, 3, 0, 1, 1)
        self.resultbrowser = QtWidgets.QTextBrowser(self.widget)
        self.resultbrowser.setObjectName("resultbrowser")
        self.gridLayout.addWidget(self.resultbrowser, 2, 0, 1, 2)

        self.retranslateUi(Search_Ui)
        QtCore.QMetaObject.connectSlotsByName(Search_Ui)

    def retranslateUi(self, Search_Ui):
        _translate = QtCore.QCoreApplication.translate
        Search_Ui.setWindowTitle(_translate("Dialog", "Search"))
        self.okbutton.setText(_translate("Dialog", "OK"))
        self.searchbutton.setText(_translate("Dialog", "Search"))

        self.selectbox.addItem("Room")
        self.selectbox.addItem("Worker")


class Search(QtWidgets.QDialog, Search_Ui):

    def __init__(self, parent=None):

        super(Search, self).__init__(parent)
        self.setupUi(self)

        self.okbutton.clicked.connect(self.close)
        self.selectbox.activated[str].connect(self.setitem)
        self.searchbutton.clicked.connect(self.search)

    def setitem(self, text):

        global item
        item = text
        print(1)

    def search(self):
        try:
            global item

            if item == 1:
                item = "room"
            if item == 2:
                item = "worker"
            if item == 'Room':
                item = "room"
            if item == "Worker":
                item = "workers"

            pos = self.selectedit.text()
            self.resultbrowser.setText(Data.Search(Data, item, pos))
        except BaseException:
            alert(text='Check your input', title='Warning!', button='OK')


class Data(object):

    def ReadI(self):

        xmldoc = minidom.parse('data.xml')
        itemlist = xmldoc.getElementsByTagName(str("res"))
        return itemlist[0].attributes["i"].value

    def Read(self, position, index):
        xmldoc = minidom.parse('data.xml')
        itemlist = xmldoc.getElementsByTagName("position"+str(index))
        return itemlist[0].attributes[str(position)].value

    def Init(self):
        filename = 'data.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        global k
        k = int(self.ReadI(Data))

        myfile = open(filename, 'w')
        for line in lines:
            if line != "</res>":
                myfile.write(line)
        myfile.close()

    def Close(self):
        global k

        filename = 'data.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        myfile = open(filename, 'w')
        for line in lines:
            if line.find("<res") != -1:
                myfile.write("<res " + "i=" + '"' + str(k) + '"' + ">" + "\n")
            else:
                myfile.write(line)
        myfile.close()

        myfile = open(filename, 'a')
        myfile.write("</res>")
        myfile.close()

    def Write(self, room, phone, workers,):
        global k
        k += 1
        doc, tag, text = Doc().tagtext()
        with tag('position'+str(k), room=room, phone=phone, workers=workers):
            text(str(k))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n')

        filename = 'data.xml'
        myfile = open(filename, 'a')
        myfile.write(result)
        myfile.write("\n")
        myfile.close()
        print(result)

    def Delete(self,  room):
        filename = 'data.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        global k
        self.Close(self)
        k = int(self.ReadI(Data))
        self.Init(self)

        myfile = open(filename, 'w')

        i = 1

        for line in lines:
            if line.find("room=" + '"' + str(room) + '"') == -1 and line.find("res") == -1:
                buf = line.split("position")
                line = "<" + "position" + str(i) + str(buf[1])[1:] + "position" + str(i) + ">" + "\n"
                myfile.write(line)
                i += 1
                k -= 1
            if (line.find("room=" + '"' + str(room) + '"') == -1) and (line.find("position") == -1):
                myfile.write(line)
        myfile.close()

    def Search(self, pos, item):
        filename = 'data.xml'
        myfile = open(filename, 'r')
        lines = myfile.readlines()
        myfile.close()

        i = 0

        for line in lines:
            if (line.find(pos + "=") != 1) and (line.find(str(item)) != -1):
                self.Close(self)
                returner = self.Read(self, "room", i) + " " + self.Read(self, "phone", i) + " " + self.Read(self, "workers", i)
                self.Init(self)
                return returner
            i += 1


Data.Init(Data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_(), Data.Close(Data))
