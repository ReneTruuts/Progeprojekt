import easygui

variandid = ["hommik", "lõuna", "õhtu"]
vajutati = easygui.choicebox("Mis aeg päevast praegu on?", choices = variandid)
kell = easygui.enterbox("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis tunnid:minutid): ")

if vajutati == "hommik":
    a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele? ", lowerbound = 0, upperbound = 10000)
    b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada duši all käimisele? ", lowerbound = 0, upperbound = 10000)
    c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada hammaste pesemisele? ", lowerbound = 0, upperbound = 10000)
    d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)? ", lowerbound = 0, upperbound = 10000)
    e = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada hommikusöögile? ", lowerbound = 0, upperbound = 10000)
    f = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele? ", lowerbound = 0, upperbound = 10000)
    h = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada riietumisele? ", lowerbound = 0, upperbound = 10000)
    i = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada meikimisele? ", lowerbound = 0, upperbound = 10000)
    j = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada koti pakkimisele? ", lowerbound = 0, upperbound = 10000)
    k = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada kohale jõudmisele? ", lowerbound = 0, upperbound = 10000)
    l = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ", lowerbound = 0, upperbound = 10000)
    summa = a + b + c + e + d + f + h + i + j + k + l
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = 60 + valjaminutid
    if valjaminutid == 0:
        valjaminutid = str('00')
    
        
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
if vajutati == "lõuna":
    a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada lõunasöögile? ", lowerbound = 0, upperbound = 10000)
    b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada koristamisele? ", lowerbound = 0, upperbound = 10000)
    c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada sarja vaatamisele? ", lowerbound = 0, upperbound = 10000)
    d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada enda korrastamisele? ", lowerbound = 0, upperbound = 10000) 
    e = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa koti kokku pakkimisele? ", lowerbound = 0, upperbound = 10000)
    f = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa kohale jõudmisele? ", lowerbound = 0, upperbound = 10000)
    h = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ", lowerbound = 0, upperbound = 10000)
    summa = a + b + c + d + e + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = 60 + valjaminutid
    if valjaminutid == 0:
        valjaminutid = str('00')
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
if vajutati == "õhtu":
    a = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada pesemisele?", lowerbound = 0, upperbound = 10000)
    b = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada õhtusöögile? ",lowerbound = 0, upperbound = 10000)
    c = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada meigile? " , lowerbound = 0, upperbound = 10000)
    d = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada riietumisele? " , lowerbound = 0, upperbound = 10000)
    e = easygui.integerbox(msg = "Palju aega (minutites) planeerid sa kulutada soojendamisele? " , lowerbound = 0, upperbound = 10000)
    f = easygui.integerbox(msg = "Palju aega (minutites) kulutad sa kohale jõudmisele? " , lowerbound = 0, upperbound = 10000)
    h = easygui.integerbox(msg = "Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? " ,lowerbound = 0, upperbound = 10000)
    summa = a + b + c + e + d + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = 60 + valjaminutid
    if valjaminutid == 0:
        valjaminutid = str('00')
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
    