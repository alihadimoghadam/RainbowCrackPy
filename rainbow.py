from hashlib import sha256
import csv

def hash_password_hack(input_file_name, output_file_name) :
    # reading input file.
    with open(input_file_name) as fin :
        reader = csv.reader(fin)
        # hp is a dictionary of hashes ranged from 1000 to 9999
        # new_hp is a dictionary of names and passwords that are hacked
        hp = {}
        new_hp = {}
        # in halghe hash haye range 1000 ta 9999 ra vared dict (hp) mikonad.
        # this loop inserts hashes from 1000 to 9999 to hp dictionary
        for i in range(1000, 9999) :
            hash_jadid = sha256(str(i).encode())
            hash_jadid = hash_jadid.hexdigest()
            hp[hash_jadid] = i
        # halghe aval name va hash ra khat be khat az file input mikhanad. halghe dovom check mikonad hash haye mojod
        # the first loop will check the hashes in the input file and the second loop will check the hashes in the dictionary
        # compares the hashes in the hp dictionary if they are the same
        # names are inserted to a dictionary named new_hp
        for radif in reader :
            name = radif[0]
            hash_in_reader = radif[1]
            for hach_in_hp in hp.keys() :
                if hash_in_reader == hach_in_hp :
                    new_hp[name] = hp.get(hach_in_hp)
    # with the code below, the passwords and names we've hacked are inserted into a new file
    with open(output_file_name, 'w') as out :
        count = 0
        for names in new_hp :
            count += 1
            if count == 1 :
                out.write(names + ',' + str(new_hp.get(names)))
            else :
                out.write('\n' + names + ',' + str(new_hp.get(names)))


