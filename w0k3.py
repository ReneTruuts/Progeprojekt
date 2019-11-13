import easygui

g = input("Kas praegu on hommik, lõuna või õhtu: ")
kell = input("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis tunnid:minutid): ")

if g.lower() == "hommik":
    a = int(input("Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele? "))
    b = int(input("Palju aega (minutites) planeerid sa kulutada duši all käimisele? "))
    c = int(input("Palju aega (minutites) planeerid sa kulutada hammaste pesemisele? "))
    d = int(input("Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)? "))
    e = int(input("Palju aega (minutites) planeerid sa kulutada hommikusöögile? "))
    f = int(input("Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele? "))
    h = int(input("Palju aega (minutites) planeerid sa kulutada riietumisele? "))
    i = int(input("Palju aega (minutites) planeerid sa kulutada meikimisele? "))
    j = int(input("Palju aega (minutites) planeerid sa kulutada koti pakkimisele? "))
    k = int(input("Palju aega (minutites) planeerid sa kulutada kohale jõudmisele? "))
    l = int(input("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? "))
    summa = a + b + c + e + d + f + h + i + j + k + l
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = abs(tunnid- int(oigekell[0]))
    valjaminutid = abs(minutid - int(oigekell[1]))

    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
if g.lower() == "lõuna":
    a = int(input("Palju aega (minutites) planeerid sa kulutada lõunasöögile? "))
    b = int(input("Palju aega (minutites) planeerid sa kulutada koristamisele? "))
    c = int(input("Palju aega (minutites) planeerid sa kulutada sarja vaatamisele? "))
    d = int(input("Palju aega (minutites) planeerid sa kulutada enda korrastamisele? "))
    e = int(input("Palju aega (minutites) kulutad sa koti kokku pakkimisele? "))
    f = int(input("Palju aega (minutites) kulutad sa kohale jõudmisele? "))
    h = int(input("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? "))
    summa = a + b + c + d + e + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = abs(tunnid- int(oigekell[0]))
    valjaminutid = abs(minutid - int(oigekell[1]))

    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    




if g.lower() == "õhtu":
    a = int(input("Palju aega (minutites) planeerid sa kulutada pesemisele? "))
    b = int(input("Palju aega (minutites) planeerid sa kulutada õhtusöögile? "))
    c = int(input("Palju aega (minutites) planeerid sa kulutada meigile? "))
    d = int(input("Palju aega (minutites) planeerid sa kulutada riietumisele? "))
    e = int(input("Palju aega (minutites) planeerid sa kulutada soojendamisele? "))
    f = int(input("Palju aega (minutites) kulutad sa kohale jõudmisele? "))
    h = int(input("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? "))
    summa = a + b + c + e + d + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = abs(tunnid- int(oigekell[0]))
    valjaminutid = abs(minutid - int(oigekell[1]))

    easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
    