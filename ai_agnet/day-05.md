##ReAct’i bir proje yöneticisine anlat. Döngü ne, tek seferde cevap yazmaya göre faydası ne?
# ReAct önce düşünür, sonra aracı çağırır, sonra dönen metni okur. Soruyu bilmiyorsa arar. Metin yeterse cevaplar, yetmezse tekrar arar. Adımlar görünür olduğu için hata, son cümleden önce yakalanır.

##LangChain agent’ına kendini düzeltmeyi nerede eklerdin?
# system_prompt içine bir kontrol cümlesi eklenerek duzeltme saglanabilir

##Hem bilgi hem akıl yürüten bir MRKL agent’ı nasıl kurardın? Hangi modül ne iş yapar?
# sorgu okunur ve hangi parcalarin kullanilacagina karar verilir daha sonra apiden gelen gerkcek bilgi gelir hesap yapilmaz son adimda ise bu iki bilgi karsilastirilarak sonuc bulunur