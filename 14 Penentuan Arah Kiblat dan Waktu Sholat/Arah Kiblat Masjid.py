print('+++++=========================================+++++')
print('---Metode 1&2 Abu al-Wafa Menentukan Arah Kiblat---')
print('--------------Sumedang, Jawa Barat-----------------')
print('----------Data Koordinat oleh Google Maps----------')
print('-----------+ Oleh: Fillah Alamsyah +---------------')
print('+++++=========================================+++++')

from math import*

#Data Koordinat berdasarkan Google Maps
#Kiblat
# -6.9082948058959674, 107.8090111589681
#Lintang Lokasi
LL = -6.9082948058959674
Cos_LL = cos(radians(LL))
Sin_LL = sin(radians(LL))
K_LL = 90-LL
print("Lintang Lokasi =" , LL)


#Bujur Lokasi
BL = 107.8090111589681
Cos_BL = cos(radians(BL))
Sin_BL = sin(radians(BL))
print("Bujur Lokasi =" , BL)

#Lintang Mekkah
LM = 21.422558
Cos_LM = cos(radians(LM))
Sin_LM = sin(radians(LM))
print("Lintang Mekkah =" , LM)
#Komplemen Lintang Mekkah
K_LM = 90 - LM
Sin_K_LM = sin(radians(K_LM))

#Bujur Mekkah
BM = 39.826128
Cos_BM = cos(radians(BM))
Sin_BM = sin(radians(BM))
print("Bujur Mekkah =" , BM)

print('+++++=========================================+++++')

#Menentukan selisih bujur lokasi dan bujur Mekkah
BLM = BL - BM
Cos_BLM = cos(radians(BLM))
Sin_BLM = sin(radians(BLM))
print("BLM =" , BLM)
BLM_M= abs (BL - BM)
print ("BLM Mutlak =", BLM_M)
print (" ")

#Menentukan sin lamda_e
Sin_lamda_e = Sin_BLM * Cos_LM
print ("Sin_lamda_e =", Sin_lamda_e)

#Menentukan busur sinus lamda_e
lamda_e = degrees (asin(Sin_lamda_e))
print("lamda e =" , lamda_e)

Cos_lamda_e = cos(radians(lamda_e))
print ("cos lamda e =" , Cos_lamda_e)

#Menentukan sinus psi_e
if(Sin_LM / Cos_lamda_e>=1 and Sin_LM / Cos_lamda_e<1.1):
    Sin_psi_e = 1
else:
    Sin_psi_e = (Sin_LM / Cos_lamda_e)
print("Sin_psi_e =" , Sin_psi_e)

#Menentukan busur sinus psi e
psi_e = degrees(asin(Sin_psi_e))
print("psi_e =" , psi_e)
print("")

#Menentukan Nilai Alpha
Sin_alpha = (Sin_BLM * Sin_K_LM)
print ("Sin Alpha =", Sin_alpha)
#Menentukan Nilai Alpha
alpha = degrees(asin(Sin_alpha))
print ("Alpha =", alpha)
#Menentukan Nilai Komplemen Alpha
K_alpha = 90 - alpha
print ("Komplemen Alpha =", K_alpha)
#Menentukan Nilai Sin Alpha
Sin_K_alpha= sin(radians(K_alpha))
print ("Sin Komplemen Alpha =", Sin_K_alpha)
print("")

#Menentukan Nilai Beta
if(Sin_LM / Sin_K_alpha>=1 and Sin_LM / Sin_K_alpha<1.1):
    Sin_beta = 1
else:
    Sin_beta = Sin_LM / Sin_K_alpha
print ("Sin Beta =", Sin_beta)
beta = degrees(asin(Sin_beta))
print ("Beta =", beta)
K_beta = 90-beta
print("")

#Locality
if LL > 0:
    print("Lintang Lokasi > 0")
elif LL < 0:
    print("Lintang Lokasi < 0")
else:
    print("Lintang Lokasi = 0")

#Selisih Bujur Mutlak Lokasi dan Mekah
if BLM_M > 90:
    print("BLM Mutlak > 90")
elif BLM_M < 90:
    print("BLM Mutlak < 90")
else:
    print("BLM Mutlak = 90")

#Selisih Beta VS ujur Mutlak Lokasi dan Mekah
if beta > LL:
    print("Beta > Lintang Lokasi")
elif beta < LL:
    print("Beta < Lintang Lokasi")
else:
    print("Beta = Lintang Lokasi")
print("")

#Menentukan Nilai AK (Gamma), h, dan AT (q)
if LL>0 and BLM_M<90 and beta==LL: #1
    print("1")
    Gamma = "Timur/Barat"
    gamma = "Timur/Barat"
    q="Timur/Barat"
    if BL>BM:
        KiblatU=270
    elif BL<BM:
        KiblatU=90

elif LL>0 and BLM_M<90 and beta>LL: #2
    print("2")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q = degrees(asin(Sin_q))
    if q>0:
        KiblatU = 360-q
    elif q<0:
        KiblatU = -q
    else:
        KiblatU = 0

elif LL>0 and BLM_M<90 and beta<LL:     #3
    print("3")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q = degrees(asin(Sin_q))
    KiblatU = 180+q

elif LL>0 and BLM_M>90 and beta==K_LL:  #4
    print("4")
    Gamma = "q=alpha"
    gamma = "q=alpha"
    q = alpha
    if q>0:
        KiblatU = 360-q
    elif q<0:
        KiblatU = -q

elif LL>0 and BLM_M>90 and beta<K_LL:  #5
    print("5")
    Gamma = "LL+psi_e"
    gamma = LL+psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q = degrees(asin(Sin_q))
    print("q = AT =", q)
    if q>0:
        KiblatU = 360-q
    elif q<0:
        KiblatU = -q

elif LL>0 and BLM_M>90 and beta>K_LL:  #6
    print("6")
    Gamma = "LL+psi_e"
    gamma = LL+psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    #Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    if(sin(radians(lamda_e))/sin(radians(duakota))>=1 and sin(radians(lamda_e))/sin(radians(duakota))<1.1):
        Sin_q = 1
    else:
        Sin_q = sin(radians(lamda_e))/sin(radians(duakota))

    q=degrees(asin(Sin_q))
    if q>0 and -beta==K_LL:
        KiblatU=180+q
    elif q>0:
        KiblatU=360-q
    elif q<0:
        KiblatU=-q

elif LL>0 and BLM_M==90:  #7
    print("7")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    KiblatU=360-q

elif LL<0 and BLM_M>90 and beta==LL:  #8
    print("8")
    Gamma = "Timur/Barat"
    gamma = "Timur/Barat"
    q = "Timur/Barat"
    if BL>BM:
        KiblatU=270
    elif BL<BM:
        KiblatU=90

elif LL<0 and BLM_M>90 and beta>LL:  #9
    print("9")
    a=BM-180
    print(a)
    if LL==-LM and BL==BM-180.0:
        Gamma = "LL+psi_e"
        gamma = LL+psi_e
        q="Kemana Saja"
        KiblatU="Kemana Saja"
    else:
        Gamma = "LL+psi_e"
        gamma = LL+psi_e
        Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
        duakota = degrees(acos(Sin_duakota))
        Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    if q>0 and gamma>0:
        KiblatU=360-q
    elif q>0:
        KiblatU=180+q
    elif q<0 and gamma<0:
        KiblatU=180+q
    elif q<0:
        KiblatU=-q
        
elif LL<0 and BLM_M>90 and beta<LL: #10
    print("10")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))

elif LL<0 and BLM_M<90 and beta==K_LL: #11
    print("11")
    Gamma = "q=alpha"
    gamma = "q=alpha"
    q=alpha

elif LL<0 and BLM_M<90 and beta<K_LL: #12   Gamma = "LL-psi_e"
    print("12")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    if q>0:
        KiblatU=360-q
    elif q<0:
        KiblatU=-q
    else:
        KiblatU=0

elif LL<0 and BLM_M<90 and beta>K_LL: #13
    print("13")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))

elif LL<0 and BLM_M==90:  #14
    print("14")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    KiblatU=360-q

elif LL==0 and BLM_M<90:  #15
    print("15")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    if q>0:
        KiblatU=360-q
    elif q<0:
        KiblatU=-q

elif LL==0 and BLM_M>90:  #16
    print("16")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    if q>0:
        KiblatU=360-q
    elif q<0:
        KiblatU=-q
        
elif LL==0 and BLM_M==90:  #17
    print("17")
    Gamma = "LL-psi_e"
    gamma = LL-psi_e
    Sin_duakota = cos(radians(gamma))*cos(radians(lamda_e))
    duakota = degrees(acos(Sin_duakota))
    Sin_q = sin(radians(lamda_e))/sin(radians(duakota))
    q=degrees(asin(Sin_q))
    KiblatU=360-q

print("Gamma =", Gamma)
print("Gamma =", gamma)
print("   ")
print("q = AT =", q)
print("Kiblat Terhadap Utara =", KiblatU)

#Nilai Arah Kiblat Terhadap Utara Sexagesimal
if KiblatU=="Kemana Saja":
    print("Kiblat Terhadap Utara =", KiblatU)
else:
    D_Q1 = KiblatU
    M_Q1 = (D_Q1 - int(D_Q1))*60.0
    S_Q1 = round((M_Q1 - int(M_Q1))*60.0)
    Q2 = int(D_Q1),int(M_Q1),int(S_Q1)
    print("Kiblat Terhadap Utara =", Q2)

print('+++++===========================================+++++')
