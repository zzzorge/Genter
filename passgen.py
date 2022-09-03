#Imports
import base64 as b64
import beaupy
import env
from hashlib import blake2b
import json
from ocryptor import oCrypt
import os
import secrets
import sqlite3
from string import ascii_lowercase, ascii_uppercase, digits


#AES stoof
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


#Languages
uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[]{},.;:-_/\\+?*|`€≡‗"
unicode = "¡¢£¤¥¦§¨©ª«¬®™️¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐıæ𐐘𐑀ඞඕᔕ"
emojis = "⚔☣️⚛️〰️🗝️🔒⛓️✨🫠🫧🫥💢"
ascii_boxes = "░▒▓█▄▀■"
ascii_draw_box = "╣╗╝┴┬╩╦═╬"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
chinese = "诶比西迪伊尺杰大水开勒哦屁吉吾儿诶比西迪伊弗吉尺艾弗吉杰屁吉吾儿?八九十开勒马娜哦月人马娜口"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portuL = "ãáàâçéêíõóôúü"
portuU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
hindi = "ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऽॐॠॡ।॥०१२३४५६७८९॰ॲॳॴॵॶॷॹॺॻॼॽॾॿೱೲऀँंःऺऻ़ािीुूृॄॅॆेैॉॊोौ्ॎॏ॒॑॓॔ॕॖॗॢॣ"
arabic = "شسژزڑرذڈدخحچجثٹتپبآاےیھہوںنملگکقفغعظطضصءئؤڙڐٿ٘ ًَُِّٰٗ؟،۰۱۲۳۴۵۶۷۸۹"
amharic = "ሀሁሂሃሄህሆሎልሌላሊሉለሐሑሒሓሔሕሖሞምሜማሚሙመሠሡሢሣሤሥሦሮርሬራሪሩረሰሱሲሳሴስሶሾሽሼሻሺሹሸቀቁቂቃቄቅቆቦብቤባቢቡበቨቩቪቫቬቭቮቶትቴታቲቱተቸቹቺቻቼችቾኆኅኄኃኂኁኀነኑኒናኔንኖኞኝኜኛኚኙኘአኡኢኣኤእኦኮክኬካኪኩከኸኹኺኻኼኽኾዎውዌዋዊዉወዐዑዒዓዔዕዖዞዝዜዛዚዙዘዠዡዢዣዤዥዦዮይዬያዪዩየደዱዲዳዴድዶጆጅጄጃጂጁጀገጉጊጋጌግጎጦጥጤጣጢጡጠጨጩጪጫጬጭጮጶጵጴጳጲጱጰጸጹጺጻጼጽጾፆፅፄፃፂፁፀፈፉፊፋፌፍፎፖፕፔፓፒፑፐ፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼፡።፣፤፥"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.



##-------------- Functions --------------##
def banner():
    return """
        ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
        ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
        ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                           
      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """





# CLEANING
## ------------------------------------------------------------------------ ##
def clear():
    os.system('cls||clear')


# Cleaning up files.
def cleanup():
    # Remove current pwords.pgen db.
    if os.path.isfile('pwords.pgen'):
        os.remove('pwords.pgen')
    else:
        pass

    # Rename new database to the name of the original database.
    if os.path.isfile('pwords2.pgen'):
        os.rename('pwords2.pgen', 'pwords.pgen')
    else:
        pass

    # Renames vne.py to env.py.
    if os.path.isfile('vne.py'):
        os.rename('vne.py', 'env.py')
        print("Please remove/delete your .so/.pyd file and use the new env.py file instead.\nYou can obfuscate and cythonize the new env.py file.")
    else:
        pass
## ------------------------------------------------------------------------ ##
  





# ENCRYPTION STUFF
## ------------------------------------------------------------------------ ##
#Decrypting old encrypted passwords in pasgen.pgen.
def stringD_lst(passw):
    import env
    salt = str(env.SALT)
    ev_password = str(env.PASS)

    passwdE = b64.b64decode(passw) # Decoding the base64 bytes and giving me the aes data to decrypt.
    try:
        key = PBKDF2(ev_password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, passwdE[:AES.block_size])
        d_cipher_data = unpad(cipher.decrypt(passwdE[AES.block_size:]), AES.block_size)
    except Exception as e:
        strd_e = f'The provided credentials do not match what was was used to encrypt the data...\nError: {e}'
        raise Exception(strd_e) from None
    return d_cipher_data.decode('unicode-escape')



# Encrypting the passwords with new encryption before rename/cleanup.
def stringE2(passw):
    import vne
    vne_salt = str(vne.SALT)
    vne_ev_password = str(vne.PASS)

    vne_key = PBKDF2(vne_ev_password, vne_salt, dkLen=32)
    vne_rb = get_random_bytes(AES.block_size)
    vne_cipher = AES.new(vne_key, AES.MODE_CBC, vne_rb)
    vne_cipher_data = b64.b64encode(vne_rb + vne_cipher.encrypt(pad(passw.encode('unicode_escape'), AES.block_size)))
    return vne_cipher_data.decode()



# Encrypting the passwords with new encryption after rename/cleanup.
def stringE(password):
    import env
    env_salt = str(env.SALT)
    env_ev_password = str(env.PASS)

    env_key = PBKDF2(env_ev_password, env_salt, dkLen=32)
    env_rb = get_random_bytes(AES.block_size)
    env_cipher = AES.new(env_key, AES.MODE_CBC, env_rb)
    env_cipher_data = b64.b64encode(env_rb + env_cipher.encrypt(pad(password.encode('unicode_escape'), AES.block_size)))
    return env_cipher_data.decode()



# Decrypting the new encryption before rename/cleanup.
def stringD2(web):
    import vne
    vne_salt = str(vne.SALT)
    vne_ev_password = str(vne.PASS)

    database = sqlite3.connect('pwords2.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables WHERE website LIKE '{web}'")

    if vne_b64passwd := c.fetchone():
        vne_passwdE = b64.b64decode(vne_b64passwd[0])
        try:
            vne_key = PBKDF2(vne_ev_password, vne_salt, dkLen=32)
            vne_cipher = AES.new(vne_key, AES.MODE_CBC, vne_passwdE[:AES.block_size])
            vne_d_cipher_data = unpad(vne_cipher.decrypt(vne_passwdE[AES.block_size:]), AES.block_size)
        except Exception as e:
            strd_e = f'The provided credentials do not match what was was used to encrypt the data...\nError: {e}'
            raise Exception(strd_e) from None
        return print(f"Password for {web}: {vne_d_cipher_data.decode('unicode-escape')}")
    else:
        print('Oof..nothing here but us foxos...')



# Decrypting the new encryption after rename.
def stringD2a(web):
    import env
    env_salt = str(env.SALT)
    env_ev_password = str(env.PASS)

    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables WHERE website LIKE '{web}'")

    if env_b64passwd := c.fetchone():
        env_passwdE = b64.b64decode(env_b64passwd[0])
        try:
            env_key = PBKDF2(env_ev_password, env_salt, dkLen=32)
            env_cipher = AES.new(env_key, AES.MODE_CBC, env_passwdE[:AES.block_size])
            env_d_cipher_data = unpad(env_cipher.decrypt(env_passwdE[AES.block_size:]), AES.block_size)
        except Exception as e:
            strd_e = f'The provided credentials do not match what was was used to encrypt the data...\nError: {e}'
            raise Exception(strd_e) from None
        return print(f"Password for {web}: {env_d_cipher_data.decode('unicode-escape')}")
    else:
        print('Oof..nothing here but us foxos...')



# Changing encryption credentials
def change():
    alphabet = uppercase_letters + lowercase_letters + numbers + symbols + unicode
    SALT = get_random_bytes(1024)
    PASS = ''.join(secrets.choice(alphabet) for _ in range(32))

    with open("vne.py", "w") as f:
        f.write(f"SALT={SALT}\n")
        f.write(f'PASS="{PASS}"\n')
        f.write('FLAG="v1"')
        f.close()



# Add and remove data from database.
def add_data(website, passwd, notes):
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    if website in dlist:
        return print(f'[Warning] - A website entry with the name of "{website}" exists in database already.\nTo avoid breaking the "reading passwords" functionality, please change the name slightly.')
    if not website:
        return print('I need a domain/website to add to the database...\n[Error]: "web" can not be empty.')
    else:
        c.execute(f"INSERT INTO pwd_tables VALUES ('{website}', '{stringE(passwd)}', '{notes}')")
        database.commit()
        database.close()
        return print(f'"{website}" and your password has been stored/saved to the database!')


def rmv_data(website):
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    if website in dlist:
        c.execute(f"DELETE FROM pwd_tables WHERE website LIKE '{website}'")
        database.commit()
        database.close()
        return print(f'"{website}" has been removed from the database!')
    else:
        return print(f'"{website}" is not a valid option or does not exist.')
## ------------------------------------------------------------------------ ##





# OTHER STUFF
## ------------------------------------------------------------------------ ##
# Hashing
def hash(password: str):
    alphabet = uppercase_letters + lowercase_letters + numbers
    
    while True:
        try:
            option = int(input(f"{banner()}\n\nHow do you want to make a key for hashing?\n\n1. Custom Key?\n2. Generate Key?\n3. Quit?\n\nEnter: "))
        except Exception as e:
            clear()
            print(f'Value given is not an integer.\nError: {e}\n\n')
            input('Press "enter" to continue...')
            clear()
            continue


        if option == 1:
            clear()
            print('[Note]: Press "q" to go back.\n')
            c_key = input('Enter/Load key to use for hashing: ')
            if c_key.lower() == 'q':
                clear()
                continue

            try:
                salt = input('Enter phrase for salting (16 letters max): ')
                if salt.lower() == 'q':
                    clear()
                    continue

                salt = bytes(salt, 'utf-8')
                clear()
                result1 = blake2b(bytes(password, 'utf-8'), key=bytes(c_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            except Exception as e:
                clear()
                print(f'Oops..An error has occured.\n[Error]: {e}')
                input('\nPress "enter" to continue...')
                clear()
                continue

            print(f'Password: {password}  |  Hash: {result1}\nSalt: {salt.decode()}  |  Key: {c_key}\n')
            return result1


        if option == 2:
            clear()
            gen_key = ''.join(secrets.choice(alphabet) for _ in range(25))
            salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8')
            
            result2 = blake2b(bytes(password, 'utf-8'), key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            print(f'Password: {password}  |  Hash: {result2}\nSalt: {salt.decode()}  |  Key: {gen_key}\n')
            return result2

        if option == 3:
            clear()
            return None

        elif option < 1 or option > 3:
            clear()
            print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
            input('Press "enter" to continue...')
            clear()




# For automatically hashing the newly generated password in the main function.
def d_conv(password):
    alphabet = uppercase_letters + lowercase_letters + numbers
    clear()
    
    default_key = ''.join(secrets.choice(alphabet) for _ in range(25)) #Can be as long as you want.
    salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8') #MUST be 16 or less.
    
    result = blake2b(bytes(password, 'utf-8'), key=bytes(default_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
    return result, salt, default_key


# config.json file loading.
def j_load():
    with open('config.json') as f:
        data = json.load(f)
        option = data['options_flag']
    return option


# Showing contents of pass.txt and clearing it.
def show_pass():
    clear()
    with open('pass.txt', 'r') as f:
        result = f.read()
        if not result:
            return None
        else:
            return result
        
def clr_pass():
    clear()
    with open('pass.txt', 'r+') as f:
        f.truncate(0)




# Reading passwords functinality.
def domains():
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    c.execute(f"SELECT notes FROM pwd_tables")
    notes = c.fetchall()

    if not sites:
        print("Hmmm...Maybe you should add something to the database first. ^-^")
    else:
        for d,n in zip(dlist, notes):
            with open('.lst', 'a') as f:
                f.writelines(f"{d}\t{n}\n")


def read():
    clear()
    domains()
    try:
        with open(".lst", "r+") as f:
            data = f.read()
            print(data)
            f.truncate(0)
            f.close()

        os.remove(".lst")
        web_to_get = input('-----------------------------------------------------\nPress "q" to go back/quit.\n\nWebsite domain/name for password: ')
        clear()
        if web_to_get.lower() == 'q':
            return web_to_get.lower()
        else:
            if os.path.isfile('vne.py'):
                stringD2(web_to_get.lower())
            else:
                stringD2a(web_to_get.lower())
    except Exception:
        pass




# Locking and unlocking files.
def lock(file_path, enc_key, enc_salt):
    oCrypt().file_encrypt(file_path, enc_key, enc_salt)

def unlock(file_path2, enc_key2, enc_salt2):
    oCrypt().file_decrypt(file_path2, enc_key2, enc_salt2)



# Making new DB for the following functions for changing your encryption.
def make_db():
    database = sqlite3.connect('pwords2.pgen')
    c = database.cursor()
    c.execute('''CREATE TABLE pwd_tables(website text, passwd text, notes text)''')
    database.commit()
    database.close()


def change_creds():
    # Get list of domains/websites from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')
    

    # Get list of passwords from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables")
    words = c.fetchall()
    lpw = str(words).replace("(", "").replace(",)", "").replace("'", "")
    plist = lpw.strip('][').split(', ')

    # Get list of notes from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT notes FROM pwd_tables")
    notes = c.fetchall()
    ndb = str(notes).replace("(", "").replace(",)", "").replace("'", "")
    nlist = ndb.strip('][').split('*   ')


    # Get all of the passwords in the list above and decrypt them. (env.so)
    lst = []
    for y in plist:
        if not y:
            pass
        else:
            pwords = stringD_lst(y)
            lst.append(pwords)
    

    # Get all of the passwords in lst and encrypt them using the new credentials. (vne.py)
    lst2 = []
    for z in lst:
        if not z:
            pass
        else:
            vne_pwords = stringE2(z)
            lst2.append(vne_pwords)

    # Get all of the websites and all of the newly encrypted passwords and iterate through them both and then write to a new database file.
    for a,b,d in zip(dlist, lst2, nlist):
        database = sqlite3.connect('pwords2.pgen')
        c = database.cursor()
        c.execute(f"INSERT INTO pwd_tables VALUES ('{a}', '{b}', '{d}')")
        database.commit()
        database.close()
## ------------------------------------------------------------------------ ##




def main():
    try:
        #You can configure what you want to do in the config.json file.
        if j_load() == True:
            langs = ['upper', 'lower', 'nums', 'syms', 'kor', 'rus', 'chi', 'GU', 'GL', 'PL', 'PU', 'spec', 'block', 'a_box', 'hin', 'arab', 'emote', 'amha']

            # Choose multiple options from a list
            clear()
            print('Chose your options! (If no options are selected you will be returned back to the main menu.)\n"Space" to select & "Enter" to continue.\nPress "CTRL+C" to exit this menu.\n\n')
            langs_config = beaupy.select_multiple(langs, ticked_indices=[0,1,2,3], tick_style="#ed1dd3", cursor_style="#ffa533", tick_character="x")

            all = ""


            if langs[0] in langs_config:
                all += uppercase_letters

            if langs[1] in langs_config:
                all += lowercase_letters

            if langs[2] in langs_config:
                all += numbers

            if langs[3] in langs_config:
                all += symbols

            if langs[4] in langs_config:
                all += korean

            if langs[5] in langs_config:
                all += russian

            if langs[6] in langs_config:
                all += chinese

            if langs[7] in langs_config:
                all += greekU

            if langs[8] in langs_config:
                all += greekL

            if langs[9] in langs_config:
                all += portuL

            if langs[10] in langs_config:
                all += portuU

            if langs[11] in langs_config:
                all += unicode

            if langs[12] in langs_config:
                all += ascii_boxes

            if langs[13] in langs_config:
                all += ascii_draw_box

            if langs[14] in langs_config:
                all += hindi

            if langs[15] in langs_config:
                all += arabic

            if langs[16] in langs_config:
                all += emojis

            if langs[17] in langs_config:
                all += amharic

            if not langs_config:
                clear()
                return

        else:
            upper = True
            lower = True
            nums = True
            syms = True
            kor = True
            rus = True
            chi = True
            GU = True
            GL = True
            PL = True
            PU = True
            spec = True
            block = True
            a_box = True
            hin = True
            arab = True
            emote = True
            amha = True


            all = ""

            if upper:
                all += uppercase_letters
            if lower:
                all += lowercase_letters
            if nums:
                all += numbers
            if syms:
                all += symbols
            if kor:
                all += korean
            if rus:
                all += russian
            if chi:
                all += chinese
            if GU:
                all += greekU
            if GL:
                all += greekL
            if PL:
                all += portuL
            if PU:
                all += portuU
            if spec:
                all += unicode
            if block:
                all += ascii_boxes
            if a_box:
                all += ascii_draw_box
            if hin:
                all += hindi
            if arab:
                all += arabic
            if emote:
                all += emojis
            if amha:
                all += amharic
            
    except Exception as e:
        clear()
        print(f"Oops! Something went wrong...\nERROR: {e}\n\n")
        input('Press "enter" to continue...')
        clear()
        return


    clear()
    print('Note: Please make sure to write your password(s) down or save the password(s) into a new text file before running this script again.\nPress "q" to go back. \n\n')



    try:
        length = input('How long do you want your password(s)?: ')
        if length.lower() == 'q':
            clear()
            return None
        else:
            length = int(length)
    except Exception as e:
        clear()
        print(f'Oops..The value you gave me is not a number/integer.\n[Error]: {e}')
        input('\nPress "enter" to continue...')
        return None



    try:
        amount = input('How many do you want generated?: ')
        if amount.lower() == 'q':
            clear()
            return None
        else:
            amount = int(amount)
    except Exception as e:
        clear()
        print(f'Oops..The value you gave me is not a number/integer.\n[Error]: {e}')
        input('\nPress "enter" to continue...')
        return None



    print('\n')


    with open('pass.txt', 'w') as f:
        for _ in range(amount):
            password = ''.join(secrets.choice(all) for _ in range(length))
            print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
        print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n')
        input('Press "enter" to continue...')
        clear()


##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    if env.FLAG == '#src':
        alphabet = uppercase_letters + lowercase_letters + numbers + symbols + unicode
        print('The env file that is needed for passgen.py has not been set up yet. Setting up the file now!...\nMake sure to obfuscate and cythonize the env.py file after!')
        input('Press "Enter" to start!')
        clear()
        SALT = get_random_bytes(1024)
        PASS = ''.join(secrets.choice(alphabet) for _ in range(32))

        with open("env.py", "w") as f:
            f.write(f"SALT={SALT}\n")
            f.write(f'PASS="{PASS}"\n')
            f.write('FLAG="v1"')
            f.close()
        print("The env file should now be all set up!")
        input('Press "enter" to exit...')
        clear()
    else:
        while True:
            clear()
            try:
                option = int(input(f"{banner()}\n\nWhat would you like to do?\n\n1. Make a password?\n2. Get hash for a password?\n3. Manage passwords?\n4. Show pass.txt?\n5. Clear pass.txt?\n6. Quit?\n\nEnter: "))
            except Exception as e:
                clear()
                print(f'Value given is not an integer.\nError: {e}\n\n')
                input('Press "enter" to continue...')
                clear()
                continue


            if option == 1:
                clear()
                main()


            if option == 2:
                clear()
                pword = input('Press "q" to go back/quit.\n\nWhat would you like to hash?: ')
                if pword.lower() == 'q':
                    clear()
                else:
                    clear()
                    check = hash(pword)
                    if not check:
                        clear()
                        continue
                    else:
                        input('Press "enter" to continue...')
                        clear()


            if option == 3:
                clear()
                while True:
                    try:
                        sub_option = int(input(f"{banner()}\n\nWhat do you want to manage?\n\n1. Add password?\n2. Remove password?\n3. Show saved websites\n4. Lock database?\n5. Unlock database?\n6. Change encryption?\n7. Back?\n\nEnter: "))
                    except Exception as e:
                        clear()
                        print(f'Value given is not an integer.\nError: {e}\n\n')
                        input('Press "enter" to continue...')
                        clear()
                        continue


                    if sub_option == 1: # Add passwords
                        if os.path.isfile('pwords.pgen.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            web = input('Press "q" to go back/quit.\n\nWhat is the website/domain name you would like to store in the Database?: ')
                            if web.lower() == 'q':
                                clear()
                                continue
                            
                            passwd = input(f'Password to save for "{web.lower()}"?: ')
                            if passwd.lower() == 'q':
                                clear()
                                continue

                            notes = input("(Optional) - Additional Information/notes: ")   
                            if notes.lower() == 'q':
                                clear()
                                continue
                            clear()
                            add_data(web.lower(), passwd, notes)
                            input('\n\nPress "enter" to continue...')
                            clear()


                    if sub_option == 2: # Remove passwords
                        if os.path.isfile('pwords.pgen.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            domains()
                            if os.path.isfile('.lst'):
                                with open(".lst", "r+") as f:
                                    data = f.read()
                                    print(data)
                                    f.truncate(0)
                                    f.close()
                                os.remove(".lst")
                            
                                web_to_rmv = input('-----------------------------------------------------\n(This will remove notes and passwords for the website/domain as well)\nPress "q" to go back/quit.\n\nWhat is the website/domain name you would like to remove from the Database?: ')
                                clear()

                                if web_to_rmv.lower() == 'q':
                                    clear()
                                    continue
                                else:
                                    rmv_data(web_to_rmv.lower())
                                    input('\n\nPress "enter" to continue...')
                                    clear()
                            else:
                                input('Press "enter" to continue...')
                                clear()
                                continue


                    if sub_option == 3:
                        if os.path.isfile('pwords.pgen.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            data = read()
                            if data == 'q':
                                clear()
                            else:
                                input('\n\nPress "enter" to continue...')
                                clear()


                    if sub_option == 4:
                        if os.path.isfile('pwords.pgen.oCrypted'):
                            clear()
                            print("Database file already encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            print('Please provide credentials to lock the database. (Do NOT forget them as you will never be able to decrypt without them.)\nPress "q" to go back/quit.\n\n')
                            enc_key = input("Encryption Key?: ")
                            if enc_key.lower() == 'q':
                                clear()
                                continue

                            enc_salt = input("Encrytion Salt?: ")
                            if enc_salt.lower() == 'q':
                                clear()
                                continue

                            file_path = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                            if file_path.lower() == 'q':
                                clear()
                                continue
                            lock(file_path, enc_key, enc_salt)
                            clear()


                    if sub_option == 5:
                        clear()
                        print('Please provide the correct credentials to unlock the database. (Do not forget them as you will NOT be able to decrypt without them.)\nPress "q" to go back/quit.\n\n')

                        enc_key2 = input("Encryption Key?: ")
                        if enc_key2.lower() == 'q':
                            clear()
                            continue

                        enc_salt2 = input("Encrytion Salt?: ")
                        if enc_salt2.lower() == 'q':
                            clear()
                            continue

                        file_path2 = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                        if file_path2.lower() == 'q':
                            clear()
                            continue
                        unlock(file_path2, enc_key2, enc_salt2)
                        clear()



                    if sub_option == 6:
                        if os.path.isfile('pwords.pgen.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()

                            print("Changing encryption credentials for the passwords in the database...")
                            change()
                            check = input('New credentials genreated and saved as "vne.py".\n\nPress "enter" to continue or "q" to go back/quit...: ')
                            if check.lower() == 'q':
                                os.remove('vne.py')
                                clear()
                                continue
                            else:
                                clear()
                                print("Making new database for passwords...")
                                if os.path.isfile('pwords2.pgen'):
                                    print("Database already exists, deleting and trying again..")
                                    os.remove('pwords2.pgen')
                                    make_db()
                                else:
                                    make_db()
                                print("New database created!\n---------------------------------------------------------------")

                                print("\n\nWorking my magic!...")
                                change_creds()
                                input('Credentials have been changed and all data is now usung the new encryption & credentials.\n\nPress "enter" to continue...')
                                clear()

                                print("Cleaning up!...\n")
                                cleanup()
                                input('\n\nFiles have been cleaned up!\nPress "enter" to quit/reload the passgen...')
                                clear()
                                quit()


                    if sub_option == 7:
                        break


                    elif sub_option < 1 or sub_option > 7:
                        clear()
                        print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                        input('Press "enter" to quit...')
                        clear()
                        
            
            if option == 4:
                passwords = show_pass()
                if not passwords:
                    clear()
                    print('No passwords found in "pass.txt"\n\n')
                    input('Press "enter" to continue...')
                    clear()
                else:
                    print(passwords)
                    input('Press "enter" to continue...')
                    clear()
            

            if option == 5:
                clr_pass()
                print("pass.txt has been wiped clean.\n\n")
                input('Press "enter" to continue...')
                clear()
            
            
            if option == 6:
                clear()
                exit("Goodbye! <3")

            
            elif option < 1 or option > 6:
                clear()
                print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                input('Press "enter" to continue...')
                clear()
                
