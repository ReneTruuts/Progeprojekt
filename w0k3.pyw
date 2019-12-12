import easygui

pilt = "kell.gif"
variandid = ["Edasi", "Sulge programm"]
vajutati = easygui.buttonbox("                            Mida soovid programmiga teha?", choices = variandid, image = pilt)
if vajutati == "Edasi":

    eesmärk = ["Mis kell alustada tegevustega?", "Kuidas oma tegevusi uuesti planeerida?"]
    valiti = easygui.choicebox("Kas tahad, et programm ütleks sulle, ", choices = eesmärk)

    if valiti == "Mis kell alustada tegevustega?":

        variandid = ["hommik", "lõuna", "õhtu"]
        vajutati = easygui.choicebox("Mis aeg päevast praegu on?", choices = variandid)
        kell = easygui.enterbox("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis hh:mm): ")
        fail = open('andmed.txt', 'w')

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

            fail.write(str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(e) + "\n" + str(d) + "\n" + str(f) + "\n" + str(h) + "\n" 
                        + str(i) + "\n" + str(j) + "\n" + str(k) + "\n" + str(l))
            fail.close()

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
            if valjaminutid < 10:
                valjaminutid = str('0') + str(valjaminutid)
            
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

            fail.write(str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(e) + "\n" + str(d) + "\n" + str(f) + "\n" + str(h))
            fail.close()

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
            if valjaminutid < 10:
                valjaminutid = str('0') + str(valjaminutid)
            
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

            fail.write(str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(e) + "\n" + str(d) + "\n" + str(f) + "\n" + str(h))
            fail.close()

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
            if valjaminutid < 10:
                valjaminutid = str('0') + str(valjaminutid)
            
            easygui.msgbox(("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
                    "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))

    elif valiti == "Kuidas oma tegevusi uuesti planeerida?":

        variandid = ["hommik", "lõuna", "õhtu"]
        vajutati = easygui.choicebox("Mis aeg päevast praegu on?", choices = variandid)
        hiljaks = easygui.enterbox("Sisesta, kui palju sa sisse magasid (formaadis hh:mm): ")
        hiljaks_järjend = hiljaks.split(':')
        hiljaks_formaadis = int(hiljaks_järjend[0])*60 + int(hiljaks_järjend[1])

        fail = open("andmed.txt", 'r')
        ajakulu = 0
        for rida in fail:
            ajakulu += int(rida.strip())
        fail.close()

        if vajutati == "hommik":
            
            tegevused = ['voodist püsti tõusmisele', 'duši all käimisele', 'hammaste pesemisele', 'muule kehahooldusele', 'hommikusöögile',
                         'nõude pesemisele/muudele koristustegevustele', 'riietumisele', 'meikimisele', 'koti pakkimisele',
                         'kohale jõudmisele', 'tegevustele, mida me Sinu käest ei küsinud']
                         
            tegur = round(float(hiljaks_formaadis / ajakulu), 1)
            n = 0
            kogu_tekst = str()
            fail = open("andmed.txt", 'r')
            for rida in fail:
                if int(rida) != 0:
                    uus_aeg = int(rida) * tegur
                    tekst = str(tegevused[n].capitalize() + ' võid kulutada nüüd ' + str(uus_aeg) + ' minutit.' + '\n')
                    kogu_tekst += tekst
                n += 1
            fail.close()
            easygui.msgbox(kogu_tekst)
        
        if vajutati == "lõuna":
            
            tegevused = ['lõunasöögile', 'koristamisele', 'sarja vaatamisele', 'enda korrastamisele', 'koti pakkimisele', 'kohale jõudmisele', 
                         'tegevustele, mida me Sinu käest ei küsinud']
                         
            tegur = round(float(hiljaks_formaadis / ajakulu), 1)
            n = 0
            kogu_tekst = str()
            fail = open("andmed.txt", 'r')
            for rida in fail:
                if int(rida) != 0:
                    uus_aeg = int(rida) * tegur
                    tekst = str(tegevused[n].capitalize() + ' võid kulutada nüüd ' + str(uus_aeg) + ' minutit.' + '\n')
                    kogu_tekst += tekst
                n += 1
            fail.close
            easygui.msgbox(kogu_tekst)

        if vajutati == "õhtu":
            
            tegevused = ['pesemisele', 'õhtusöögile', 'meigile', 'riietumisele', 'soojendamisele', 'kohale jõudmisele',
                         'tegevustele, mida me Sinu käest ei küsinud']
                         
            tegur = round(float(hiljaks_formaadis / ajakulu), 1)
            n = 0
            kogu_tekst = str()
            fail = open("andmed.txt", 'r')
            for rida in fail:
                if int(rida) != 0:
                    uus_aeg = int(rida) * tegur
                    tekst = str(tegevused[n].capitalize() + ' võid kulutada nüüd ' + str(uus_aeg) + ' minutit.' + '\n')
                    kogu_tekst += tekst
                n += 1
            fail.close
            easygui.msgbox(kogu_tekst)

if vajutati == "Sulge programm":
    exit   
    
