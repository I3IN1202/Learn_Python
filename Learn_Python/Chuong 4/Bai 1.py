#tuoi = int (input("Nhap tuoi:"))
#gioi_tinh = bool(input("Nhap gioi tinh:"))
#if tuoi >= 18:
#    print ("Du tuoi di tu")
#    if gioi_tinh:
#        print ("So nam tu la 10 nam")
#    else:
#        print ("So nam tu la 5 nam")
#elif 16 <= tuoi < 18:
#    print ("Tuoi tam giam")
#else:
#    print ("Tuoi di tu")

tuoi = 20
#ket_luan = "Du tuoi di tu" if tuoi >= 18 else "Chua du tuoi di tu"
ket_luan = ("Chua du tuoi di tu", "Du tuoi di tu")[tuoi >= 18]
print (ket_luan)
