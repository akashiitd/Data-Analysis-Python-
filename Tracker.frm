VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Tracker 
   Caption         =   "U.I "
   ClientHeight    =   8190
   ClientLeft      =   45
   ClientTop       =   375
   ClientWidth     =   11595
   OleObjectBlob   =   "Tracker.frx":0000
   ShowModal       =   0   'False
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Tracker"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Option Explicit
Private Declare Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long)

Public autECLSession As Object
Public autECLPS As Object
Public autECLOIA As Object




Private Sub CommandButton1_Click()
      Set autECLSession = CreateObject("pcomm.auteclsession")
        Set autECLPS = CreateObject("Pcomm.auteclps")
        Set autECLOIA = CreateObject("Pcomm.autecloia")
        Workbooks("Data.xlsx").Sheets("DataSheet").Activate

        'Session Creation
        lr_data = Range("A" & Rows.Count).End(xlUp).Row
        
            For i = 2 To lr_data
                    autECLSession.SetConnectionByName (SessionBox.Value)
            
                    autECLSession.autECLPS.SetCursorPos 22, 54
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLPS.SetCursorPos 14, 21
                    autECLSession.autECLPS.SendKeys Cells(i, 1)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 15, 21
                    autECLSession.autECLPS.SendKeys Cells(i, 2)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 16, 21
                    autECLSession.autECLPS.SendKeys Cells(i, 3)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 18, 6
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 18, 6
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
        
                    autECLSession.autECLPS.SetCursorPos 8, 28
                    autECLSession.autECLPS.SendKeys Cells(i, 4)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                   
                    autECLSession.autECLPS.SetCursorPos 9, 28
                    autECLSession.autECLPS.SendKeys Cells(i, 5)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 13, 29
                    autECLSession.autECLPS.SendKeys Cells(i, 6)
                    autECLSession.autECLPS.SetCursorPos 13, 38
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    autECLSession.autECLPS.SetCursorPos 13, 70
                    autECLSession.autECLPS.SendKeys Cells(i, 6)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 13, 80
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    autECLSession.autECLPS.SetCursorPos 13, 79
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    
                    
                    autECLSession.autECLPS.SetCursorPos 20, 26
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 21, 26
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 21, 55
                    autECLSession.autECLPS.SendKeys Cells(i, 7)
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
'                    autECLSession.autECLPS.SetCursorPos 21, 33
'                    autECLSession.autECLPS.SendKeys " "
'                    autECLSession.autECLOIA.WaitForInputReady
'                    Call Sleep(500)
'
                    autECLSession.autECLPS.SetCursorPos 22, 54
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 23, 15
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 7, 9
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 20, 24
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 22, 67
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
             Next i
                    
                    
End Sub

Private Sub Submit_Click()
    Set autECLSession = CreateObject("pcomm.auteclsession")
        Set autECLPS = CreateObject("Pcomm.auteclps")
        Set autECLOIA = CreateObject("Pcomm.autecloia")
        
        'Session Creation
        
                    autECLSession.SetConnectionByName (SessionBox.Value)
            
                    autECLSession.autECLPS.SetCursorPos 22, 54
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLPS.SetCursorPos 14, 21
                    autECLSession.autECLPS.SendKeys GBUTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 15, 21
                    autECLSession.autECLPS.SendKeys GROUPTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 16, 21
                    autECLSession.autECLPS.SendKeys TTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 18, 6
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 18, 6
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
        
                    autECLSession.autECLPS.SetCursorPos 8, 28
                    autECLSession.autECLPS.SendKeys FACILITYTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                   
                    autECLSession.autECLPS.SetCursorPos 9, 28
                    autECLSession.autECLPS.SendKeys CONTRACTTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 13, 29
                    autECLSession.autECLPS.SendKeys SIGNEDTEXT
                    autECLSession.autECLPS.SetCursorPos 13, 38
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    autECLSession.autECLPS.SetCursorPos 13, 70
                    autECLSession.autECLPS.SendKeys SIGNEDTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 13, 80
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    autECLSession.autECLPS.SetCursorPos 13, 79
                    autECLSession.autECLPS.SendKeys "[backspace]"
                    
                    
                    autECLSession.autECLPS.SetCursorPos 20, 26
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    autECLSession.autECLPS.SetCursorPos 21, 26
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 21, 55
                    autECLSession.autECLPS.SendKeys ITEMTEXT
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
'                    autECLSession.autECLPS.SetCursorPos 21, 33
'                    autECLSession.autECLPS.SendKeys " "
'                    autECLSession.autECLOIA.WaitForInputReady
'                    Call Sleep(500)
'
                    autECLSession.autECLPS.SetCursorPos 22, 54
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 23, 15
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    autECLSession.autECLPS.SetCursorPos 7, 9
                    autECLSession.autECLPS.SendKeys " "
                    autECLSession.autECLOIA.WaitForInputReady
                    Call Sleep(500)
                    
                    
                    
                    
                        
End Sub

Private Sub UserForm_Click()

End Sub

Private Sub UserForm_Initialize()
    
  'text box
    
    GBUTEXT.Value = ""
    GROUPTEXT.Value = ""
    TTEXT.Value = ""
    FACILITYTEXT = ""
    CONTRACTTEXT = ""
    SIGNEDTEXT = ""
    ITEMTEXT = ""
    
  'Session BOX
  
  SessionBox.clear


    With SessionBox
        .AddItem "A"
        .AddItem "B"
        .AddItem "C"
        .AddItem "D"
        .AddItem "E"
        
    End With
    
End Sub
