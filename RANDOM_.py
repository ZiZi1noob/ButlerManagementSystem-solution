from phone_gen import PhoneNumber
import names
import random

from TIME_ import *
def phone_random(area=None):
    if area == None:
        phone_number = PhoneNumber("HK")
    else:
        phone_number = PhoneNumber(area)
    return phone_number.get_number()

def name_random():
    return names.get_full_name()

def msg_random():
    msg_clt = ["Can you help telling my neighbours to keep quiet", "Hi, my door doesn't close can you send someone to fix?", 'so noise',\
               "Here is a picture of the door", 's the meeting room available Friday ?', "Can you help telling my neighbours to keep quiet", "And they start the noise again...","Can someone help me look into this issue",\
                "there are some rubbish outsided my door in the halloway","please send someone to clean it", "Hi. Please let reception know that the person looking after my cat will be taking it out today. I am delayed in the uk, so they are taking it home with them.", "Hi, the waterpipe or not sure what it is above 9th floor or below 9th floor is making a very loud noise. Sounds like it has issues or something", "Hi, the elevator is not working…",\
                "Hi, the waterpipe or not sure what it is above 9th floor or below 9th floor is making a very loud noise. Sounds like it has issues or something", "The Bose surround sound system does not turn on and thus no sound from TV",\
                "No one contact yet", "Hi this is the second time i have found a screw on the floor of the playhouse", "no response",\
                "Hi, I have requested Jensen to deliver my ordered Dyson fan to my apartment on 9 jun 2023 pm.", "Hi I would like to change my email address contact",\
                "need help on TV", "need helps on WIFI", "Hi receiption. One of the air conditioners is not giving out cold air. Its never been used.", "The IKEA delivery will be there around 20 minutes from now on.\nSince I am not in the apartment now, they would like to leave the delivery at the reception.\nIs it okay?",\
                "I am Lisa, I need help", 'bathroom is leaking', 'HELP!', 'Please take my delivery!']
    
    return msg_clt[random.randrange(len(msg_clt))]

def random_data():
    
    generate_time = time_generator.time_ISO8601()
    generate_name = name_random()
    generate_tel = phone_random()
    msg = msg_random()
    random_num = random.randrange(50)
    if random_num == 20:
        return {
        "createdAt": generate_time
    }
    elif random_num == 30:
        return {
        'tel': generate_tel,
        'msg': msg
    }
    elif random_num == 40:
        return {
        'tel': generate_tel,
        "name": generate_name,
        'msg': msg
    }
    else:
        return {
            "createdAt": generate_time,
            "name": generate_name,
            'tel': generate_tel,
            'msg': msg
        }
    
def random_data_list():
    items_num = input('How many random items you wanna generate? I recommend to set a high value for proving incomplete items will be generated, like 600.')
    while 1:
        try:
            items_num = int(items_num)
            break
        except:
            try:
                items_num = int(input('Only accecpt int. Please try again.'))
                break
            except:
                pass
                
    result = []
    for i in range(items_num):
        result.append(random_data())
    return result
        
    