import os
Header = "Telefonnummer\tFacebookID\tVorname\tNachname\tGeschlecht\tWohnort\tLand\tBeziehungsstatus\tBeruf\tInfo\tGeburtstag\tE-Mail\n"

def fileid(List):
    global punctual
    global comma
    IdentifierArray = []
    identification_mark = 12
    i = 1
    if i != identification_mark:
        for line in List:
            Zeile = line
            break

    for char in Zeile:
        IdentifierArray.append(char)
    print(IdentifierArray)
    if IdentifierArray[12] == ":":
        punctual = 1
        comma = 0
    elif IdentifierArray[12] == ",":
        punctual = 0
        comma = 1
    else:
        print("No Valid seperator can be found")
        exit(0)




Ueberverzeichnis = os.listdir(fr"C:\Users\Blick\Downloads\Stuff\Tools\Big_Data\Facebook_RF\New_Data")
for dir in Ueberverzeichnis:
    Path = fr"C:\Users\Blick\PycharmProjects\pythonProject1\Database\{dir.upper()}"
    os.makedirs(Path)
    Countryfiles = os.listdir(fr"C:\Users\Blick\Downloads\Stuff\Tools\Big_Data\Facebook_RF\Data\{dir}")
    loop_files = 1
    for file in Countryfiles:
        Datei = open(fr"{Path}\{dir.upper()}_{loop_files}.txt", "w", encoding="utf-8")
        Datei.write(Header)
        with open(fr"C:\Users\Blick\Downloads\Stuff\Tools\Big_Data\Facebook_RF\Data\{dir}\{file}", "r", encoding="utf-8") as List:
            data = ""
            douplepointcounter = 0

            try:
                fileid(List)
                if punctual == 1:
                    for line in List:
                        for char in line:

                            if char == ":":
                                re_char = "\t"
                                douplepointcounter += 1
                                Datei.write(re_char)
                            if char == "\n":
                                if not douplepointcounter == 11:
                                    exit('Counting Error')
                                douplepointcounter = 0
                                Datei.write("\n")
                            if douplepointcounter > 11:
                                print('Out of Bound ocurred :', line)
                                exit(-1)
                            if char == "\r":
                                char = ""
                            else:
                                data += char.replace(":", "")
                                Datei.write(data)
                                data = ""


                elif comma == 1:
                    for line in List:
                        for char in line:
                            if char == ",":
                                re_char = "\t"
                                douplepointcounter += 1
                                Datei.write(re_char)
                            if char == "\n":
                                if not douplepointcounter == 11:
                                    exit('Counting Error')
                                douplepointcounter = 0
                                Datei.write("\n")
                            if douplepointcounter > 11:
                                print('Out of Bound ocurred :', line)
                                exit(-1)
                            else:
                                data += char
                                Datei.write(data)
                                data = ""

                else:
                    print("Read Error occured!!!")
                    exit()

            except UnicodeError:
                print(char)
                del char
            print("Yo, you have a Unicode Error")

        Datei.close()