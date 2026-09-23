##Vektör deposu nedir ve AI agent’ta uzun bellek için neden işe yarar?
# metin sayiya cevrilir ve depolanir sorgu geldiginde bu depodan ilgili olan kisim okunur ve ona gore cevaplanir veya aksiyon alinir boylelikle is yuku azaltilmis olur

##LangChain agent’ına konuşma geçmişi ekleyen Python kodunu yaz.
```python
messages = [
    {"role": "user", "content": "Akşam 21 dereceyi seviyorum."},
    {"role": "assistant", "content": "Akşam 21 dereceyi tercih ettiğini hatırlıyorum."},
    {"role": "user", "content": "Termostatı kaç derece yapayım?"},
]
result = agent.invoke({"messages": messages})
```
##Kullanıcı tercihini uzun süre hatırlayan bir bellek sistemi tasarla.
# message listesine degil vektor diske yazilir, vektor deposunda metinsel ifade olarak depolanir ve sorgu geldiginde butun gecmisi okumak yerine ilgili yeri bulur ve orayi okur ve model ona gore cevaplar
