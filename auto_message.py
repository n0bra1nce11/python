import pyautogui as pi
import time
messages=(
  "Hey! Did you know that the word 'gullible' isn't in the dictionary?",
  "If you were a vegetable, you’d be a cute-cumber!",
  "Knock knock. Who’s there? Interrupting cow. Interrupting cow wh- MOO!",
  "Do you ever just yawn and realize it’s not because you’re tired, but because your brain is running out of oxygen?",
  "Why don't you ever see elephants hiding in trees? Because they're so good at it!",
  "I just finished a puzzle in one week and the box said '2-4 years'!",
  "If two vegetarians argue, is it still called beef?",
  "I told my computer I needed a break, and now it won’t stop sending me Kit Kat ads.",
  "Did you know there are more planes in the ocean than submarines in the sky?",
  "If you get scared half to death twice, what happens?",
  "I named my dog ‘5 Miles’ so I can tell people I walk 5 miles every day.",
  "Do you think sand is called sand because it’s between the sea and land?",
  "If money doesn’t grow on trees, why do banks have branches?",
  "My bed is a magical place where I suddenly remember everything I was supposed to do.",
  "Why do they call it 'beauty sleep' when you wake up looking like a troll?",
  "If tomatoes are fruits, is ketchup a smoothie?",
  "Have you ever tried to clap with one hand? It’s pretty hard!",
  "Why does quicksand work so slowly?",
  "I'm reading a book about anti-gravity. It's impossible to put down!",
  "Do fish get thirsty?",
  "If you drop a bar of soap on the floor, is the floor clean or the soap dirty?",
  "Why do noses run but feet smell?",
  "What happens if you get a paper cut from a Get Well card?",
  "How do you handcuff a one-armed man?",
  "Why is it called 'after dark' when it’s really 'after light'?",
  "Do stairs go up or down?",
  "Why is the word 'abbreviated' so long?",
  "Can you cry underwater?",
  "If a turtle doesn’t have a shell, is it homeless or naked?",
)
time.sleep(5)
for message in messages:
    pi.typewrite(message)
    pi.press("enter")
    time.sleep(1)	#optional line
