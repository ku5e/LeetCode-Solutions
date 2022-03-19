#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
#from collections import Counter 

def findTheDifference(s, t):
	s = set(map(str, s))
	t = set(map(str, t))
	t.difference_update(s)
	return (t)

#	s = sum(map(ord, s))
#	t = sum(map(ord, t))
#	u = chr(t - s)
#	return u
	
#	new = t
#	s, t = Counter(s), Counter(t)
#	for i in new:
#		if s[i] != t[i]:
#			return i
	
#	orgSum = 0
#	for i in range(len(t)):
#		try:
#			orgSum += ord(t[i]) - ord(s[i])
#		except:
#			orgSum += ord(t[i])
#	return chr(orgSum)

	
#	orgSum = 0
#	for i in range(len(s)):
#		orgSum += ord(t[i]) - ord(s[i])
#	orgSum += ord(t[len(s)])
#	return chr(orgSum)

#	return chr(sum(map(ord, t)) - sum(map(ord, s)))

#	orgSum = 0
#	for letter in s:
#		orgSum -= ord(letter)
#	for letter in t:
#		orgSum += ord(letter)
#	return chr(orgSum)
#	
#	return (new[0])

#	original = list(map(str, s))
#	new = list(map(str, t))
#	
#	ans = set(new).difference(set(original))
#	
#	if len(ans) > 0:
#		return (list(ans)[0])
#	else:
#		for i in range(len(original)):
#			if new[i] in original:
#				new[i] = ''
#		new.sort(reverse = True)
#		return new	
	
#	for item in original:
#		new.remove(item)
#	
#	print(new[0])
	
print(findTheDifference('abd', 'adbc'))
print(findTheDifference("ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor", "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"))
