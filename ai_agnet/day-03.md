##LangChain ile LlamaIndex’in tasarım fikri nasıl ayrılır?

# LangChain sorguya gore arac cagiran veri ceken ileten bir yapidayken LlamaIndex elindeki verilerden pdf ten veya dokumandan o konu ile ilgili kisimi llm e iletir

##Kendi PDF dosyalarınla sohbet eden bir agent kurmak istesen hangi çerçeve daha uygun, neden? 

# LlamaIndex daha uygundur kendi kayitli dokumandan ve klasorlerden konu ile ilgili kismi alip llm e iletir boylelikle  tum dosylar taranmak zorunda kalmaz

##LangChain ile Hello World agent

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("Hello, World!").content)
```