g = input("Kas praegu on hommik, päev või õhtu: ")
kell = input("Sisesta kellaaeg, mil sa kuskil olema pead: ")
if g.lower() == "hommik":
    a = int(input("Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele?"))
    b = int(input("Palju aega (minutites) planeerid sa kulutada duši all käimisele?"))
    c = int(input("Palju aega (minutites) planeerid sa kulutada hammaste pesemisele?"))
    d = int(input("Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)?"))
    e = int(input("Palju aega (minutites) planeerid sa kulutada hommikusöögile?"))
    f = int(input("Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele?"))
    g = int(input("Palju aega (minutites) planeerid sa kulutada riietumisele?"))
    h = int(input("Palju aega (minutites) planeerid sa kulutada meikimisele?"))
    i = int(input("Palju aega (minutites) planeerid sa kulutada koti pakkimisele?"))
    j = int(input("Palju aega (minutites) planeerid sa kulutada kohale jõudmisele?"))
    k = int(input("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud?"))
    
    
    
    
    
if g.lower() == "päev":
    a = int(input("Palju aega (minutites) planeerid sa kulutada lõunasöögile?"))
    b = int(input("Palju aega (minutites) planeerid sa kulutada sarja vaatamisele?"))
    c = int(input("Palju aega (minutites) planeerid sa kulutada koristamisele?"))
    d = int(input("Palju aega (minutites) planeerid sa kulutada enda korrastamisele?"))
    e = int(input("Palju aega (minutites) kulutad sa koti kokku pakkimisele?"))
    f = int(input("Palju aega (minutites) kulutad sa kohalejõudmisele?"))
    summa = a + b + c + e + d + f
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    print("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit.")
    




if g.lower() == "õhtu":
    a = input("Palju aega (minutites) planeerid sa kulutada pesemisele?")
    b = input("Palju aega (minutites) planeerid sa kulutada õhtusöögile?")
    c = input("Palju aega (minutites) planeerid sa kulutada meigile?")
    d = input("Palju aega (minutites) planeerid sa kulutada riietumisele?")
    e = input("Palju aega (minutites) planeerid sa kulutada soojendamisele?")
    f = input("Palju aega (minutites) kulutad sa kohalejõudmisele?")
    
    
    