#install libraries
!pip install SpeechRecognition
!pip install PyAudio #Mostly error

#Another ways to Install PyAudio libraries
#1. Check your python version on cmd or any terminal
#2. write "python" on your cmd or any terminal, example:
C: Users\Bagas> Python

#3. After knowing the version of your python, download one of the file in this link
url = "https://www.lfd.uci.edu/~gohlke/pythonlibs/" #copy and paste this link

#4. The file that you may download have to meet the requirement of your python consol, example
# My python version is 3.8.5, so I just have two links that meet the requirement
PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
PyAudio‑0.2.11‑cp38‑cp38‑win32.whl
#so I'll download one of the file above

#5. After that, search "Run" in the search bar, then write %appdata%, and you may redirected into "Roaming" Directory File
#6. Then go back from the "Roaming" file, until you can see the the folders that included "Local", "LocalLow", and "Roaming"
#7. Choose "Local", and Then Click on Programs → Python →Python 38–32 → Scripts →Paste the downloaded file (PyAudio) inside the Scripts folder.
#8 After that, try to install the PyAudio libraries once again with this query
C: Users\Bagas> pip install C:\Users\Bagas\AppData\Local\Programs\Python\Python38-32\Scripts\PyAudio-0.2.11-cp38-cp38-win32.whl

#9. DONE! your PyAudio Libraries may work Now

#TIME TO CODE
#import packages from Libraries
import speech_recognition as sr

#SpeechRecognition with Microphone
def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio = r.listen(source)

        try:
            print("You have said: \n " + r.recognize_google(audio))

        except Exception as e:
            print("Error: " + str(e))

#SpeechRecognition with audiofile (.wav format)
def main():
    r = sr.Recognizer()

    with sr.WavFile('sample.wav') as source: #depends on your audiofile name
        audio = r.record(source)

        try:
            print("Transcription: \n " + r.recognize_google(audio))

        except LookupError:
            print("Error: " + str(e))

if __name__ == "__main__":
    main()
