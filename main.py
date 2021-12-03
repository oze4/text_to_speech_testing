import gtts
import playsound
# Box allows us to "dot-source" into a dict. ex: `dict.prop` vs `dict["prop"]`
import box

"""
chunk_str : takes a string and returns it in "n" number of chunks.
@returns a list of strings
"""
def chunk_str(string: str, n_chunks: int): 
  s, n = string, n_chunks
  return [s[i:i+n] for i in range(0, len(s), n)]

# Script variables

TEXT = "Hello world! Welcome to the matrix! Would you like the red or blue pill?"
OUTPUT_FILE_PATH = "test.mp3"
LANGUAGE = "en"
IS_SLOW_SPEED = False
ACCENTS = box.Box({ # https://gtts.readthedocs.io/en/latest/module.html#localized-accents
  "indian": "co.in",
  "australian": "com.au",
  "british": "co.uk",
  "american": "com",
  "canadian": "ca",
  "irish": "ie",
  "south_african": "co.za"
})

# Main

mp3 = gtts.gTTS(
  text=TEXT, 
  lang=LANGUAGE,
  tld=ACCENTS.american,
  slow=IS_SLOW_SPEED
)

mp3.save(OUTPUT_FILE_PATH)
playsound.playsound(sound=OUTPUT_FILE_PATH)