# Cassie Chong 1005301 50.042 Lab2 Part 1

# Import

Counter to make counting easier,\
copy to keep original file safe (in case)

```python
from collections import Counter
import copy
```

  

# Open file and new file to write to

```python

file = open('story_cipher.txt', 'r')
fout = open('story_text.txt', 'w', encoding='utf-8')

```

# Get cipher

As a string. Then make an array to change it as strings are immutable.

```python
cipher = file.read()
cp = copy.deepcopy(cipher)
cipherl = list(cp)
```

# Get char count

Only count if the character is an alphabet. Ignore if it is whitespace or a punctuation mark.

```python

charcount = Counter(cipher)
total = 0
for chr in charcount:
	if chr.isalpha():
	total += charcount[chr]
print(total)
```

```
2655
```

# Get a dictionary of (char, freq)

Use `total` and `charcount` found earlier to do this.

```python

frequency = {}
for chr in charcount:
	if chr.isalpha():
		frequency[chr] = (charcount[chr] / total) * 100
	else:
		frequency[chr] = 0 # dummy value

print(frequency)

```

```

{'M': 1.8832391713747645, 'X': 6.0263653483992465, 'Q': 8.022598870056497, 'J': 9.905838041431261, ' ': 0, 'Y': 8.625235404896422, 'I': 7.457627118644068, 'O': 2.1845574387947266, 'C': 2.6365348399246704, 'F': 1.6195856873822974, 'E': 7.758945386064029, 'W': 2.6741996233521657, 'U': 11.487758945386064, 'H': 4.934086629001883, '.': 0, 'V': 1.8832391713747645, 'B': 3.84180790960452, 'D': 7.721280602636535, ',': 0, 'L': 1.0922787193973633, 'R': 1.3182674199623352, 'T': 3.6911487758945385, 'S': 2.297551789077213, 'K': 1.92090395480226, 'A': 0.7532956685499058, 'N': 0.11299435028248588, 'Z': 0.11299435028248588, 'P': 0.03766478342749529}

```

# Then sort.

```python

sorted_freq = {k:v for k,v in sorted(frequency.items(), key=lambda item:item[1] , reverse=True)}

print(sorted_freq)

```

```

{'U': 11.487758945386064, 'J': 9.905838041431261, 'Y': 8.625235404896422, 'Q': 8.022598870056497, 'E': 7.758945386064029, 'D': 7.721280602636535, 'I': 7.457627118644068, 'X': 6.0263653483992465, 'H': 4.934086629001883, 'B': 3.84180790960452, 'T': 3.6911487758945385, 'W': 2.6741996233521657, 'C': 2.6365348399246704, 'S': 2.297551789077213, 'O': 2.1845574387947266, 'K': 1.92090395480226, 'M': 1.8832391713747645, 'V': 1.8832391713747645, 'F': 1.6195856873822974, 'R': 1.3182674199623352, 'L': 1.0922787193973633, 'A': 0.7532956685499058, 'N': 0.11299435028248588, 'Z': 0.11299435028248588, 'P': 0.03766478342749529, ' ': 0, '.': 0, ',': 0}

```

  

# Start analysis

## Function to replace

I found that `.replace()` cannot replace by characters. I will do it iteratively through a character array by reassignment.

Make a function to do this.

```python

def rep(a, b, txt):
	for i in range(0, len(txt)):
		if txt[i] == a:
			txt[i] = b
```

## 2 Characters with highest frequencies
Let

| Ciphertext | Plaintext |
| ---------- | --------- |
| U          | e         |
| J          | t         | 

As these are the highest frequencies found.
Then do it.

```python
rep('U', 'e', cipherl)
rep('J', 't', cipherl)
print(''.join(cipherl))

```

First bit of output:

```

MXQt YI IOCFXEWeQH. VEH Q BEEEEEDW, BEEEDW tYCe Y XQLe DeLeH REtXeHeT eDWQWYDW COIeBV YD tXYI VHQDSXYIe. Y TYT DEt KDTeHItQDT MXQt Yt YI. DEM tXQt tXe IXEM YI XQLYDW YtI BQIt IeQIED, Y TeSYTeT tE VYDQBBO WYLe YD, WYLe IOCFXEWeQH Q tHO VHEC tXe LeHO ItQHt. Y MEDTeHeT XEM XQLe Y CYIIeT EKt ED tXe QDYCe EV tXe TeSQTe QBB tXeIe OeQHI. Y XEDeItBO TYT DEt ADEM MXQt tE eNFeSt MQtSXYDW tXe LeHO VYHIt eFYIETe ADEMYDW QRIEBKteBO DEtXYDW QREKt tXe VHQDSXYIe. tXe IXEM tEOeT MYtX CO eCEtYEDI IE CKSX YD tXQt EFeDYDW IetFYeSe. Yt eDTeT KF ReYDW EDe EV tXe CEIt BYVe QVVYHCYDW IXEMI EKt tXeHe. Q ItKDDYDW TYIFBQO EV YTYESO QDT QStYED tXQt YI REtX SXQHCYDW QDT SQFtYLQtYDW. Yt YI SEDVYTeDt YD YtI ItHeDWtXI QDT FQHQTeI YtI MeQADeIIeI FHEKTBO, Q IXEM tXQt YI REtX QBB ItOBe QDT QBB IKRItQDSe.

```


## Next 4

Y, Q, E, D frequencies are close, could be a, o, i, n\
Q and Y can be standalone words, probably a and i\
E and D: E mostly seen between letters. Repeated E sighted. Repeated n unlikely, so E => o
==> D => n

| Ciphertext | Plaintext |
| ---------- | --------- |
| Q          | a         |
| Y          | i         |
| E          | o         |
| D          | n         | 

So replace and see again.

```python

rep('Q', 'a', cipherl)
rep('Y', 'i', cipherl)
rep('E', 'o', cipherl)
rep('D', 'n', cipherl)
print(''.join(cipherl))

```

```

MXat iI IOCFXoWeaH. VoH a BooooonW, BooonW tiCe i XaLe neLeH RotXeHeT enWaWinW COIeBV in tXiI VHanSXiIe. i TiT not KnTeHItanT MXat it iI. noM tXat tXe IXoM iI XaLinW itI BaIt IeaIon, i TeSiTeT to VinaBBO WiLe in, WiLe IOCFXoWeaH a tHO VHoC tXe LeHO ItaHt. i MonTeHeT XoM XaLe i CiIIeT oKt on tXe aniCe oV tXe TeSaTe aBB tXeIe OeaHI. i XoneItBO TiT not AnoM MXat to eNFeSt MatSXinW tXe LeHO ViHIt eFiIoTe AnoMinW aRIoBKteBO notXinW aRoKt tXe VHanSXiIe. tXe IXoM toOeT MitX CO eCotionI Io CKSX in tXat oFeninW IetFieSe. it enTeT KF ReinW one oV tXe CoIt BiVe aVViHCinW IXoMI oKt tXeHe.

```


## Next 3

Next highest frequencies: I, X, H ==> s, r, h\
I likely s as double II is seen, and some iI is seen, likely 'is'\
H is then likely r as several words ended with H and words are less likely to end with h\
Then X is h.

| Ciphertext | Plaintext |
| ---------- | --------- |
| I          | s         |
| X          | h         |
| H          | r         | 

So replace and see again.

```python

rep('I', 's', cipherl)
rep('X', 'h', cipherl)
rep('H', 'r', cipherl)
print(''.join(cipherl))

```

```

Mhat is sOCFhoWear. Vor a BooooonW, BooonW tiCe i haLe neLer RothereT enWaWinW COseBV in this VranShise. i TiT not KnTerstanT Mhat it is. noM that the shoM is haLinW its Bast season, i TeSiTeT to VinaBBO WiLe in, WiLe sOCFhoWear a trO VroC the LerO start. i MonTereT hoM haLe i CisseT oKt on the aniCe oV the TeSaTe aBB these Oears. i honestBO TiT not AnoM Mhat to eNFeSt MatShinW the LerO Virst eFisoTe AnoMinW aRsoBKteBO nothinW aRoKt the VranShise. the shoM toOeT Mith CO eCotions so CKSh in that oFeninW setFieSe. it enTeT KF ReinW one oV the Cost BiVe aVVirCinW shoMs oKt there. a stKnninW TisFBaO oV iTioSO anT aStion that is Roth SharCinW anT SaFtiLatinW.

```

## Words are already visible. Substitute obvious.

| Ciphertext | Plaintext |
| ---------- | --------- |
| V          | f         |
| S          | c         |
| K          | u         |
| T          | d         |
| M          | w         |
| B          | l         |
| O          | y         |
| W          | g         |
| L          | v         |
| R          | b         |
| F          | p         |
| C          | m         |
| Z          | j         |
| N          | x         |
| A          | k         | 

```python

rep('V', 'f', cipherl)
rep('S', 'c', cipherl)
rep('K', 'u', cipherl)
rep('T', 'd', cipherl)
rep('M', 'w', cipherl)
rep('B', 'l', cipherl)
rep('O', 'y', cipherl)
rep('W', 'g', cipherl)
rep('L', 'v', cipherl)
rep('R', 'b', cipherl)
rep('F', 'p', cipherl)
rep('C', 'm', cipherl)
rep('Z', 'j', cipherl)
rep('N', 'x', cipherl)
rep('A', 'k', cipherl)
print(''.join(cipherl))

```

```

what is symphogear. for a looooong, looong time i have never bothered engaging myself in this franchise. i did not understand what it is. now that the show is having its last season, i decided to finally give in, give symphogear a try from the very start. i wondered how have i missed out on the anime of the decade all these years. i honestly did not know what to expect watching the very first episode knowing absolutely nothing about the franchise. the show toyed with my emotions so much in that opening setpiece. it ended up being one of the most life affirming shows out there.

```

Amazing. Hold on what's at the back?

```

so what is symphogear. it is a hybrid idol anime. it is an anime about fisting. it is five seasons and seven years long and has captivated the hearts of many. but most importantly, it is believing in the song of your heart.

```

It is a what??? Am interested who wrote this. Should I also give symphogear a try?

  

# Write to file

```python

text = ''.join(cipherl)
fout.write(text)

file.close()
fout.close()

```

Now I have another file with the decrypted text.
I also have new knowledge about what symphogear is.

  

# Further

For avoiding confusion, I used lower case letters for decrypted plaintext while ignoring grammar conventions.