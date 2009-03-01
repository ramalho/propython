# hanoi

def move_tower(height, from_pin, to_pin, using_pin):

	def move_disk(from_pin, to_pin):
		print from_pin, '->', to_pin
		
	if height > 0:
		move_tower(height - 1, from_pin, using_pin, to_pin)
		move_disk(from_pin, to_pin)
		move_tower(height - 1, using_pin, to_pin, from_pin)
		
if __name__ == '__main__':

	import sys
	
	print 'Tower of Hanoi'
	
	try:
	    height = int(sys.argv[1])
	except (IndexError, ValueError):    
		print 'Usage: %s <number_of_disks>' % sys.argv[0]  
		raise SystemExit
	    
	move_tower(height, 1, 3, 2)
	
	    
	
	
	