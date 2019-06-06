# usr/bin/bash -tt
import os

from CabinNarrow import CabinNarrow 

class Airplane:
	
	def __init__(self, name, seatsNumber, maxLoadCapacity, maxDistance, maxSpeed, flightRange,     fuselageDiameter, cabinNarrow):
		self.name = name
		self.seatsNumber = seatsNumber
		self.maxLoadCapacity = maxLoadCapacity
		self.maxDistance = maxDistance
		self.maxSpeed = maxSpeed
		self.flightRange = flightRange
		self.fuselageDiameter = fuselageDiameter
		self.cabinNarrow = cabinNarrow
	
	def __repr__(self):
		return repr((self.name, self.seatsNumber, self.maxLoadCapacity, self.maxDistance, self.maxSpeed, self.flightRange, self.fuselageDiameter, self.cabinNarrow))	
		
	@property
	def get_name(self):
		return self.name		
	

	def set_name(self, x):
		self.name = x
		
	@property
	def get_seatsNumber(self):
		return self.seatsNumber

	def set_seatsNumber(self, x):
		self.seatsNumber = x
		
	@property
	def get_maxLoadCapacity(self):
		return self.maxLoadCapacity

	def set_maxLoadCapacity(self, x):
		self.maxLoadCapacity = x
		
	@property
	def get_maxDistance(self):
		return self.maxDistance

	def set_maxDistance(self, x):
		self.maxDistance = x
		
	@property
	def get_maxSpeed(self):
		return self.maxSpeed

	def set_maxSpeed(self, x):
		self.maxSpeed = x
		
	@property
	def get_flightRange(self):
		return self.flightRange

	def set_flightRange(self, x):
		self.flightRange = x
		
	@property
	def get_fuselageDiameter(self):
		return self.fuselageDiameter

	def set_fuselageDiameter(self, x):
		self.fuselageDiameter = x
		
	@property	
	def get_cabinNarrow(self):
		return self.cabinNarrow

	def set_cabinNarrow(self, x):
		self.cabinNarrow = x
		
def main():
	airplane = Airplane('Alexa-32', 120, 5000, 2000, 430, 1200, 9, CabinNarrow.SIXABREAST.value)
	
	print(airplane.get_name)
	airplane.set_name("NEwName")
	print(airplane.get_name)
	
	print(airplane.get_cabinNarrow)
	airplane.set_cabinNarrow(CabinNarrow.TWOABREAST.value)
	print(airplane.get_cabinNarrow)

if __name__ == "__main__": main()

os.system("PAUSE")
