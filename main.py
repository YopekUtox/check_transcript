import glob

samples_path = ""       # Paste here directory to wav (samples) files folder.
transcription_path = ""   # Paste the path to the.txt file here with the transcription like: C:\\Users\\YourName\\....\\transcription.txt

samples_path = samples_path + "*"

x = 0
not_found_wav = []

while True:
    with open(transcription_path) as transcription_list:
        try:
            exist_check = transcription_list.read().split("\n")[x]
        except(IndexError):
            if x == 0:
                print("Probably valid transcription file not found !")
            elif len(not_found_wav) == 0 and 0 <= x:
                print("All files are in transcription !")
            else:
                print("These files were not found in the transcription file: " + str(not_found_wav))
            exit()

        if exist_check in glob.glob(samples_path):
            ''
        else:
            not_found_wav.append(exist_check)

        x = x + 1
