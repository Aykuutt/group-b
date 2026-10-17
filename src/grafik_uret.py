"""
FE Görsel Üretim Scripti — G1-GÖRSEL
Dosya: src/grafik_uret.py
Yazar: Ece Naz Aktürk (FE)
Kaynaklar: data/lojistik-sevkiyat.csv, docs/analiz-g1.md
Çıktılar:
  - visuals/taslak-grafikler.png (Issue #16 için ön taslak / wireframe ekran görüntüsü)
  - visuals/zaman-serisi.png
  - visuals/kirilim.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Grafik stil ayarları
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'lojistik-sevkiyat.csv')
VISUALS_DIR = os.path.join(BASE_DIR, 'visuals')

os.makedirs(VISUALS_DIR, exist_ok=True)

def uret_taslak():
    """Issue #16 için taslaksız başlanamaz kuralına uygun mockup/wireframe taslak görseli üretir."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=200)
    fig.patch.set_facecolor('#F8F9FA')

    # Sol: Zaman Serisi Taslağı
    ax1.set_facecolor('#FFFFFF')
    aylar = ['Ocak 2026', 'Şubat 2026', 'Mart 2026']
    adetler = [99, 98, 103]
    ax1.plot(aylar, adetler, marker='o', markersize=8, color='#7F8C8D', linestyle='--', linewidth=2)
    for i, txt in enumerate(adetler):
        ax1.annotate(f"{txt} adet", (aylar[i], adetler[i] + 0.8), ha='center', fontsize=10, color='#555555')
    ax1.set_title('[TASLAK] Aylık Sevkiyat Sayısı (Ocak–Mart 2026)', fontsize=12, fontweight='bold', pad=12, color='#2C3E50')
    ax1.set_xlabel('Ay', fontsize=10, labelpad=8)
    ax1.set_ylabel('Sevkiyat Adedi (adet)', fontsize=10, labelpad=8)
    ax1.set_ylim(85, 115)
    ax1.grid(True, linestyle=':', alpha=0.6, color='#BDC3C7')
    ax1.text(0.5, 0.05, '* DQ Analizine Göre Veri Kapsamı: Ocak–Mart 2026', transform=ax1.transAxes,
             fontsize=8, ha='center', style='italic', color='#7F8C8D')

    # Sağ: Kırılım Taslağı
    ax2.set_facecolor('#FFFFFF')
    modlar = ['Hava', 'Kara', 'Demiryolu', 'Deniz']
    ucretler = [14028.00, 4476.02, 2850.24, 1823.49]
    bars = ax2.bar(modlar, ucretler, color='#BDC3C7', edgecolor='#7F8C8D', linestyle='--', linewidth=1.5, width=0.55)
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 300, f"{yval:,.2f} TL", ha='center', va='bottom', fontsize=9, color='#555555')
    ax2.set_title('[TASLAK] Taşıma Moduna Göre Ortalama Ücret', fontsize=12, fontweight='bold', pad=12, color='#2C3E50')
    ax2.set_xlabel('Taşıma Modu', fontsize=10, labelpad=8)
    ax2.set_ylabel('Ortalama Ücret (TL)', fontsize=10, labelpad=8)
    ax2.set_ylim(0, 16500)
    ax2.grid(True, axis='y', linestyle=':', alpha=0.6, color='#BDC3C7')

    plt.suptitle('G1-GÖRSEL ÖN TASLAK ÇİZİMİ (MOCKUP / WIREFRAME) — ISSUE #16', fontsize=14, fontweight='bold', color='#1A252F', y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    
    taslak_yol = os.path.join(VISUALS_DIR, 'taslak-grafikler.png')
    plt.savefig(taslak_yol, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Taslak çizim üretildi: {taslak_yol}")


def uret_zaman_serisi(df):
    """Standartlara uygun yüksek çözünürlüklü zaman serisi grafiği üretir."""
    df['tarih'] = pd.to_datetime(df['tarih'])
    df['ay_kod'] = df['tarih'].dt.to_period('M')
    
    aylik_ozet = df.groupby('ay_kod').size().reset_index(name='sevkiyat_adedi')
    
    ay_isimleri = {
        '2026-01': 'Ocak 2026',
        '2026-02': 'Şubat 2026',
        '2026-03': 'Mart 2026'
    }
    aylik_ozet['ay_etiket'] = aylik_ozet['ay_kod'].astype(str).map(ay_isimleri)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FAFAFA')

    # Çizgi grafik
    x = aylik_ozet['ay_etiket']
    y = aylik_ozet['sevkiyat_adedi']
    
    line = ax.plot(x, y, color='#1F4E79', linewidth=3, marker='o', markersize=9, 
                   markerfacecolor='#2E75B6', markeredgecolor='#1F4E79', markeredgewidth=2, label='Sevkiyat Adedi')

    # Veri etiketleri
    for i, val in enumerate(y):
        ax.annotate(f'{val} adet', 
                    (x[i], val), 
                    textcoords="offset points", 
                    xytext=(0, 14), 
                    ha='center', 
                    fontsize=11, 
                    fontweight='bold', 
                    color='#1F4E79',
                    bbox=dict(boxstyle="round,pad=0.3", fc="#EBF1F5", ec="#2E75B6", lw=1))

    ax.set_title('Aylık Sevkiyat Sayısı (Ocak–Mart 2026)', fontsize=15, fontweight='bold', pad=16, color='#1F4E79')
    ax.set_xlabel('Ay', fontsize=12, fontweight='bold', labelpad=10, color='#333333')
    ax.set_ylabel('Sevkiyat Adedi (adet)', fontsize=12, fontweight='bold', labelpad=10, color='#333333')
    
    ax.set_ylim(80, 115)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.grid(True, linestyle='--', alpha=0.5, color='#CCCCCC')

    # Dipnot: DQ analiz devir uyarısı
    plt.figtext(0.5, 0.01, '* Veri Kaynağı: data/lojistik-sevkiyat.csv | Kapsam: 1 Ocak–31 Mart 2026 (DQ Analiz Devir Notu: docs/analiz-g1.md)',
                ha='center', fontsize=9, color='#666666', style='italic')

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    cikis_yolu = os.path.join(VISUALS_DIR, 'zaman-serisi.png')
    plt.savefig(cikis_yolu, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Zaman serisi grafiği üretildi: {cikis_yolu}")


def uret_kirilim(df):
    """Standartlara uygun yüksek çözünürlüklü taşıma modu kırılım grafiği üretir."""
    # Taşıma moduna göre ortalama ücret
    mod_ozet = df.groupby('tasima_modu')['ucret_tl'].mean().reset_index()
    
    mod_isimleri = {
        'hava': 'Hava',
        'kara': 'Kara',
        'demiryolu': 'Demiryolu',
        'deniz': 'Deniz'
    }
    mod_ozet['mod_etiket'] = mod_ozet['tasima_modu'].map(mod_isimleri)
    # Büyükten küçüğe sırala
    mod_ozet = mod_ozet.sort_values(by='ucret_tl', ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FAFAFA')

    renkler = ['#1F4E79', '#2E75B6', '#5B9BD5', '#41B6E6']
    bars = ax.bar(mod_ozet['mod_etiket'], mod_ozet['ucret_tl'], color=renkler, width=0.52, edgecolor='#1F4E79', linewidth=1)

    # Veri etiketleri
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, h + 320,
                f"{h:,.2f} TL".replace(',', 'X').replace('.', ',').replace('X', '.'),
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1F4E79')

    ax.set_title('Taşıma Moduna Göre Ortalama Sevkiyat Ücreti', fontsize=15, fontweight='bold', pad=16, color='#1F4E79')
    ax.set_xlabel('Taşıma Modu', fontsize=12, fontweight='bold', labelpad=10, color='#333333')
    ax.set_ylabel('Ortalama Ücret (TL)', fontsize=12, fontweight='bold', labelpad=10, color='#333333')
    
    ax.set_ylim(0, 16000)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,} TL".replace(',', '.')))
    ax.grid(True, axis='y', linestyle='--', alpha=0.5, color='#CCCCCC')

    plt.figtext(0.5, 0.01, '* Veri Kaynağı: data/lojistik-sevkiyat.csv | N=300 Sevkiyat | Metrikler: docs/analiz-g1.md',
                ha='center', fontsize=9, color='#666666', style='italic')

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    cikis_yolu = os.path.join(VISUALS_DIR, 'kirilim.png')
    plt.savefig(cikis_yolu, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Kırılım grafiği üretildi: {cikis_yolu}")


if __name__ == '__main__':
    print("Veri yükleniyor...")
    df = pd.read_csv(DATA_PATH)
    print(f"Veri yüklendi: {len(df)} satır.")
    
    print("\n1. Aşama: Taslak çizim (mockup) üretiliyor...")
    uret_taslak()
    
    print("\n2. Aşama: Zaman serisi grafiği üretiliyor...")
    uret_zaman_serisi(df)
    
    print("\n3. Aşama: Kırılım grafiği üretiliyor...")
    uret_kirilim(df)
    
    print("\nTüm grafikler başarıyla oluşturuldu!")
