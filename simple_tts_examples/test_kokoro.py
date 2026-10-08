from kokoro import KPipeline
import sounddevice as sd

pipeline = KPipeline(lang_code="b")

text = "Greetings. How can i help?"
generator = pipeline(
    text= text,
    voice="bm_george",
    speed=1.0,
)
for graphemes, phonemes, audio in generator:
    sd.play(audio, samplerate=24000)
    sd.wait()
