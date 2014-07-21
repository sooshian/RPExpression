#refer to http://www.nowamagic.net/librarys/veda/detail/2307

def ToRPExp(exp):
	ond_weights = {'+':1,'-':1,'*':2,'/':2,'(':0,')':0}
	stack = []
	result = ''
	number = ''
	for index in range(len(exp)):
		i = exp[index]
		if i.isdigit():
			number = number + i
		else:
			if number != '':
				result = result + ' ' + number
				number = ''
			if len(stack) == 0:
				stack.append(i)
			elif i == '(':
				stack.append(i)
			elif i == ')':
				length = len(stack)-1
				for k in range(length,-1,-1):
					if stack[k] == '(':
						stack.pop(k)
						break
					result = result + ' ' + stack.pop(k)

			elif ond_weights[stack[-1]] <= ond_weights[i]:
				stack.append(i)
			else:
				length = len(stack)-1
				for k in range(length,-1,-1):
					result = result + ' ' + stack.pop(k)
					
				stack.append(i)
	result = result + ' ' + number
	number = ''
	length = len(stack) - 1
	for k in range(length,-1,-1):
		result = result + ' ' + stack.pop(k)
	return result[1:]


exp = '9+(3-1)*3+10/2'
print ToRPExp(exp)
	
		