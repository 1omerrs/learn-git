 
 
 
 
 
 
 
 
 
 ```python
 from langchain.tools import tool

 @tool
 def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    return f"{city} icin hava metini burada API den gelir."


##Q:Twitter’a yazan bir aracın girdisi ve çıktısı ne olur?
#A:girdi paylaşılacak metin, iş Twitter’a göndermek, dönüş ise “gönderildi” gibi bir onay metni

##Q:Agent’a rastgele kod çalıştıran bir araç vermek neden tehlikelidir ve bu risk nasıl azaltılır? 
#A:Rastgele kod çalıştıran araç dosya silebilir ve makinedeki .env anahtarını okuyup dışarı gönderebilir. Bu risk, agent’a istediği komutu değil, yalnızca web_search ve get_weather gibi adı belli araçları vererek azaltılır.