#theGame.py#
import time

def main():
            
      print('''
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████──██████─██████████████─████████████████───██████████████────██████████████─██████──────────██████────██████████─
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██████████████░░██────██░░░░░░██─
─██░░██──────────██░░██─██░░██──██░░██─██░░██████████─██░░████████░░██───██░░██████████────██░░██████░░██─██░░░░░░░░░░░░░░░░░░██────████░░████─
─██░░██──────────██░░██─██░░██──██░░██─██░░██─────────██░░██────██░░██───██░░██────────────██░░██──██░░██─██░░██████░░██████░░██──────██░░██───
─██░░██──██████──██░░██─██░░██████░░██─██░░██████████─██░░████████░░██───██░░██████████────██░░██████░░██─██░░██──██░░██──██░░██──────██░░██───
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██──██░░██──────██░░██───
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██████████─██░░██████░░████───██░░██████████────██░░██████░░██─██░░██──██████──██░░██──────██░░██───
─██░░██████░░██████░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─────██░░██────────────██░░██──██░░██─██░░██──────────██░░██──────██░░██───
─██░░░░░░░░░░░░░░░░░░██─██░░██──██░░██─██░░██████████─██░░██──██░░██████─██░░██████████────██░░██──██░░██─██░░██──────────██░░██────████░░████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██────██░░██──██░░██─██░░██──────────██░░██────██░░░░░░██─
─██████──██████──██████─██████──██████─██████████████─██████──██████████─██████████████────██████──██████─██████──────────██████────██████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████─██████──────────██████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─████░░████─██░░░░░░░░░░██──██░░██─██░░██████████─
─██░░██─────────██░░██──██░░██───██░░██───██░░██████░░██──██░░██─██░░██─────────
─██░░██─────────██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██─────────
─██░░██──██████─██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██████─
─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██████░░██─██░░██──██░░██─
─██░░██████░░██─██░░██████░░██─████░░████─██░░██──██░░░░░░░░░░██─██░░██████░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─
─██████████████─██████████████─██████████─██████──────────██████─██████████████─
──────────────────────────────────────────────────────────────────────────────── ''')

      time.sleep(1)   
                                                                                                                  
      print("--------------------------------------------------")
      if input("WELCOME SELECT LANGUAGE --> (English/Dutch : ") == "Dutch" :
            print("Dutch selected")
      else:
          print("I scanned you in my database and here it says that your dutch please restart and pick Dutch")
          return False
      print("--------------------------------------------------")
      print("Loading...")
      time.sleep(1.5)

      print("--------------------------------------------------")
      time.sleep(3)
      print("welkom in de game kies het juiste pad of anders overleef je het niet je kent het wel, laten we beginnen  ")
      time.sleep(3)
      print("--------------------------------------------------")
      time.sleep(3)
      print("Je bent gespawned op station Gorinchem en je moet binnen 2 uur naar Amsterdam kies de juist voertuigen om er op tijd te komen anders mis je het opstreden van Rapper Sjors")
      time.sleep(3)
      print("--------------------------------------------------")

      if input("je moet naar Dordrecht neem je de trein of de bus? : (Bus/trein) ") == "trein":
            print("--------------------------------------------------") 
            print("Je nam de trein en je bent in 13 min aangekomen in Dordrecht!")
      else:
            print("Je hebt de bus genomen maar omdat hij overal stopt ben je nu na 43 min aangekomen in dordrecht en dat is veel ste laat helaas")
            return False
      time.sleep(3)
      print("--------------------------------------------------")
      if input("Je bent nu in Dordrecht en je kan de trein nemen naar Amsterdam Centraal of de bus toeristen bus righting Amsterdam welke kies je? : trein naar Amsterdam/toeristen bus : ") == "toeristen bus":
            print("--------------------------------------------------")
            time.sleep(2)
            print("Je antwoord is goed je neemt de bus en voorkomt erge vertraging door een kind op het spoor je bent nu in 1 uur en 30 min bij een tank station dichtbij Amsterdam")
            time.sleep(3)
      else:
            print("Je neemt de trein maar komt na 7 min al met vertaging door een kind op het spoor je komt pas heel laat aan op Amsterdam centraal en je hebt het concert gemist helaas")
            return False
      print("--------------------------------------------------")
      time.sleep(3)

      if input("Je bent nu bij een tankstation van Shell daar stopte de bus en iedereen ging even wat kopen/pissen maar ze reden al weg voordat je klaar was en je staat daar nu helemaal alleen, wat ga je doen wachten voor een lift of bel je iemand in de buurt? : wachten voor een lift/bel iemand : ") == "wachten voor een lift":
           print("goedzo je wachten gewoon tot er een auto kwam en vroeg of je een stukje mee mocht rijden heel verstandig daarmee heb je tijd bespaard en ben je nu in Amsterdam")
      
      else:
            print("jammer je koos er voor om iemand te bellen en je hebt veel tijd verspeelt en je bent al te laat 2 uur is al om?")
            return False
            print("--------------------------------------------------")
      


      
      return True


if __name__ == "__main__":
    if main():
        print("--------------------------------------------------")
        print("UW missie is geslaagt u heeft het spel uitgespeelt")
    else:
        print("Uw missie is mislukt")
print("-------------------------------------------------------------------")
