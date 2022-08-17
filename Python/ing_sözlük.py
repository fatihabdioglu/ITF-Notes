  # sözlük oluşturup kelime ve anlam ekleme günlük limit 2
ing_sözlük = {"blue" : "mavi", "red" : "kırmızı", "yellow" : "sarı"}
count = 0
while count < 2 :
    sorgu = input("Lütfen sorgulayacağınız kelimeyi giriniz. ").lower()
    if sorgu not in ing_sözlük :
        print("Veri tabanımızda yoktur.Lütfen kelimeyi veri tabanına giriniz. ")
        terc = input(f"Lütfen {sorgu} kelimesinin anlamını giriniz. ").lower()

        ing_sözlük.update({sorgu : terc})
        count += 1
        print(sorgu, terc)
    else :
        print(sorgu, "kelimesiveri tabanında bulunmaktadır.")
    
print("Tebrikler!Bugünkü hedefinizi tamamladınız. ")           