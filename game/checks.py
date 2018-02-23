def check_if_in_box(ctr,x,y):
	if ctr == 0 and (x<2 or y<2 or y>=12 or x>=12):
		return 1 
	elif ctr == 1 and (x<14 or y<2 or y>=12 or x>=24):
		return 1
	else:
		return 0

def check_if_ship_present(ctr, x, y, rect, rect1):
	for i in rect[ctr]:
		if [x,y] not in i:
			continue
		else:
			return 1
	if [x,y] not in rect1:
		return 0
	else:
		return 1

def check_if_diagonal(x,y,rect1):
	if abs(rect1[0][0]-x) == 1 and abs(y-rect1[0][1]) == 1:
		return 1
	else: 
		return 0

def check_if_valid(x,y,rect1):
	if check_if_diagonal(x,y,rect1) == 1:
		return 0
	elif (abs(x - rect1[0][0]) == 1 or abs(y - rect1[0][1]) == 1):
		return 1
	else:
		return 0
		
def check_orientation((x2,y2),(x1,y1)):
	if abs(x2-x1) == 1:
		return 0
	else:
		return 1
		
def check_if_horizontal(x,y,rect1,count):
	if (abs(x - rect1[0][0]) == 1 and abs(y - rect1[0][1]) == 0) or (abs(x - rect1[count-1][0]) == 1 and abs(y-rect1[count-1][1]) == 0):
		return 1
	else: 
		return 0

def check_if_vertical(x,y,rect1,count):
	if (abs(x - rect1[0][0]) == 0 and abs(y - rect1[0][1]) == 1) or (abs(x - rect1[count-1][0]) == 0 and abs(y-rect1[count-1][1]) == 1):
		return 1
	else:
		return 0

def check_if_attacked(ctr,x,y,moves_of_p1,moves_of_p2):
	if ctr == 1:
		if [x,y] not in moves_of_p1:
			return 0
		else:
			return 1
	elif ctr == 2:
		if [x,y] not in moves_of_p2:
			return 0
		else:
			return 1
			
def check_if_win(rect,ctr):
	if ctr == 2: 
		if rect[0][0][0][0] == 0 and rect[0][0][0][1] == 0 and rect[0][1][0][0] == 0 and rect[0][1][0][1] == 0 and rect[0][2][0][0] == 0 and rect[0][2][0][1] == 0 and rect[0][3][0][0] == 0 and rect[0][3][0][1] == 0 and rect[0][4][0][0] == 0 and rect[0][4][0][1] == 0:
			return 1
	elif ctr == 1:
		if (rect[1][0][0][0] == 0 and rect[1][0][0][1] == 0) and (rect[1][1][0][0] == 0 and rect[1][1][0][1] == 0) and (rect[1][2][0][0] == 0 and rect[1][2][0][1] == 0) and (rect[1][3][0][0] == 0 and rect[1][3][0][1] == 0)and (rect[1][4][0][0] == 0 and rect[1][4][0][1] == 0):
			return 1
