import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Tere tulemast meie ajaarvutusprogrammi!')],
            [sg.Text('Et programmiga jätkata, vajuta Jätka. Et lahkuda, vajuta Lõpeta.')],
            [sg.Button('Jätka'), sg.Button('Lõpeta')] ]

# Create the Window
window = sg.Window('w0k3', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Lõpeta'):   # if user closes window or clicks cancel
        break
        window.close()
    if event in ("Jätka"):
        window.close()
        layout = [  [sg.Text('Vali, kas praegu on hommik, lõuna või õhtu.')],
                    [sg.Radio('Hommik', key= 1, group_id= "grp"), sg.Radio('Lõuna', key = 2, group_id= "grp"), sg.Radio("Õhtu", key = 3, group_id= "grp")],
                    [sg.Button('Jätka'), sg.Button('Lõpeta')] ]
        window = sg.Window('wok3', layout)
        event = window.read()

        event, values = window.read()
        if event in (None, "Lõpeta"):
            break
        else:
           if event in ("Jätka"):
               
                


            

        











# variandid = ["hommik", "lõuna", "õhtu"]
# vajutati = easygui.choicebox("Mis aeg päevast praegu on?", choices = variandid)
# kell = easygui.enterbox("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis tunnid:minutid): ")

# if vajutati == "hommik":
#     a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele? ", lowerbound = 0, upperbound = 10000)
#     b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada duši all käimisele? ", lowerbound = 0, upperbound = 10000)
#     c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada hammaste pesemisele? ", lowerbound = 0, upperbound = 10000)
#     d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)? ", lowerbound = 0, upperbound = 10000)
#     e = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada hommikusöögile? ", lowerbound = 0, upperbound = 10000)
#     f = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele? ", lowerbound = 0, upperbound = 10000)
#     h = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada riietumisele? ", lowerbound = 0, upperbound = 10000)
#     i = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada meikimisele? ", lowerbound = 0, upperbound = 10000)
#     j = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada koti pakkimisele? ", lowerbound = 0, upperbound = 10000)
#     k = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada kohale jõudmisele? ", lowerbound = 0, upperbound = 10000)
#     l = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ", lowerbound = 0, upperbound = 10000)
#     summa = a + b + c + e + d + f + h + i + j + k + l
#     tunnid = summa // 60
#     minutid = summa - (tunnid * 60)
#     oigekell = kell.split(":")
#     valjatund = int(oigekell[0]) - tunnid
#     valjaminutid = int(oigekell[1]) - minutid
#     if valjatund < 0:
#         valjatund = 24 - abs(valjatund)
#     if valjaminutid < 0:
#         valjatund = valjatund - 1
#         valjaminutid = abs(valjaminutid)
    
        
    
#     easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
#             "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
# if vajutati == "lõuna":
#     a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada lõunasöögile? ", lowerbound = 0, upperbound = 10000)
#     b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada koristamisele? ", lowerbound = 0, upperbound = 10000)
#     c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada sarja vaatamisele? ", lowerbound = 0, upperbound = 10000)
#     d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada enda korrastamisele? ", lowerbound = 0, upperbound = 10000) 
#     e = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa koti kokku pakkimisele? ", lowerbound = 0, upperbound = 10000)
#     f = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa kohale jõudmisele? ", lowerbound = 0, upperbound = 10000)
#     h = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ", lowerbound = 0, upperbound = 10000)
#     summa = a + b + c + d + e + f + h
#     tunnid = summa // 60
#     minutid = summa - (tunnid * 60)
#     oigekell = kell.split(":")
#     valjatund = int(oigekell[0]) - tunnid
#     valjaminutid = int(oigekell[1]) - minutid
#     if valjatund < 0:
#         valjatund = 24 - abs(valjatund)
#     if valjaminutid < 0:
#         valjatund = valjatund - 1
#         valjaminutid = abs(valjaminutid)
    
#     easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
#             "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
# if vajutati == "õhtu":
#     a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada pesemisele?", lowerbound = 0, upperbound = 10000)
#     b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada õhtusöögile? ",lowerbound = 0, upperbound = 10000)
#     c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada meigile? " , lowerbound = 0, upperbound = 10000)
#     d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada riietumisele? " , lowerbound = 0, upperbound = 10000)
#     e = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada soojendamisele? " , lowerbound = 0, upperbound = 10000)
#     f = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa kohale jõudmisele? " , lowerbound = 0, upperbound = 10000)
#     h = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? " ,lowerbound = 0, upperbound = 10000)
#     summa = a + b + c + e + d + f + h
#     tunnid = summa // 60
#     minutid = summa - (tunnid * 60)
#     oigekell = kell.split(":")
#     valjatund = int(oigekell[0]) - tunnid
#     valjaminutid = int(oigekell[1]) - minutid
#     if valjatund < 0:
#         valjatund = 24 - abs(valjatund)
#     if valjaminutid < 0:
#         valjatund = valjatund - 1
#         valjaminutid = abs(valjaminutid)
    
#     easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
#             "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
    