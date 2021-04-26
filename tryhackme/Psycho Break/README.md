# Psycho Break

```
export IP=10.10.67.176
```

# Task 1 - Recon

1. How many ports are open?

```
nmap -sV $IP

ANS = 3
```

2. What is the operating system that runs on the target machine?

```
Ubuntu
```

# Task 2 - Web

1. Key to the locker room

```
Browser => http://$IP
View Source
Browser => http://$IP/sadistRoom
Click link for key
ANS = 532219a04ab7a02b56faafbec1a4c1ea
```

2. Key to access the map

```
Decode this piece of text "Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv"
Browser => https://www.boxentriq.com/code-breaking/cipher-identifier
Identified as Atbash
ANS = Grant_me_access_to_the_map_please
```

3. The Keeper Key

```
View source
"Search through me and find it"
gobuster dir -u http://$IP/SafeHeaven -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,txt
/keeper
ANS = 48ee41458eb0b43bf82b986cecf3af01
```

4. What is the filename of the text file (without the extension)

```
Append shell=ls .. to URL
Hidden Directory = 680e89809965ec41e64dc7e447f175ab
ANS = you_made_it
```

# Task 3 - Help Mee

1. Who is locked up in the cell?

```
cat helpme.txt
ANS Joseph
```

2. There is something weird with the .wav file. What does it say?

```
Open file in Sonic Visualiser
Morse Code
ANS = SHOWME
```

3. What is the FTP Username?

```
steghide extract -sf Joseph_Oda.jpg
password - SHOWME
cat thankyou.txt
ANS = joseph
```

4. What is the FTP User Password?

```
As above
ANS = intotheterror445
```

# Task 4 - Crack it open

1. They key used by the program

```
Write a script to run all keywords in dictionary file against the program
ANS = kidman
```

2. What do the crazy long numbers mean when they're decrypted?

```
Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33
Mobile Numpad (T9 encryption)
ANS = kidmanspasswordissostrange
```

# Task 5 - Go Capture the Flag

1. user.txt

```
ssh to kidman@$IP
password = kidmanspasswordissostrange
cat user.txt
ANS = 4C72A4EF8E6FED69C72B4D58431C4254
```

2. root.txt 

```

```

3. [Bonus] Defeat Ruvik

```

```
