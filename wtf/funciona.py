a = open("corretaco_final.csv","r")
b = open("nova_saida.csv","w")

for linha in a:
  linha = linha.replace("  "," ").replace("  "," ").replace("  "," ").replace(",",";")
  b.write(linha)
  
a.close()
b.close()
 
a = open("nova_saida.csv", "r")
b = open("mais_nova_nova.csv", "w")

for linha in a:
  linha = linha.replace("  "," ").replace("  "," ").replace(".",",")
  b.write(linha)
  
a.close()
b.close()