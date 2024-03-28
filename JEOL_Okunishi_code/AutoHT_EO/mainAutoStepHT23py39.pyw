# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:51:27 2020

@author: Eiji Okunishi
"""

import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore
from PyJEM.offline import TEM3
from time import sleep
import datetime
import configparser

from gui_AutoStepHT24_py38 import Ui_AutoStepHT

TEM3.connect()
 
class Test(QWidget):
  def __init__(self,parent=None):
    super(Test, self).__init__(parent)
    self.ui = Ui_AutoStepHT()
    self.ui.setupUi(self)
    
#外部制御の宣言(PyJEM)
 
    self.eos = TEM3.EOS3()
    self.ht = TEM3.HT3()
    self.gun = TEM3.GUN3()

    global setstage
    setstage = self.ui.comboBox_13.currentIndex()
    print(setstage)

    if (setstage == 0):
        self.ui.label_19.hide()
        self.ui.label_9.hide()
        self.ui.label_2.hide()
        self.ui.label_18.hide()
        self.ui.label_44.hide()

        self.ui.doubleSpinBox_ST2.hide()
        self.ui.doubleSpinBox_step2.hide()
        self.ui.doubleSpinBox_HT3.hide()

        self.ui.comboBox_2.hide()

        self.ui.label_10.hide()
        self.ui.label_21.hide()
        self.ui.label_45.hide()
        self.ui.label_20.hide()
        self.ui.label_3.hide()

        self.ui.doubleSpinBox_ST3.hide()
        self.ui.doubleSpinBox_step3.hide()
        self.ui.doubleSpinBox_HT4.hide()

        self.ui.comboBox_3.hide()

        self.ui.label_11.hide()
        self.ui.label_22.hide()
        self.ui.label_23.hide()
        self.ui.label_46.hide()
        self.ui.label_4.hide()

        self.ui.doubleSpinBox_ST4.hide()
        self.ui.doubleSpinBox_step4.hide()
        self.ui.doubleSpinBox_HT5.hide()

        self.ui.comboBox_4.hide()

        self.ui.groupBox_3.resize(111, 131)
        self.ui.groupBox_4.resize(91, 131)
        self.ui.groupBox_5.resize(81, 131)

        self.ui.groupBox.resize(311, 271) 

        self.ui.groupBox_6.setGeometry(5,270, 311, 131) #progress window

        self.ui.toolButton_3.setGeometry(10, 410, 81, 31) #close
        self.ui.pushButton_6.setGeometry(230, 410, 81, 31) #save 

        self.resize(322,450) # window

    elif (setstage == 1):
        #self.ui.label_19.show()
        #self.ui.label_9.show()
        #self.ui.label_2.show()
        #self.ui.label_18.show()
        #self.ui.label_44.show()

        #self.ui.doubleSpinBox_ST2.show()
        #self.ui.doubleSpinBox_step2.show()
        #self.ui.doubleSpinBox_HT3.show()

        #self.ui.comboBox_2.hide()

        self.ui.label_10.hide()
        self.ui.label_21.hide()
        self.ui.label_45.hide()
        self.ui.label_20.hide()
        self.ui.label_3.hide()

        self.ui.doubleSpinBox_ST3.hide()
        self.ui.doubleSpinBox_step3.hide()
        self.ui.doubleSpinBox_HT4.hide()

        self.ui.comboBox_3.hide()

        self.ui.label_11.hide()
        self.ui.label_22.hide()
        self.ui.label_23.hide()
        self.ui.label_46.hide()
        self.ui.label_4.hide()

        self.ui.doubleSpinBox_ST4.hide()
        self.ui.doubleSpinBox_step4.hide()
        self.ui.doubleSpinBox_HT5.hide()

        self.ui.comboBox_4.hide()

        self.ui.groupBox_3.resize(111, 211)
        self.ui.groupBox_4.resize(91, 211)
        self.ui.groupBox_5.resize(81, 211)

        self.ui.groupBox.resize(311, 351) 

        self.ui.groupBox_6.setGeometry(5,350, 311, 131) #progress window

        self.ui.toolButton_3.setGeometry(10, 490, 81, 31) #close
        self.ui.pushButton_6.setGeometry(230, 490, 81, 31) #save 

        self.resize(322,690) # window

    elif (setstage == 2):
        #self.ui.label_19.show()
        #self.ui.label_9.show()
        #self.ui.label_2.show()
        #self.ui.label_18.show()
        #self.ui.label_44.show()

        #self.ui.doubleSpinBox_ST2.show()
        #self.ui.doubleSpinBox_step2.show()
        #self.ui.doubleSpinBox_HT3.show()

        #self.ui.comboBox_2.show()

        #self.ui.label_10.show()
        #self.ui.label_21.show()
        #self.ui.label_45.show()
        #self.ui.label_20.show()
        #self.ui.label_3.show()

        #self.ui.doubleSpinBox_ST3.show()
        #self.ui.doubleSpinBox_step3.show()
        #self.ui.doubleSpinBox_HT4.show()

        #self.ui.comboBox_3.show()

        self.ui.label_11.hide()
        self.ui.label_22.hide()
        self.ui.label_23.hide()
        self.ui.label_46.hide()
        self.ui.label_4.hide()

        self.ui.doubleSpinBox_ST4.hide()
        self.ui.doubleSpinBox_step4.hide()
        self.ui.doubleSpinBox_HT5.hide()

        self.ui.comboBox_4.hide()

        self.ui.groupBox_3.resize(111, 291)
        self.ui.groupBox_4.resize(91, 291)
        self.ui.groupBox_5.resize(81, 291)

        self.ui.groupBox.resize(311, 431) 

        self.ui.groupBox_6.setGeometry(5,430, 311, 131) #progress window

        self.ui.toolButton_3.setGeometry(10, 570, 81, 31) #close
        self.ui.pushButton_6.setGeometry(230, 570, 81, 31) #save 

        self.resize(322,690) # window

    elif (setstage == 3):
        #self.ui.label_19.show()
        #self.ui.label_9.show()
        #self.ui.label_2.show()
        #self.ui.label_18.show()
        #self.ui.label_44.show()

        #self.ui.doubleSpinBox_ST2.show()
        #self.ui.doubleSpinBox_step2.show()
        #self.ui.doubleSpinBox_HT3.show()

        #self.ui.comboBox_2.show()

        #self.ui.label_10.show()
        #self.ui.label_21.show()
        #self.ui.label_45.show()
        #self.ui.label_20.show()
        #self.ui.label_3.show()

        #self.ui.doubleSpinBox_ST3.show()
        #self.ui.doubleSpinBox_step3.show()
        #self.ui.doubleSpinBox_HT4.show()

        #self.ui.comboBox_3.show()

        #self.ui.label_11.show()
        #self.ui.label_22.show()
        #self.ui.label_23.show()
        #self.ui.label_46.show()
        #self.ui.label_4.show()

        #self.ui.doubleSpinBox_ST4.show()
        #self.ui.doubleSpinBox_step4.show()
        #self.ui.doubleSpinBox_HT5.show()

        #self.ui.comboBox_4.show()

        self.ui.groupBox_3.resize(111, 371)
        self.ui.groupBox_4.resize(91, 371)
        self.ui.groupBox_5.resize(81, 371)

        self.ui.groupBox.resize(311, 511) 

        self.ui.groupBox_6.setGeometry(5,510, 311, 131) #progress window

        self.ui.toolButton_3.setGeometry(10, 650, 81, 31) #close
        self.ui.pushButton_6.setGeometry(230, 650, 81, 31) #save 

        self.resize(322,690) # window
    

   # global HT1
   # global HT2
   # global HT3
   # global HT4
    global HT5
    
   # global ST2
    #g#lobal ST3
    #global ST4
    
    global SV1
    global SV2
    global SV3
    global SV4
    
    global SV1c
    global SV2c
    global SV3c
    global SV4c
    
    #global step1
    #global step2
    #global step3
    #global step4
    
    global num
    
    global a1

    now = datetime.datetime.now()
    #print('Start:{%m/%d-%H:%M:%S}'.format(now))
    a = 360
    now2 = now + (datetime.timedelta(seconds=1)* a)
    #print('Expected End time:{%m/%d-%H:%M:%S}'.format(now2))

    HT1 = self.ui.doubleSpinBox_HT1.value()
    HT2 = self.ui.doubleSpinBox_HT2.value()
    HT3 = self.ui.doubleSpinBox_HT3.value()
    HT4 = self.ui.doubleSpinBox_HT4.value()
    HT5 = self.ui.doubleSpinBox_HT5.value()
    
    #ST1 = self.ui.doubleSpinBox_ST1.value()
    ST2 = self.ui.doubleSpinBox_ST2.value()
    ST3 = self.ui.doubleSpinBox_ST3.value()
    ST4 = self.ui.doubleSpinBox_ST4.value()
    
    
    
    SV1c= float(self.ui.comboBox.currentText())
    SV2c= float(self.ui.comboBox_2.currentText())
    SV3c= float(self.ui.comboBox_3.currentText())
    SV4c= float(self.ui.comboBox_4.currentText())
    
    
    step1 = self.ui.doubleSpinBox_step1.value()
    step2 = self.ui.doubleSpinBox_step2.value()
    step3 = self.ui.doubleSpinBox_step3.value()
    step4 = self.ui.doubleSpinBox_step4.value()
    
    HTini = self.ht.GetHtValue()
    HTini1 = HTini/1000
    self.ui.label_12.setText("{:.2f}".format(HTini1))

    SV1c_index = int(self.ui.comboBox.currentIndex())
    #print("index1",SV1c_index)
    SV2c_index = int(self.ui.comboBox_2.currentIndex())
    #print("index2",SV2c_index)
    SV3c_index = int(self.ui.comboBox_3.currentIndex())
    #print("index3",SV3c_index)
    SV4c_index = int(self.ui.comboBox_4.currentIndex())
    #print("index4",SV4c_index)

 #iniファイルの読み込み（初期値）  
    config = configparser.ConfigParser()
    config.read('config_AutoStepHT2.ini')
   
    HT1 = config.get('HT', 'ht1')
    HT2 = config.get('HT', 'ht2')
    HT3 = config.get('HT', 'ht3')
    HT4 = config.get('HT', 'ht4')
   
    ST2 = config.get('ST', 'st2')
    ST3 = config.get('ST', 'st3')
    ST4 = config.get('ST', 'st4')
    
    SV1c_index = config.get('SV', 'sv1c')
    SV2c_index = config.get('SV', 'sv2c')
    SV3c_index = config.get('SV', 'sv3c')
    SV4c_index = config.get('SV', 'sv4c')
    
    step1 = config.get('step', 'step1')
    step2 = config.get('step', 'step2')
    step3 = config.get('step', 'step3')
    step4 = config.get('step', 'step4')
    
    self.ui.doubleSpinBox_HT1.setProperty("value", HT1) 
    self.ui.doubleSpinBox_HT2.setProperty("value", HT2) 
    self.ui.doubleSpinBox_HT3.setProperty("value", HT3) 
    self.ui.doubleSpinBox_HT4.setProperty("value", HT4)
    
    self.ui.doubleSpinBox_ST2.setProperty("value", ST2)
    self.ui.doubleSpinBox_ST3.setProperty("value", ST3) 
    self.ui.doubleSpinBox_ST4.setProperty("value", ST4) 
    
    self.ui.doubleSpinBox_step1.setProperty("value", step1) 
    self.ui.doubleSpinBox_step2.setProperty("value", step2) 
    self.ui.doubleSpinBox_step3.setProperty("value", step3) 
    self.ui.doubleSpinBox_step4.setProperty("value", step4) 
    
 #iniファイルの読み込み値を書き込む（初期値）  
    
    self.ui.comboBox.setCurrentIndex(int(SV1c_index))
    self.ui.comboBox_2.setCurrentIndex(int(SV2c_index))
    self.ui.comboBox_3.setCurrentIndex(int(SV3c_index))
    self.ui.comboBox_4.setCurrentIndex(int(SV4c_index))

    SV1c= float(self.ui.comboBox.currentText())
    SV2c= float(self.ui.comboBox_2.currentText())
    SV3c= float(self.ui.comboBox_3.currentText())
    SV4c= float(self.ui.comboBox_4.currentText())
    
    #print(SV1c)
    #print(SV2c)
    #print(SV3c)
    #print(SV4c)

    self.ui.doubleSpinBox_step1.setProperty("value", step1) 
    self.ui.doubleSpinBox_step2.setProperty("value", step2) 
    self.ui.doubleSpinBox_step3.setProperty("value", step3) 
    self.ui.doubleSpinBox_step4.setValue(float(step4))
    
    
    
    #self.ui.comboBox_2.setCurrentIndex(2)
    

 #iniファイルの書き出し（初期値）  
   # config = configparser.ConfigParser()

   # config['HT'] = {
   #     'HT1': HT1,
   #     'HT2': HT2,
   #     'HT3': HT3,
   #     'HT4': HT4,
    #}
    #config['ST'] = {
     #   'ST2': ST2,
      #  'ST3': ST3,
       # 'ST4': ST4,
    #}
    #config['SV'] = {
     #   'SV1c': SV1c_index,
      #  'SV2c': SV2c_index,
       # 'SV3c': SV3c_index,
    #      'SV4c': SV4c_index,
   # }
    #config['step'] = {
     #   'step1': step1,
      #  'step2': step2,
       # 'step3': step3,
      #  'step4': step4,
   # }
    #with open('config_AutoStepHT.ini', 'w') as file:
     #   config.write(file)
                
 
  def getsetup(self):
    
    global HT1
    global HT2
    global HT3
    global HT4
    global HT5
    global HT2k
    global HT1k
    global HT3k
    global HT4k
    global HT5k

    global ST2
    global ST3
    global ST4
    
    
    global SV1c
    global SV2c
    global SV3c
    global SV4c
    
    global step1
    global step2
    global step3
    global step4
    
    global stage1
    global stage2
    global stage3
    global stage4
    
    global SV1c_index
    global SV2c_index
    global SV3c_index
    global SV4c_index
    
    
    SV1c= float(self.ui.comboBox.currentText())
    SV2c= float(self.ui.comboBox_2.currentText())
    SV3c= float(self.ui.comboBox_3.currentText())
    SV4c= float(self.ui.comboBox_4.currentText())

    HT1 = self.ui.doubleSpinBox_HT1.value()
    HT2 = self.ui.doubleSpinBox_HT2.value()
    HT3 = self.ui.doubleSpinBox_HT3.value()
    HT4 = self.ui.doubleSpinBox_HT4.value()
    HT5 = self.ui.doubleSpinBox_HT5.value()
    HT1k = HT1 * 1000
    HT2k = HT2 * 1000
    HT3k = HT3 * 1000
    HT4k = HT4 * 1000
    HT5k = HT5 * 1000
    
    #ST1 = self.ui.doubleSpinBox_ST1.value()
    ST2 = self.ui.doubleSpinBox_ST2.value()
    ST3 = self.ui.doubleSpinBox_ST3.value()
    ST4 = self.ui.doubleSpinBox_ST4.value()
    

    
    step1 = self.ui.doubleSpinBox_step1.value()
    step2 = self.ui.doubleSpinBox_step2.value()
    step3 = self.ui.doubleSpinBox_step3.value()
    step4 = self.ui.doubleSpinBox_step4.value()

    stage1 = (((HT2 - HT1)/SV1c)*step1)
    stage2 = ((((HT3 - HT2)/SV2c)*step2)+(ST2*60))
    stage3 = ((((HT4 - HT3)/SV3c)*step3)+(ST3*60))
    stage4 = ((((HT5 - HT4)/SV4c)*step4)+(ST4*60))
    
    stage1s = stage1/60
    stage2s = ((stage2/60) + stage1s) 
    stage3s = ((stage3/60) + stage2s) 
    stage4s = ((stage4/60) + stage3s) 
    
    self.ui.label.setText("{:.1f}".format(stage1s))
    self.ui.label_2.setText("{:.1f}".format(stage2s))
    self.ui.label_3.setText("{:.1f}".format(stage3s))
    self.ui.label_4.setText("{:.1f}".format(stage4s))
    
    HTini = self.ht.GetHtValue()
    HTini1 = HTini/1000
    self.ui.label_12.setText("{:.2f}".format(HTini1))
    
    SV1c_index = int(self.ui.comboBox.currentIndex())
    #print("index1",SV1c_index)
    SV2c_index = int(self.ui.comboBox_2.currentIndex())
    #print("index2",SV2c_index)
    SV3c_index = int(self.ui.comboBox_3.currentIndex())
    #print("index3",SV3c_index)
    SV4c_index = int(self.ui.comboBox_4.currentIndex())
    #print("index4",SV4c_index)
    
 #iniファイルの書き出し（初期値）  
    config = configparser.ConfigParser()

    config['HT'] = {
        'HT1': HT1,
        'HT2': HT2,
        'HT3': HT3,
        'HT4': HT4,
    }
    config['ST'] = {
        'ST2': ST2,
        'ST3': ST3,
        'ST4': ST4,
    }
    config['SV'] = {
        'SV1c': SV1c_index,
        'SV2c': SV2c_index,
        'SV3c': SV3c_index,
        'SV4c': SV4c_index,
    }
    config['step'] = {
        'step1': step1,
        'step2': step2,
        'step3': step3,
        'step4': step4,
    }
    with open('config_AutoStepHT2.ini', 'w') as file:
        config.write(file)
        

  def autoHT1(self):

    if (setstage == 0):

      num = HT1 * 1000
      
      now = datetime.datetime.now()
      #print('{0:%Y/%m/%d-%H:%M:%S}'.format(now))
      self.ui.label_27.setText('{0:%m/%d-%H:%M:%S}'.format(now))
      timeHT1 = stage1
      #print('timeHT1',timeHT1)
      now2 = now + (datetime.timedelta(seconds=1)* timeHT1)
      #print('{0:%Y/%m/%d-%H:%M:%S}'.format(now2))
      self.ui.label_26.setText('{0:%m/%d-%H:%M:%S}'.format(now2))
      
      try :
        while num <= HT2k:
           
          SV1k = SV1c * 1000
          self.ht.SetHtValue(num)
          #sleep(1)
          a = self.ht.GetHtValue()
          a1 = a/1000
          CHT1 = HT2 - HT1
          CHT2 = a1 - HT1
          CHT3 = (CHT2 / CHT1) * 100
          self.ui.label_12.setText("{:.2f}".format(a1))
          self.ui.label_14.setText("Accelarating")
          self.ui.progressBar.setValue(CHT3)
          QApplication.processEvents()
          num += SV1k
          sleep(step1)
      
          
          if a == HT2k:
              self.ui.label_14.setText("Complite")
              break
      except KeyboardInterrupt:      
         self.ui.label_14.setText("Break")
            
       
  #def autoHT2(self):
    elif (setstage == 1):  
      num = HT1 * 1000
      print("stage_HT2")
      now = datetime.datetime.now()
      #print('Start:{0:%Y/%m/%d-%H:%M:%S}'.format(now))
      timeHT2 = stage2
      now2 = now + (datetime.timedelta(seconds=1)* timeHT2)
      #print('Expected End time:{0:%Y/%m/%d-%H:%M:%S}'.format(now2))
      
      while num <= HT2k:
          SV1k = SV1c * 1000
          self.ht.SetHtValue(num)
          #sleep(1)
          a = self.ht.GetHtValue()
          a1 = a/1000
          CHT1 = HT3 - HT1
          CHT2 = a1 - HT1
          CHT3 = (CHT2 / CHT1) * 100
          self.ui.label_12.setText("{:.2f}".format(a1))
          self.ui.label_14.setText("Accelarating")
          self.ui.progressBar.setValue(CHT3)
          QApplication.processEvents()
          num += SV1k
          sleep(step1)
          
          if a == HT2k:
              sleep(ST2*60)
              num2 = HT2 * 1000
              while num2 <= HT3k:
                  SV2k = SV2c * 1000
                  self.ht.SetHtValue(num2)
                  a = self.ht.GetHtValue()
                  a1 = a/1000
                  CHT1 = HT3 - HT1
                  CHT2 = a1 - HT1
                  CHT3 = (CHT2 / CHT1) * 100
                  self.ui.label_12.setText("{:.2f}".format(a1))
                  self.ui.label_14.setText("Accelarating")
                  self.ui.progressBar.setValue(CHT3)
                  QApplication.processEvents()
                  num2 += SV2k
                  sleep(step2)

                  if a == HT3k:

                     self.ui.label_14.setText("Complite")
                     break
 

  #def autoHT3(self):
    elif (setstage == 2):  
      num = HT1 * 1000
      print("stage_HT3")
      now = datetime.datetime.now()
      #print('Start:{0:%Y/%m/%d-%H:%M:%S}'.format(now))
      
      timeHT3 = stage3
      now2 = now + (datetime.timedelta(seconds=1)* timeHT3)
      #print('Expected End time:{0:%Y/%m/%d-%H:%M:%S}'.format(now2))
      
      while num <= HT2k:
          SV1k = SV1c * 1000
          self.ht.SetHtValue(num)
          #sleep(1)
          a = self.ht.GetHtValue()
          a1 = a/1000
          CHT1 = HT4 - HT1
          CHT2 = a1 - HT1
          CHT3 = (CHT2 / CHT1) * 100
 
          self.ui.label_12.setText("{:.2f}".format(a1))
          self.ui.label_14.setText("Accelarating")
          self.ui.progressBar.setValue(CHT3)
          QApplication.processEvents()
          num += SV1k
          sleep(step1)
          
          if a == HT2k:
              sleep(ST2)
              num2 = HT2 * 1000
              while num2 <= HT3k:
                  SV2k = SV2c * 1000
                  self.ht.SetHtValue(num2)
                  #sleep(1)
                  a = self.ht.GetHtValue()
                  a1 = a/1000
                  CHT1 = HT4 - HT1
                  CHT2 = a1 - HT1
                  CHT3 = (CHT2 / CHT1) * 100

                  self.ui.label_12.setText("{:.2f}".format(a1))
                  self.ui.label_14.setText("Accelarating")
                  self.ui.progressBar.setValue(CHT3)
                  QApplication.processEvents()
                  num2 += SV2k
                  sleep(step2)

                  
                  if a == HT3k:
                      sleep(ST3)
                      num3 = HT3 * 1000
                      while num3 <= HT4k:
                          SV3k = SV3c * 1000
                          self.ht.SetHtValue(num3)
                          #sleep(1)
                          a = self.ht.GetHtValue()
                          a1 = a/1000
                          CHT1 = HT4 - HT1
                          CHT2 = a1 - HT1
                          CHT3 = (CHT2 / CHT1) * 100

                          self.ui.label_12.setText("{:.2f}".format(a1))
                          self.ui.label_14.setText("Accelarating")
                          self.ui.progressBar.setValue(CHT3)
                          QApplication.processEvents()
                          num3 += SV3k
                          sleep(step3)

                          if a == HT4k:
                             self.ui.label_14.setText("Complite")
                             break

  #def autoHT4(self):
    elif (setstage ==4) :
      num = HT1 * 1000
      print("stage4")
      now = datetime.datetime.now()
      #print('Start:{0:%Y/%m/%d-%H:%M:%S}'.format(now))
      timeHT4 = stage4
      now2 = now + (datetime.timedelta(seconds=1)* timeHT4)
      #print('Expected End time:{0:%Y/%m/%d-%H:%M:%S}'.format(now2))
      
      while num <= HT2k:
          SV1k = SV1c * 1000
          self.ht.SetHtValue(num)
          #sleep(1)
          a = self.ht.GetHtValue()
          num += SV1k
          sleep(step1)
          
          if a == HT2k:
              sleep(ST2)
              num2 = HT2 * 1000
              while num2 <= HT3k:
                  SV2k = SV2c * 1000
                  self.ht.SetHtValue(num2)
                  #sleep(1)
                  a = self.ht.GetHtValue()
                  a1 = a/1000
                  CHT1 = HT5 - HT1
                  CHT2 = a1 - HT1
                  CHT3 = (CHT2 / CHT1) * 100

                  self.ui.label_12.setText("{:.2f}".format(a1))
                  self.ui.label_14.setText("Accelarating")
                  self.ui.progressBar.setValue(CHT3)
                  QApplication.processEvents()
                  num2 += SV2k
                  sleep(step2)
                  
                  if a == HT3k:
                      sleep(ST3)
                      num3 = HT3 * 1000
                      while num3 <= HT4k:
                          SV3k = SV3c * 1000
                          self.ht.SetHtValue(num3)
                          #sleep(1)
                          a = self.ht.GetHtValue()
                          a1 = a/1000
                          CHT1 = HT5 - HT1
                          CHT2 = a1 - HT1
                          CHT3 = (CHT2 / CHT1) * 100

                          self.ui.label_12.setText("{:.2f}".format(a1))
                          self.ui.label_14.setText("Accelarating")
                          self.ui.progressBar.setValue(CHT3)
                          QApplication.processEvents()
                          num3 += SV3k
                          sleep(step3)
                          
                          if a == HT4k:
                              sleep(ST4)
                              num4 = HT4 * 1000
                              while num4 <= HT5k:
                                  SV4k = SV4c * 1000
                                  self.ht.SetHtValue(num4)
                                  #sleep(1)
                                  a = self.ht.GetHtValue()
                                  a1 = a/1000
                                  CHT1 = HT5 - HT1
                                  CHT2 = a1 - HT1
                                  CHT3 = (CHT2 / CHT1) * 100

                                  self.ui.label_12.setText("{:.2f}".format(a1))
                                  self.ui.label_14.setText("Accelarating")
                                  self.ui.progressBar.setValue(CHT3)
                                  QApplication.processEvents()
                                  num4 += SV4k
                                  sleep(step4)

                                  if a == HT5k:
                                      self.ui.label_14.setText("Complite")
                                      break
  def autoHT2(self):
      print("2")
  def autoHT3(self):
      print("3")
  def autoHT4(self):  
      print("4")      

  def save(self):

 #iniファイルの書き出し（初期値）  
    config = configparser.ConfigParser()

    config['HT'] = {
        'HT1': HT1,
        'HT2': HT2,
        'HT3': HT3,
        'HT4': HT4,
    }
    config['ST'] = {
        'ST2': ST2,
        'ST3': ST3,
        'ST4': ST4,
    }
    config['SV'] = {
        'SV1c': SV1c_index,
        'SV2c': SV2c_index,
        'SV3c': SV3c_index,
        'SV4c': SV4c_index,
    }
    config['step'] = {
        'step1': step1,
        'step2': step2,
        'step3': step3,
        'step4': step4,
    }
    with open('config_AutoStepHT2.ini', 'w') as file:
        config.write(file)

#GUIの表示の切り替え        
  def setstage(self):
        setstage = self.ui.comboBox_13.currentIndex()
        print(setstage)

        if (setstage == 0):
          self.ui.label_19.hide()
          self.ui.label_9.hide()
          self.ui.label_2.hide()
          self.ui.label_18.hide()
          self.ui.label_44.hide()

          self.ui.doubleSpinBox_ST2.hide()
          self.ui.doubleSpinBox_step2.hide()
          self.ui.doubleSpinBox_HT3.hide()

          self.ui.comboBox_2.hide()

          self.ui.label_10.hide()
          self.ui.label_21.hide()
          self.ui.label_45.hide()
          self.ui.label_20.hide()
          self.ui.label_3.hide()

          self.ui.doubleSpinBox_ST3.hide()
          self.ui.doubleSpinBox_step3.hide()
          self.ui.doubleSpinBox_HT4.hide()

          self.ui.comboBox_3.hide()

          self.ui.label_11.hide()
          self.ui.label_22.hide()
          self.ui.label_23.hide()
          self.ui.label_46.hide()
          self.ui.label_4.hide()

          self.ui.doubleSpinBox_ST4.hide()
          self.ui.doubleSpinBox_step4.hide()
          self.ui.doubleSpinBox_HT5.hide()

          self.ui.comboBox_4.hide()

          self.ui.groupBox_3.resize(111, 131)
          self.ui.groupBox_4.resize(91, 131)
          self.ui.groupBox_5.resize(81, 131)

          self.ui.groupBox.resize(311, 271) 

          self.ui.groupBox_6.setGeometry(5,270, 311, 131) #progress window

          self.ui.toolButton_3.setGeometry(10, 410, 81, 31) #close
          self.ui.pushButton_6.setGeometry(230, 410, 81, 31) #save 

          self.resize(322,450) # window
  
        elif (setstage == 1):
          self.ui.label_19.show()
          self.ui.label_9.show()
          self.ui.label_2.show()
          self.ui.label_18.show()
          self.ui.label_44.show()
  
          self.ui.doubleSpinBox_ST2.show()
          self.ui.doubleSpinBox_step2.show()
          self.ui.doubleSpinBox_HT3.show()
  
          self.ui.comboBox_2.show()
  
          self.ui.label_10.hide()
          self.ui.label_21.hide()
          self.ui.label_45.hide()
          self.ui.label_20.hide()
          self.ui.label_3.hide()
  
          self.ui.doubleSpinBox_ST3.hide()
          self.ui.doubleSpinBox_step3.hide()
          self.ui.doubleSpinBox_HT4.hide()
  
          self.ui.comboBox_3.hide()
  
          self.ui.label_11.hide()
          self.ui.label_22.hide()
          self.ui.label_23.hide()
          self.ui.label_46.hide()
          self.ui.label_4.hide()
  
          self.ui.doubleSpinBox_ST4.hide()
          self.ui.doubleSpinBox_step4.hide()
          self.ui.doubleSpinBox_HT5.hide()
  
          self.ui.comboBox_4.hide()
  
          self.ui.groupBox_3.resize(111, 211)
          self.ui.groupBox_4.resize(91, 211)
          self.ui.groupBox_5.resize(81, 211)
  
          self.ui.groupBox.resize(311, 351) 
  
          self.ui.groupBox_6.setGeometry(5,350, 311, 131) #progress window
  
          self.ui.toolButton_3.setGeometry(10, 490, 81, 31) #close
          self.ui.pushButton_6.setGeometry(230, 490, 81, 31) #save 
  
          self.resize(322,530) # window

        elif (setstage == 2):
          self.ui.label_19.show()
          self.ui.label_9.show()
          self.ui.label_2.show()
          self.ui.label_18.show()
          self.ui.label_44.show()
  
          self.ui.doubleSpinBox_ST2.show()
          self.ui.doubleSpinBox_step2.show()
          self.ui.doubleSpinBox_HT3.show()
  
          self.ui.comboBox_2.show()
  
          self.ui.label_10.show()
          self.ui.label_21.show()
          self.ui.label_45.show()
          self.ui.label_20.show()
          self.ui.label_3.show()
  
          self.ui.doubleSpinBox_ST3.show()
          self.ui.doubleSpinBox_step3.show()
          self.ui.doubleSpinBox_HT4.show()
  
          self.ui.comboBox_3.show()
  
          self.ui.label_11.hide()
          self.ui.label_22.hide()
          self.ui.label_23.hide()
          self.ui.label_46.hide()
          self.ui.label_4.hide()
  
          self.ui.doubleSpinBox_ST4.hide()
          self.ui.doubleSpinBox_step4.hide()
          self.ui.doubleSpinBox_HT5.hide()
  
          self.ui.comboBox_4.hide()
  
          self.ui.groupBox_3.resize(111, 291)
          self.ui.groupBox_4.resize(91, 291)
          self.ui.groupBox_5.resize(81, 291)
  
          self.ui.groupBox.resize(311, 431) 
  
          self.ui.groupBox_6.setGeometry(5,430, 311, 131) #progress window
  
          self.ui.toolButton_3.setGeometry(10, 570, 81, 31) #close
          self.ui.pushButton_6.setGeometry(230, 570, 81, 31) #save 
  
          self.resize(322,610) # window
  
        elif (setstage == 3):
          self.ui.label_19.show()
          self.ui.label_9.show()
          self.ui.label_2.show()
          self.ui.label_18.show()
          self.ui.label_44.show()
  
          self.ui.doubleSpinBox_ST2.show()
          self.ui.doubleSpinBox_step2.show()
          self.ui.doubleSpinBox_HT3.show()
  
          self.ui.comboBox_2.show()
  
          self.ui.label_10.show()
          self.ui.label_21.show()
          self.ui.label_45.show()
          self.ui.label_20.show()
          self.ui.label_3.show()
  
          self.ui.doubleSpinBox_ST3.show()
          self.ui.doubleSpinBox_step3.show()
          self.ui.doubleSpinBox_HT4.show()
  
          self.ui.comboBox_3.show()
  
          self.ui.label_11.show()
          self.ui.label_22.show()
          self.ui.label_23.show()
          self.ui.label_46.show()
          self.ui.label_4.show()
  
          self.ui.doubleSpinBox_ST4.show()
          self.ui.doubleSpinBox_step4.show()
          self.ui.doubleSpinBox_HT5.show()
  
          self.ui.comboBox_4.show()
  
          self.ui.groupBox_3.resize(111, 371)
          self.ui.groupBox_4.resize(91, 371)
          self.ui.groupBox_5.resize(81, 371)
  
          self.ui.groupBox.resize(311, 511) 
  
          self.ui.groupBox_6.setGeometry(5,510, 311, 131) #progress window
  
          self.ui.toolButton_3.setGeometry(10, 650, 81, 31) #close
          self.ui.pushButton_6.setGeometry(230, 650, 81, 31) #save 
  
          self.resize(322,690) # window


    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())        
     
         