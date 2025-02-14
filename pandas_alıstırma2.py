("""
1) df_tips içindeki Payment ID column'unun son 3 rakamını çekin. Bu işlemi 3 farklı yolla da yapmaya çalışın.
2) df_tips içindeki Payer Name sütununda isim ve soy isim bilgileri bulunuyor. O sütundan sadece isim bilgileri çekin ve 'JustName' adında yeni bir column oluşturun. (Bu biraz zorlayıcı olabilir, Önce kendiniz yapmaya çalışın fakat yapamazsanız ChatGPT'ye soruyu düzgünce sorarak cevabını kod olarak alabilirsiniz, ardından döndürülen kodu anlamaya çalışmanız yeterlidir.)
3) 2.Soruda yeni oluşturduğunuz 'JustName' sütunundaki verilerin her birinden kaç tane olduğuna uygun methodu kullanarak bakın.
4) 3.Soruda gördüğünüz gibi JustName sütununda 'Jason' isminden 9 tane, 'Michael' isminden 7 tane , 'James' isminden 6 tane bulunuyor. Peki bunların hepsi gerçekten farklı kişiler mi ? Hemen 'Payer Name' sütunundaki verilerin adetlerini de saydırtarak bir kıyaslama yapın. 'JustName' sütununu kullanmanın faydasız ve yanıltıcı olabileceğini görün ardından oluşturduğumuz 'JustName' sütununu kalıcı olarak drop edin. (Oluşturmanız için bir pratikti bu sütun sadece :D)
5) Erkeklerin ve kadınların davranış patternlerini ayrı ayrı inceleyip yorumda bulunabilmek için 'df_male' ve 'df_female' adında 2 dataframe oluşturun. Birinde sadece 157 erkek verisi, diğerinde sadece 87 kadın verisi bulunsun.
6) Ardından bu 'df_male' ile 'df_female' 'in ödedikleri bahşişler toplamını bulup karşılaştırın.
7) 6.Soruda erkeklerin ve kadınların ödedikleri bahşişler toplamına bakıldığında Erkeklerin kadınlara kıyasla toplamda daha çok bahşiş ödediğini görüyoruz. Fakat biz biliyoruz ki bizim verimizde 157 Erkek, 87 kadın verisi vardı. Dolayısıyla Erkek sayısı daha fazla olduğu için toplam ödeyecekleri bahşiş miktarlarında da daha fazla çıkması oldukça normal bir durum. Bu yüzden daha mantıklı bir çıkarım için bu sefer df_male ile df_female'in bahşiş ORTALAMALARIN'a bakıp kıyaslayın, aralarında anlamlı ve ciddi bir fark var mı ?
8) Oluşturmuş olduğunuz df_male ile çalışarak elimizdeki verideki erkeklerin yüzde kaçının sigara içtiğini bulun. Aynı şekilde elimizdeki kadınların yüzde kaçının sigara içtiğini de bulun. Aralarında anlamlı bir fark mı yorumlayın.
9) Erkeklerin zaman olarak dinnerda mı yoksa lunch'da mı daha fazla yemek yediğini yüzdesel olarak bulun. Aynı işlemi kadınlar için de yapın. Yüzdesel olarak erkeklerin ve kadınların yemek yeme vakitleri arasında anlamlı bir fark var mı yok mu yorumlayın.
10) CC Number sütununu kalıcı olarak drop edin. Ardından df'in içindeki sütunların birbirleriyle olan ilişkilerini inceleyin ve çıkan sonuçlar hakkında yorumlarınızı belirtin.""")


import pandas as pd
import numpy as np

df_tips = pd.read_csv('tips.csv')
print(df_tips.head(2))
cek = df_tips['Payment ID']
print(cek)
print("***************************************************************************\n")

print(df_tips['Payer Name'])
print(df_tips['Payer Name'][0])
df_tips['Just Name'] = df_tips['Payer Name'].str.split().str[0]

print(df_tips['Just Name'])
print("***************************************************************************\n")

deger =df_tips['Just Name'].value_counts()

print(deger)
print(deger.sum())
print(len(df_tips['Payer Name']))
print("***************************************************************************\n")

df_male = df_tips[df_tips['sex'] == 'Male']
print(df_male)
df_female = df_tips[df_tips['sex'] == 'Female']
print(df_female)
eb = df_male['tip'].sum()
kb = df_female['tip'].sum()
print(eb/157)
print(kb/87)


es =len(df_male[df_male['smoker'] == 'Yes'])
ks =len(df_female[df_female['smoker'] == 'Yes'])
print((es/157) * 100)
print((ks/87) * 100)

print("***************************************************************************\n")

el = len(df_male[df_male['time'] == 'Lunch'])
ed = len(df_male[df_male['time'] == 'Dinner'])
ely = (el/157) * 100
edy = (ed/157) * 100

print(ely,edy)
kl = len(df_female[df_female['time'] == 'Lunch'])
kd = len(df_female[df_female['time'] == 'Dinner'])

kly = (kl/87)*100
kdy = (kd/87)* 100

print(kly,kdy)

df_tips.drop('CC Number',axis = 1,inplace=True)
print(df_tips)










