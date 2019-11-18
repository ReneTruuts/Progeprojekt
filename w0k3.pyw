import easygui

variandid = ["hommik", "lõuna", "õhtu"]
vajutati = easygui.choicebox("Mis aeg päevast praegu on?", choices = variandid)
kell = easygui.enterbox("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis tunnid:minutid): ")

if vajutati == "hommik":
    a = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele? ")
    b = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada duši all käimisele? ")
    c = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada hammaste pesemisele? ")
    d = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)? ")
    e = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada hommikusöögile? ")
    f = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele? ")
    h = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada riietumisele? ")
    i = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada meikimisele? ")
    j = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada koti pakkimisele? ")
    k = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada kohale jõudmisele? ")
    l = easygui.integerbox("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
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
        valjaminutid = abs(valjaminutid)
    
        
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
if vajutati == "lõuna":
    a = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada lõunasöögile? ")
    b = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada koristamisele? ")
    c = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada sarja vaatamisele? ")
    d = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada enda korrastamisele? ")
    e = easygui.integerbox("Palju aega (minutites) kulutad sa koti kokku pakkimisele? ")
    f = easygui.integerbox("Palju aega (minutites) kulutad sa kohale jõudmisele? ")
    h = easygui.integerbox("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
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
        valjaminutid = abs(valjaminutid)
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
if vajutati == "õhtu":
    a = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada pesemisele? ")
    b = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada õhtusöögile? ")
    c = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada meigile? ")
    d = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada riietumisele? ")
    e = easygui.integerbox("Palju aega (minutites) planeerid sa kulutada soojendamisele? ")
    f = easygui.integerbox("Palju aega (minutites) kulutad sa kohale jõudmisele? ")
    h = easygui.integerbox("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
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
        valjaminutid = abs(valjaminutid)
    
    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
    