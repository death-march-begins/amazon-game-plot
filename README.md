# amazon-game-plot

## Preprocess

 **run** : ***produk-feq.py** dirData OutputName*

Menghitung review untuk masing2 produk, dan memberikan skor pada produk berdasarkan total review dan ratingnya
contoh data :

**{"produk": "B00HTK1NCS", "total": 6462, "positif": 5113, "netral": 479, "negatif": 870, "score": 10705}**

- produk : id dari produk game amazon
- total : total dari review pada produk
- positif : total riview rating diatas 3.0
- netral : total riview rating sama dengan 3.0
- negatif : total riview rating dibawah 3.0

 
  
## Plotting Histogram

  **run** : ***rank-game.py** score.json*
  
Melakukan plotting dalam bentuk histogram dari data yang sudah diproses sebelunya dalam bentuk Histogram

![alt text](http://url/to/img.png)
  
