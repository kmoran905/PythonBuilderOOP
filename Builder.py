from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# This a software design pattern called builder 
# that demonstrates the concept of building objects in a step-by-step basis


#Abstract class for a builder design pattern.
class Builder(ABC):
    @property
    @abstractmethod
    def outfit(self) -> None:
        pass
    @abstractmethod
    def helmet(self) -> None:
        pass

    @abstractmethod
    def sword(self) -> None:
        pass

    @abstractmethod
    def shield(self) -> None:
        pass

class Outfit():
    def __init__(self) -> None:
        #Array for adding elements of the equipment
        self.equipment = []
    
    def equip(self , equipment: Any ) -> None:
        self.equipment.append(equipment)
        
    #Function for printing the outfit   
    def print_equipment(self) -> None:
        for x in self.equipment:
            print(x)
        
        
        
class OutfitBuilder(Builder):

    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._outfit = Outfit()
    
    #Property annotation to set and get values of the names of the equipment   
    @property
    def outfit(self) -> Outfit:      
        outfit = self._outfit
        self.reset()
        return outfit
    
    #Defining the names of the equipment
    def helmet(self) -> None:
        self._outfit.equip("Demon Helmet")
     
    def sword(self) -> None:
        self._outfit.equip("Firesword")
    
    def shield(self) -> None:
        self._outfit.equip("Spiked Shield")
    
    #Function to build the entire equipment 
    def build_outfit(self) -> None:
        self.helmet()
        self.sword()
        self.shield()
       
    
if __name__ == "__main__":

    builder = OutfitBuilder()
    
    print("Outfit:")
    builder.build_outfit()
    builder.outfit.print_equipment()
    print("\n")
    
    
    
        
        
    
    
        
        