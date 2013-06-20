n = 'abcdefafdasdfasdfljlkj'
m = 'asdf'

def mn_anagram(n, m):
	len_m = len(m)
	len_n = len(n)
	
	cnt_m = {}
	for i in range(len_m):
		cnt_m.setdefault(m[i], 0)
		cnt_m[m[i]] += 1
	
	for i in range(len_n):
		head = i - len_m + 1
		if n[i] in cnt_m: 
			cnt_m[n[i]] -= 1
			if n[head] in cnt_m:
				for m_ch, cnt in cnt_m.items():
					if cnt != 0: break
				else:
					print head 
					for j in range(head, i + 1):
						print n[j],
					print
		if n[head] in cnt_m: cnt_m[n[head]] += 1

print m
print n
mn_anagram(n, m)
