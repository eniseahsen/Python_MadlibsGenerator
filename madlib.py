with open("story.txt","r") as f: # r mode reading modu
  story = f.read()

words = set()
start_of_word = -1 #hedef kelimenin başlangıç pozisyonunu bulmak için atanan bir değişkendir. başlangıçta -1 olarak atanır, çünkü henüz kelimenin başlangıcı bulunmamıştır.

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
  if char == target_start:
    start_of_word = i # char target_start'a eşitse kelimenin başlangıcı bulunmuş demektir. Bu durumda start_of_word değişkeni güncellenir.
  if char == target_end  and start_of_word != -1:  # Eğer döngüdeki karakter target_end işaretine eşitse ve start_of_word değişkeni -1 değilse (yani önceden bir başlangıç bulunmuşsa), kelimenin sonu bulunmuş demektir.
    word = story[start_of_word: i + 1] #(slicing) bu satır, story içerisindeki start_of_word indisinden başlayarak i+1 indisine kadar olan kısmı kesiyor ve word değişkenine atıyor
    words.add(word) # append yerine add kullanmamın sebebi aynı kelime tekrarı olsun istemem. unique words. Fakat liste yapılarında append kullanamadığımız için words attribute 'ünü "set" olarak tanımladık
    start_of_word = -1  #Bir kelimenin sonu bulunduktan sonra, start_of_word tekrar -1 olarak ayarlanır, böylece bir sonraki kelimenin başlangıcı aranabilir hale gelir.


answers = {}

for word in words:
  answer = input("Enter a word for " + word + " : ")
  answers[word] = answer


for word in words:
  story = story.replace(word,answers[word])  #Döngü içinde, bu satır, story adlı bir dize içindeki tüm geçişleri mevcut word ile answers sözlüğündeki ilgili değerle değiştirir. replace() fonksiyonu, word'ü story içindeki her örneğini bulur ve bunu answers[word] ile değiştirir.

print(story)
  
  
