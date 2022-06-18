# ASEAN-5 Study
> **oleh**: Muhammad Nur Fitrah Ramadhan

[![Generic badge](https://img.shields.io/badge/pandas-1.2.5-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/matplotlib-3.3.5-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/numpy-1.20.2-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/seaborn-0.11.2-<COLOR>.svg)](https://shields.io/)

## Tentang *ASEAN-5 Study*
Seri ini mengulas secara mendalam tentang kondisi ekonomi kawasan ASEAN-5 (Indonesia, Malaysia, Singapura, Thailand, dan Filipina). Menggunakan dataset yang tersedia di *World Bank Open Data*, seri ini mengkaji secara menyeluruh atau negara per negara secara komprehensif.

> Mengapa ASEAN-5?

Kelima negara Asia Tenggara, Indonesia, Malaysia, Singapura, Filipina, dan Thailand,merupakan pelopor berdirinya Association of South East Asian Nation (ASEAN) pada tahun 1967. Sejak berdirinya ASEAN, kelima negara tersebut, khususnya ASEAN-5 dan umumnya keseluruhan negara ASEAN, telah melakukan berbagai macam kerjasama dalam bidang ekonomi internasional.

Kerjasama-kerjasama yang dihadirkan merupakan bentuk upaya menumbuhkan kesejahteraan di setiap negara anggota. Semisal perjanjian AFTA pada tahun 1992 dalam rangka mendorong perdagangan bebas di kawasan Asia Tenggara. Dihapuskannya berbagai macam bentuk hambatan perdagangan diharapkan mampu mendorong terciptanya peningkatan volume perdagangan.

## Kondisi Makroekonomi Negara-Negara ASEAN-5
### *Gross Domestic Product (GDP)*
> Apa itu GDP?

*Gross domestic product (GDP) is a monetary measure of the market value of all the final goods and services produced in a specific time period by countries.*
***sumber: https://en.wikipedia.org/wiki/Gross_domestic_product***

Meski demikian, GDP yang digunakan dalam seri ini adalah GDP konstan yang mengukur nilai barang dan jasa akhir setiap tahunnya menggunakan US$ tahun 2015 sebagai tahun dasar.

> GDP ASEAN-5

![Constant GDP ASEAN-5!](/pictures/constant-gdp.png)

GDP negara ASEAN-5 mengalami peningkatan sejak tahun 1961. Tampak terjadi pergerakan bersama pada masa-masa tertentu. Semisal krisis ekonomi asia pada tahun 1998, setiap negara ASEAN-5 mengalami penurunan nilai GDP. Hal serupa terjadi pada tahun 2020, yaitu krisis ekonomi akibat pandemi Covid-19.

Indonesia menjadi negara dengan kue ekonomi terbesar di antara negara ASEAN-5 lainnya. Dengan nilai GDP tertinggi sebebsar US$ 1.049,31 Miliar. Dimana:

* Malaysia = 2.88x Indonesia
* Singapore = 3.01x Indonesia
* Thailand = 2.28x Indonesia
* Philippines = 2.65x Indonesia

## Pertumbuhan Ekonomi
> Apa itu pertumbuhan ekonomi?

Pertumbuhan ekonomi mengukur perubahan GDP konstan dari tahun-ke-tahun.

> Pertumbuhan ekonomi ASEAN-5

![GDP Growth ASEAN-5!](/pictures/gdp-growth.png)

|	|Indonesia   | Malaysia  | Philippines | Singapore    | Thailand  |
|-------|------------|-----------|-------------|--------------|-----------|
|count	| 60.000000  | 60.000000 | 60.000000   | 60.000000    | 60.000000 |
|mean	| 5.131592   | 6.124539  | 4.200713    | 7.017688     | 5.732013  |
|std	| 3.434743   | 3.620158  | 3.372412    | 4.457693     | 3.894371  |
|min	|-13.126725  |-7.359415  |-9.573030    |-5.391021     |-7.634035  |
|25%	| 4.682127   | 5.166832  | 3.488565    | 4.341629     | 4.256277  |
|50%	| 5.716609   | 6.359908  | 5.062535    | 7.512713     | 5.618073  |
|75%	| 6.987645   | 8.453714  | 6.134874    | 10.124566    | 8.120804  |
|max	| 10.915179  | 11.701082 | 8.782009    | 14.525639    | 13.288114 |

Singapura menjadi negara dengan pertumbuhan ekonomi tertinggi secara rata-rata dengan nilai 7.01 persen per tahun. Sementara itu, Indonesia menjadi yang terendah dengan pertumbuhan rata-rata 5.13 persen per tahun.

Selain dari dua krisis besar, Asian Financial Crisis 1997 dan Pandemi Covid-19, Terdapat beberapa momen di mana ekonomi beberapa negara tertentu mengalami krisis. Misalnya, di Filipina beberapa krisis terjadi sebagai akibat dari instabilitas politik.

## Stabilitas Ekonomi

![Boxplot Growth ASEAN-5!](/pictures/growth-boxplot.png)

> #### Penjelasan mengenai bagian-bagian boxplot
>> * Titik-titik yang berada diluar ekor boxplot menunjukkan data outlier.
>> * Garis horizontal ditengah box menunjukkan nilai tengah
>> * Sisi atas box menunjukkan kuartil 3
>> * Sisi bawah box menunjukkan kuartil 1
>> * Ekor atas menunjukkan nilai maksimum kuartil, kuartil 3 + 1.5*(kuartil 3 - kuartil 1)
>> * Ekor atas menunjukkan nilai minimum kuartil, kuartil 1 - 1.5*(kuartil 3 - kuartil 1)

Indonesia menjadi negara yang mendapatkan pengalaman terburuk dari krisis ekonomi dengan *outlier* negatif yang paling jauh dibanding negara lainnya. Namun, fluktuasi pertumbuhan relatif lebih rendah. Sedangkan, Singapura menjadi negara yang kebal terhadap krisis ekonomi sekaligus menjadi negara yang mengalami pertumbuhan yang relatif lebih fluktuatif.
* **Indonesia: Rentan tetapi stabil secara keseluruhan**
* **Singapura: Kebal tetapi tidak stabil secara keseluruhan**

## Korelasi Pertumbuhan Ekonomi

![Heatmap Growth ASEAN-5!](/pictures/growth-heatmap.png)

Secara keseluruhan, negara ASEAN-5 mengalami korelasi positif. Artinya, terdapat hubungan yang kuat antara pertumbuhan ekonomi suatu negara dan negara lainnya.

* Korelasi tertinggi dialami oleh pasangan negara Malaysia-Singapura dengan nilai korelasi sebesar 0,73
* Korelasi terendah dialami oleh pasangan negara Indonesia-Filipina dengan nilai korelasi sebesar 0,37


## Inflasi

![inflasi Tahun 1960 - 2021!](/pictures/inflation1960-2021.png)

Inflasi di Indonesia sangat bergejolak terutama sebelum tahun 1970. Pada masa itu terjadi hyperinflasi di Indonesia.

![inflasi pasca 1970!](/pictures/inflation1970-2021.png)

Pasca 1970, Indonesia berhasil melakukan stabilisasi tingkat inflasi. Namun secara keseluruhan, Indonesia tetap menjadi negara dengan fluktuasi inflasi yang paling tinggi dibanding negara lainnya.

![boxplot inflasi](/pictures/inflation1970-2021.png)

Sebaliknya, Singapura menjadi negara yang paling stabil dalam menangani fluktuasi ekstrim dari tingkat inflasi.

* Interquartile Indonesia : 8.350583150582125
* Interquartile Malaysia : 5.624871041423183
* Interquartile Singapore : 3.6150353508487516
* Interquartile Thailand : 4.025250997713025
* Interquartile Philippines : 6.40322063068572

Terdapat hubungan yang sangat kuat untuk tingkat inflasi di ASEAN-5

![heatmap inflasi](/pictures/inflation-heatmap.png)


