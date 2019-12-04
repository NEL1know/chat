#讀取檔案
def read_file(filename):
	lines=[]
	# utf-8-sig 為另一種編碼,
	# 可自動將記事本等文檔編輯器自動存入的編碼訊息符號隱藏起來
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換格式
def convert(lines):
	A_wordcount = 0
	V_wordcount = 0
	A_imageCount = 0
	V_imageCount = 0
	A_stickerCount = 0
	V_stickerCount = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				if m == '圖片':
					A_imageCount += 1
				elif m == '貼圖':
					A_stickerCount +=1
				else:
					A_wordcount += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				if m == '圖片':
					V_imageCount += 1
				elif m == '貼圖':
					V_stickerCount +=1
				else:
					V_wordcount += len(m)
	print('Allen一共說了', A_wordcount, '個字')
	print('Allen一共貼了', A_imageCount, '張圖片')
	print('Allen一共用了', A_stickerCount, '個貼圖')

	print('Viki一共說了', V_wordcount, '個字')
	print('Viki一共貼了', V_imageCount, '張圖片')
	print('Viki一共用了', V_stickerCount, '個貼圖')
	

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	# write_file('output.txt', lines)

main()