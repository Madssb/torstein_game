import time
import sys #sys.exit() lives here
class player:
    def __init__(self,name) -> None:
        self.name = name
        
class IncomprehensibleManError(Exception):
    def __init__(self):
        self.message = "you are simply unable to comprehend this man and his features. You find yourself spiraling into an abyss of madness and oblivion."

tick = 0.6


class room:
    def __init__(self,interactable_objects,room_name,condition,exit):
        self.condition = condition
        self.condition_met = False
        self.exit = exit
        self.room_name = room_name
        self.objects = list(interactable_objects.keys())
        self.inspect_object = interactable_objects

    def print_objects(self):
        for object in self.objects:
            print(f">{object}")
        print("\n")
    
    def gameplay(self):
        print(f"You look around, and identify the following:")
        self.print_objects()
        room_exited = False
        while room_exited == False:
            time.sleep(2*tick)
            print("what do you wish to interact with?")
            #object_interacted_with = input("Make your choice:\t")
            while (object_interacted_with := input("give me an input: ")) not in self.objects:print(f" {object_interacted_with} is not found within {self.room_name}, try again.\n")

            if object_interacted_with == self.condition:
                self.condition_met = True
            
            if object_interacted_with == self.exit and self.condition_met:
                break

            interaction = self.inspect_object[object_interacted_with]
            print(f"{self.inspect_object[object_interacted_with]}\n")
            if "man" in interaction:
                print("you are simply unable to comprehend this man and his features. You find yourself spiraling into an abyss of madness and oblivion.")
                sys.exit()

"""chillefy"""
objects_in_chillefy ={
    "door to lillefy":"It's locked.",
    "couch":"You carefully search between the couch cusions. You find a key, which you decide to keep.",
    "blackboard":"You inspect the blackboard. It reads: 'Please resist your curiosity'.",
    "whiteboard":"you inspect the whiteboard. You find an illustration of a silhouette figure. It also reads:'He is incomprehensible'.",
    "table":"There originates a scent of beer from this table, and unsurprisingly, you find open cans of beer.",
    "window":"There is a thick fog outside, and you can't see very far. You look downwards towards the ground, the snow is churned up and matted, as if something heavy had fallen.",
    "phone": "Your phone is dead. you must find a charger somewhere",
    "Børge":"It feels as if he's watching my every move."
}

chillefy = room(objects_in_chillefy,"chillefy","couch","door to lillefy")
print("You wake up from the couch. It feels as if you've slept for days, and you recall neither your dreams, or the previous couple of days. The air is flat, and you're uncomfortable.")
chillefy.gameplay()

objects_in_lillefy = {
    "whiteboard":"You inspect the whiteboard. The writing is slanted and uneven, as if written in a hurry. It reads: 'I narrowly avoided contact, but she most unfortunately caught a glimpse. There was no amount of persuation or actions capable of stopping her, may she rest in peace. In the meantime, i seek shelter behind closed doors.'.", 
    "Magnus's desk":"You inspect Magnus's desk. You find a crudely painted cow on a canvas, along with some lab goggles, which have their vision obscured by stickers. You decide to keep the goggles.",
    "door to theta":"Upon closer inspection, you find that the door to theta simply can't be locked. With a soft push, you carefully open the door, and are immediately confronted by the presence of a man.",
    "mannequinn":"He is dressed like boba fett. It is a comforting presence in a despairing atmosphere.",
    "blackboard":"You inspect the blackboard. It reads: 'I sense his presence, i hear his very existence. This is no longer a safe place, he has made it inside. I am making a run for it, an attempt to leave by whatever means nescesary. you're on your own. good luck.'.",
    "door to staircase":"The door is locked from the inside. You are confronted with an acute sense of dread as to what awaits on the other end. You decide to postpone this dangerous attempt to head towards storefy auditorium.",
    "door to piano room":"He is playing the piano, you decide to listen in. you listen for what feels like 1 minute, until you muster the strength to break away from his trance. You realize you've been listening for 5 hours.",
    "my desk":"You find your phone charger. As your phone turns on, you confirm that you've been sleeping for 3 days. You've recieved messages, they're entirely incoherent. Your internet access is also for the time being entirely nonexistent.",


}

lillefy = room(objects_in_lillefy,"lillefy","Magnus's desk","door to staircase")
print("You use the key found inbetween the couch cusions to unlock the door to lillefy.\n")
time.sleep(1)
print("As you enter, you confront the uncanney atmosphere. Your surroundings feel decieving, and you sense a dangerous presence.")
lillefy.gameplay()

print("Prior to exiting, you put your ear up towards the door, sensing some activity outside. Just prior to unlocking the door, you equip Magnus's goggles as a precautionary measure to avoid any potential line of sight with the man.")
print("You step into the staircase, effectively blindfolded. You hear a deep and guttural sound, as if the very fabric of reality is being torn apart, resonating deep within your chest. You feel small and insignificant in the face of its power.")
print("Sensing that this is coming from a region somewhat downwards in the staircase, and not wanting to push your luck, you head upwards towards storefy.")
print("You make it safely inside Store fysiske auditorium, and quickly barricade the door, seeing as it has no locking capabilities. Although not physically hurt, the staircase encountered has left you weakened.")
objects_in_storefy = {
    "door to staircase":"you press your ear in towards the door. You hear a deep droning sound, and you sense him approaching. There is no way in hell you're going back down.",
    "door towards Laplace":"The door is securely lockded, neither the button, or the mechanical lock appears to function.",
    "Even & Torstein's former AST2000 office":"You climb the staircase upwards to the Even Tobias & Torstein AST2000 room. You find a note, it reads: 'I have yet to find survivors, and i admittedly haven't been looking too much. Come find me in the section for theoretical physics, if i have survived, that is. I  will be heading there, as ideem an escape attempt too dangerous.'",
    "door towards theory":"Your encounter in the staircase has left you weakened, the door is barely budging from the force you manage to exert.",
    "whiteboard":"You inspect the whiteboard. It reads: 'He attacks the senses, and i somehow detect his presence even in the absence of all of them.' "
}hyh