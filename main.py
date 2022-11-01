print('''
"----------------------------------------------------------------------------"
          __-----__
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.\
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    `;.,|.    |      '\.-'/
      ~~;;;,._|___.,-;;;~'
          ''=--'


"----------------------------------------------------------------------------"
''')
print(" Bem vindo a ILHA DO TESOURO")
print(" Sua missão é encontrar o tesouro perdido do rei Lucky")
escolha1= input("Após sair do barco você se depara com uma mata densa! Mas após cortar a vegetação você percebe dois caminhos destintos.Você segue a direita or esquerda. \n").lower() 
if escolha1 == "esquerda":
  escolha2 = input("Parabéns,você chegou a um lago! Existe uma ilha no meio dele. Você decide esperar por um barco or para nadar. \n").lower()
  if escolha2 == "esperar":
    escolha3 = input("Você chega à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? \n"). lower()
    if escolha3 == "vermelha":
      print("Oh Não, uma sala cheia de cobras venenosas. GAME OVER")
    elif escolha3 == "azul":
      print(" Você Venceu!!!. O espirito do Rei Lucky fica agradecido por o encontrar, e te entrega a chave do Baú Perdido.")
    elif escolha3 == "amarela":
      print("Oh Não, Um abismo. GAME OVER")
    else: 
      print(" Esta porta não existe")
  else: 
    print("Crocodilos e piranhas famintas, você virou petisco. GAME OVER")
else: 
  print("Você voltou para a praia. Game Over")

    

  



