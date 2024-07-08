
("""
- Evrensel kısaltmaları kullanarak numpy ve pandas kütüphanelerini import ediniz.

1) İndexlerinde "Breaking Bad" , "Chernobyl" , "Leyla ile Mecnun" , "X-Men"  , "Captain America"  , "Disaster Movie" olan 
   Datasında 9.4 , 9.3 , 8.8 , 8.4 , 3.8 , 2.1 olan bir seri oluşturun.(2 Farklı yolla da oluşturun) (Datayı ve İndexleri liste olarak göndererek ve doğrudan dictionary göndererek.)


2) donem1_mat adında bir seri oluşturun. Bu serinin içinde "Ali" ,"Deniz" ,"Aslı" ,"Burak" ,"Kerem" ,"Yasemin" ,"Derya" index değerleri olsun, 
   85, 80 , 94 , 74 , 91 , 96 , 70 data değerleri olsun. Bu şekilde donem1 adında öğrencilerin 1.dönem matematik nor ortalamalarının tutulduğu bir seri oluşturun.

   donem2_mat adında başka bir seri oluşturun. Okula yeni bir öğrenci gelmiş olsun ve indexlerde bu sefer "Ali" ,"Deniz" ,"Aslı" ,"Burak" ,"Kerem" ,"Yasemin" ,"Derya" ,"Mert"         indexleri olsun. 80, 92 , 85 , 87, 90 , 92, 100, 83 ise dataları olsun. Bu iki seriyi birleştirerek bütün öğrencilerin yıl sonu matematik ORTALAMASINI hesaplayın.

   Not : Eğer bir öğrencinin sadece ikinci dönem notu bulunuyorsa, birinci dönem hesaba eklenmeden ikinci dönem notu yıl sonu notu olarak hesaplansın.


3) İndexlerinde "Osman", "Ozlem", "İnci", "Koray", "Melek" olan, columnlarında "Sınıf" , "Cinsiyet" , "Favori Ders" isimlerinde 3 column bulunan bir DF oluşturacaksınız. Osman'ın sınıfı 8 , cinsiyeti "E" , Favori Dersi "Fen"
Ozlem'in sınıfı 11 , cinsiyeti "K" , Favori Dersi "Mat"
İnci'nin sınıfı 5 , cinsiyeti "K" , Favori Dersi "Sosyal"
Koray'ın sınıfı 9 , cinsiyeti "E" , Favori Dersi "Mat"
Meleğin sınıfı 7 , cinsiyeti "K" , Favori Dersi "Ing"          Olacak şekilde bir df oluşturun.

4) GitHubda bulunan "Advertising.csv" reklam datasını herhangi bir platformda DF olarak okuyun ve "df_adv" adında bir değişkene atayın. Ardından df_adv değişkeninin ilk 3 satırına, son 3 satırına , rastgele 3 satırına bakın.

5) Elde ettiğiniz "df_adv" infosuna ve describe'ına bakın ve yorumlamaya çalışın.

6) df_adv içinden sadece "TV" sütununu seri olarak çekin.

7) df_adv içinden "TV" ve "sales" sütununu çekin ve df_salesTV adında bir değişkene atayın.

8) df_adv içindeki "TV" , "radio" , "newspaper" sütunlarındaki değerleri toplayarak "total_adv" adında yeni bir sütun oluşturun.

9) df_adv içindeki "sales" sütununun drop edilmiş halini ekrana yazdırın. (Kalıcı hale getirmeyin. Sadece ekrana bastırın)

10) df_adv içindeki son 50 index'i(satırı) çekin ve ekrana yazdırın.

11) df_adv içinde satışları 25'den fazla olanları getirin.

12) df_adv içinde "TV" reklamlarına 250'den fazla VE "newspaper" reklamlarına 60'dan fazla harcama yapanları getirin.

13) df_adv içinde "newspaper" reklam harcamaları 70'den fazla VEYA "radio" reklam harcamaları 50'den fazla olanları getirin.

14) df_adv içinde "sales" ları 10 ile 15(10 ve 15 dahil) arasında olanları getirin.

15) df_adv içinde "sales" ları tam olarak 18.3 veya 14.0 veya 25.5 veya 21.7 veya 13.6 veya 6.9 olanları getirin.

16) GitHubda bulunan "tips.csv" restoran datasını "df_tips" adıyla okuyun. Ardından ilk 5 satırına bakın.

17) df_tips'in "CC Number" ve "Payment ID" column'larını kalıcı olarak düşürün.

18) df_tips'in "Payer Name" column'unu kalıcı olarak index yapın ve artık columndan düşürün.

19) df_tips içindeki kayıtlardan kişi sayısı 4 veya 4'den fazla olan siparişlerin kaç tane olduğunu bulun.(Sorguyu yazıp istediğimiz satırları getirdikten sonra basitçe len() fonksiyonunu kullanarak sayılarını bulabilirsiniz. Veya daha güzeli .shape[0] yaparak elde ettiğiniz sorguda kaç satır olduğunun sayısına ulaşabilirsiniz.)

20) df_tips içindeki Kişi sayısı 2 ya da 3 olan, sigara içen, erkek olan ve ödediği ücret 20 dolardan az olan kişi sayısını bulalım.
 """)

import pandas as pd
import numpy as np

my_data = ["Breaking Bad" , "Chernobyl" , "Leyla ile Mecnun" , "X-Men"  , "Captain America"  , "Disaster Movie"]
my_idx = [9.4 , 9.3 , 8.8 , 8.4 , 3.8 , 2.1]

ss = pd.Series(my_idx,my_data)
print(ss)

dict = {"Breaking Bad":9.4 , "Chernobyl":9.3 , "Leyla ile Mecnun":8.8 , "X-Men":8.4  , "Captain America":3.8  , "Disaster Movie":2.1}
ss1 = pd.Series(dict)
print(ss1)
print("***************************************************************************\n")

donem1_mat = {"Ali":85 ,"Deniz":80 ,"Aslı":94 ,"Burak":74 ,"Kerem":91 ,"Yasemin":96 ,"Derya":70}
d1 = pd.Series(donem1_mat)
donem2_mat = {"Ali":80 ,"Deniz":92 ,"Aslı":85 ,"Burak":87 ,"Kerem":90 ,"Yasemin":92 ,"Derya":100 , "Mert":83}
d2 = pd.Series(donem2_mat)
total = d1.add(d2,fill_value=0)/2
print(d1)
print(d2)
print(total)
print("***************************************************************************\n")

my_idx =("Osman", "Ozlem", "İnci", "Koray", "Melek")
my_colm = ("Sınıf" , "Cinsiyet" , "Favori Ders")
my_data = ([8,"E","Fen"],[11,"K","Mat"],[5,"K","Sostal"],[9,"E","Mat"],[7,"K","Ing"])

son = pd.DataFrame(data=my_data,index=my_idx,columns=my_colm)
print(son)
print("***************************************************************************\n")

df_adv = pd.read_csv('Advertising (1).csv')
print(df_adv.head(3))
print("***************************************************************************\n")

print(df_adv.tail(3))
print("***************************************************************************\n")

print(df_adv.sample(3))
print("***************************************************************************\n")

print(df_adv.shape)
print("***************************************************************************\n")

print(df_adv.info)
print(df_adv.describe())
print("***************************************************************************\n")

seri = df_adv['TV']
print(seri)
print("***************************************************************************\n")

df_salesTV = df_adv[['TV','sales']]
print(df_salesTV)
print("***************************************************************************\n")

df_adv['total_adv'] = df_adv['TV'] + df_adv['radio'] + df_adv['newspaper']
print(df_adv)
print("***************************************************************************\n")

print(df_adv.drop(['sales'],axis=1,inplace=False))
print("***************************************************************************\n")

print(df_adv.tail(50))
print("***************************************************************************\n")

print(df_adv[df_adv['sales']>25])
print("***************************************************************************\n")

print(df_adv[(df_adv['TV']>250) & (df_adv['newspaper']>60)])
print("***************************************************************************\n")

print(df_adv[(df_adv['newspaper']>70) | (df_adv['radio']>50)])
print("***************************************************************************\n")

print(df_adv[(df_adv['sales']>= 10) & (df_adv['sales']<=15)])
print("***************************************************************************\n")

print(df_adv[(df_adv['sales']== 18.3) | (df_adv['sales']==14.0) | (df_adv['sales']== 25.5) | (df_adv['sales']== 21.7) | (df_adv['sales']== 13.6) | (df_adv['sales']== 6.9)])
print("***************************************************************************\n")

df_tips = pd.read_csv('tips.csv')

print(df_tips.head(5))
print("***************************************************************************\n")

df_tips.set_index('Payer Name',drop=True,inplace=True)
print(df_tips)
print("***************************************************************************\n")

sayi = df_tips[(df_tips['size'] >= 4)]
print(len(sayi))
print(sayi.shape[0])
print("***************************************************************************\n")
print(df_tips.info)
print(df_tips.columns)
print(df_tips['smoker'])
print(df_tips['sex'])
print((df_tips[((df_tips['size'] == 3) | (df_tips['size'] == 4)) & (df_tips['smoker'] == 'Yes') & (df_tips['sex'] == 'Male') & (df_tips['total_bill'] < 20)]))




