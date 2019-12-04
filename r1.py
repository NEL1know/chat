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
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
		elif line == 'Tom':
			person = 'Tom'
		else:
			new.append(person + ': ' + line)
	return new

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()