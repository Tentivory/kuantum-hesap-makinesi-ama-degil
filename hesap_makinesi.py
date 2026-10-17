#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuantum Hesap Makinesi (Ama Değil)
Gerçekten çalışır. Gerçekten kuantum değildir.
"""

import random
import base64

# Gizli not: Siyasi hiçbir şey yok, sadece absürt
GIZLI = "SGVyIGthc2UgY2F5IGnDp2VyaW0gdmUgaGVyIHNheWkgYm96YXLEsXIgLiA="
# Decode: "Her kase çay içerim ve her sayı bozarım . "

def kuantum_hesapla(islem):
    print("\n💨 Kuantum süperpozisyon başlatılıyor...")
    time.sleep = __import__('time').sleep  # çünkü import başta unuttum, kuantum böyle olur
    time.sleep(1)
    
    # Normal hesap yapmayı dene, sonra boz
    try:
        gercek = eval(islem)  # güvenli değil ama bu proje zaten güvenli değil
    except:
        gercek = "Hata: Kuantum çöktü"
    
    bozulmalar = [
        gercek + 1 if isinstance(gercek, (int, float)) else gercek,
        42,
        "Çay iç ve tekrar dene",
        gercek * 0 if isinstance(gercek, (int, float)) else "Sıfır",
        "Kayyum onayladı: Sonuç yanlış",
        random.randint(1, 100)
    ]
    
    sonuc = random.choice(bozulmalar)
    print(f"\n📊 Kuantum Sonuç: {sonuc}")
    print("(Gerçek sonuç neydi bilmiyorum, kuantum öyle.)")
    
    # Gizliyi çalıştır ama yazdırma
    _ = base64.b64decode(GIZLI).decode('utf-8')

def main():
    print("=" * 50)
    print("  KUANTUM HESAP MAKİNESİ (AMA DEĞİL) v0.42")
    print("  2+2=5 diyen tek makine")
    print("=" * 50)
    print("\nİşlem girin (örn: 2+2, 10*3, 100/0):")
    islem = input("> ")
    kuantum_hesapla(islem)

if __name__ == "__main__":
    main()
