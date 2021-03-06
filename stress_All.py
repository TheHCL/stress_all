import os
import sys
import time
import pyautogui as p
locate = os.getcwd() #get current directory
device_compare = locate+"/Device_Compare_v1.0.1.4"
pwrtest = locate+"/Pwrtest_RS6_18362(For RS6)"
warmboot = locate +"/warmboot v2.0"
coldboot = locate +"/coldboot_2.0"
STPM = locate+"/STPM_V2.5.1.0(Build_01021743)"
STPM_ini = STPM+"/ITPM_DriverUpdate_20190313"
plan = STPM+"/PLAN"


run_mode = input("Please Enter Run mode (S3/S4/WB/CB) :")
amd = input("SUT is AMD platform?(y/n):")
amd = amd.lower()
run_mode = run_mode.lower() # change str to lower case

def dc_init(run_mode):
	os.chdir(device_compare)
	dits = dict(s3="70",s4="70",wb="90",cb="90")	
	file_delay_time = open("DelayTime.txt","w")
	file_delay_time.write(dits[run_mode])
	file_delay_time.close()
	print("Delay time update!")


def event_log_clean():
	os.chdir(locate)
	os.system("clear_log.cmd")
	print("event log has been deleted.")

def dc_compare():
	#file_delay_time.close()
	os.startfile("DeviceCompare.exe")
	time.sleep(5)
	os.chdir(locate)
	dc_reset = p.locateCenterOnScreen("pic/DC/dc_reset.PNG",confidence = 0.8)
	p.click(dc_reset)
	time.sleep(1)
	dc_stop_on_fail_checked = p.locateCenterOnScreen("pic/DC/dc_stop_on_fail_checked.PNG")
	if dc_stop_on_fail_checked is None:
		dc_stop_on_fail = p.locateCenterOnScreen("pic/DC/dc_stop_on_fail.PNG",confidence = 0.8)
		p.click(dc_stop_on_fail)
	time.sleep(1)
	dc_sync = p.locateCenterOnScreen("pic/DC/dc_sync.PNG",confidence = 0.8)
	p.click(dc_sync)
	time.sleep(5)
	dc_start = p.locateCenterOnScreen("pic/DC/dc_start.PNG",confidence = 0.8)
	p.click(dc_start)
	time.sleep(1)
def dc_compare_4k():
	os.startfile("DeviceCompare.exe")
	time.sleep(5)
	os.chdir(locate)
	dc_reset = p.locateCenterOnScreen("pic/DC/dc_reset_4k.PNG",confidence = 0.8)
	p.click(dc_reset)
	time.sleep(1)
	dc_stop_on_fail_checked = p.locateCenterOnScreen("pic/DC/dc_stop_on_fail_checked_4k.PNG")
	if dc_stop_on_fail_checked is None:
		dc_stop_on_fail = p.locateCenterOnScreen("pic/DC/dc_stop_on_fail_4k.PNG",confidence = 0.8)
		p.click(dc_stop_on_fail)
	time.sleep(1)
	dc_sync = p.locateCenterOnScreen("pic/DC/dc_sync_4k.PNG",confidence = 0.8)
	p.click(dc_sync)
	time.sleep(5)
	dc_start = p.locateCenterOnScreen("pic/DC/dc_start_4k.PNG",confidence = 0.8)
	p.click(dc_start)
	time.sleep(1)


def s3_bat():
	os.chdir(pwrtest)
	file_s3 = open("S3.bat","w")
	file_s3.write("pwrtest /sleep /s:3 /c:250 /d:90 /P:120")
	file_s3.close()
	os.system("S3.bat")

def s4_bat():
	os.chdir(pwrtest)
	file_s4 = open("S4.bat","w")
	file_s4.write("pwrtest /sleep /s:4 /c:250 /d:90 /P:180")
	file_s4.close()
	os.system("S4.bat")

def warmboot_bat():
	os.chdir(warmboot)
	os.system("warmboot.bat")

def coldboot_bat():
	os.chdir(coldboot)
	os.system("coldboot.bat")


def Full_HD():
	os.chdir(STPM_ini)
	driver_update_bool = os.path.exists("exist.txt")
	if driver_update_bool == False:
		filebool = open("exist.txt","w")
		filebool.write("1")
		filebool.close()
		os.system("disableUAC.BAT")
		os.startfile("ITPM_DriverUpdate.exe")
		time.sleep(3)
		os.chdir(locate)
		ITPM_update = p.locateCenterOnScreen("pic/ITPM_update.PNG",confidence = 0.8)
		p.click(ITPM_update)
		time.sleep(1)
		ITPM_OK = p.locateCenterOnScreen("pic/ITPM_OK.PNG",confidence = 0.8)
		p.click(ITPM_OK)
		time.sleep(1)
		ITPM_exit = p.locateCenterOnScreen("pic/ITPM_exit.PNG",confidence = 0.8)
		p.click(ITPM_exit)

	os.chdir(plan)
	plan_bool = os.path.exists("STPM_TESTPLAN.PLN")

	if plan_bool == True:
		os.remove("STPM_TESTPLAN.PLN")
		flag = "1"
		print("file delted")
	else:
		flag ="0"

	os.chdir(STPM)
	os.startfile("STPM.exe")
	time.sleep(5)
	os.chdir(locate)
#===============================================#
#====stpm_running?==============================#
	stpm_cancel = p.locateCenterOnScreen("pic/stpm_cancel.PNG",confidence = 0.8)
	p.click(stpm_cancel,clicks = 3)
	time.sleep(2)
	stpm_terminate = p.locateCenterOnScreen("pic/stpm_terminate.PNG",confidence = 0.8)
	p.click(stpm_terminate)
	time.sleep(2)
	stpm_reset = p.locateCenterOnScreen("pic/stpm_reset.PNG",confidence = 0.7)
	p.click(stpm_reset)
	time.sleep(2)

#====stpm_stid press=======
	stpm_stid = p.locateCenterOnScreen("pic/stpm_stid.PNG",confidence = 0.5)
	p.keyDown("ctrl")
	p.keyDown("alt")
	p.click(stpm_stid)
	p.keyUp("alt")
	p.keyUp("ctrl")
	time.sleep(5)
#=====stpm_setup press=======
	stpm_setup = p.locateCenterOnScreen("pic/stpm_setup.PNG",confidence = 0.5)
	p.click(stpm_setup)
	time.sleep(1)
#=====stpm_scanAll============
	if flag == "0":
		stpm_scan_all = p.locateCenterOnScreen("pic/stpm_scan_all.PNG",confidence = 0.8)
		p.click(stpm_scan_all)
		time.sleep(1)
#=====stpm_check_both
		stpm_check_both = p.locateCenterOnScreen("pic/stpm_check_both.PNG",confidence = 0.9)
		p.click(stpm_check_both)
		time.sleep(1)
#=====stpm_check_device
		stpm_check_device = p.locateCenterOnScreen("pic/stpm_check_device.PNG",confidence = 0.8)
		p.click(stpm_check_device)
		time.sleep(1)
		stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
		time.sleep(2)
		if stpm_alert is not None:
			p.click(stpm_alert)
	
		time.sleep(1)
#=====stpm_auto_run
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)

#=====stpm_edit_plan
	stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan.PNG",confidence = 0.9)
	p.click(stpm_edit_plan)
	time.sleep(1)
#=====stpm_test_item===============================
	stpm_test_item = p.locateCenterOnScreen("pic/stpm_test_item.PNG",confidence = 0.9)
	p.click(stpm_test_item)
	time.sleep(2)
	if flag =="1":
		stpm_test_item_wb = p.locateCenterOnScreen("pic/stpm_test_item_wb.PNG",confidence = 0.9)
		p.click(stpm_test_item_wb)
		time.sleep(2)
#=====stpm_coldboot
	stpm_coldboot = p.locateCenterOnScreen("pic/stpm_coldboot.PNG",confidence = 0.8)
	p.click(stpm_coldboot)
	time.sleep(1)
#======stpm_count_down
	stpm_count_down = p.locateCenterOnScreen("pic/stpm_count_down.PNG",confidence = 0.8)
	p.click(stpm_count_down)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_count_down_time,interval=0.5)
#=======stpm_sleep_time
	stpm_sleep_time = p.locateCenterOnScreen("pic/stpm_sleep_time.PNG",confidence = 0.8)
	p.click(stpm_sleep_time)
	time.sleep(1)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_sleep_time,interval=0.5)
#========stpm_execute_count
	stpm_execute_count = p.locateCenterOnScreen("pic/stpm_execute_count.PNG",confidence = 0.8)
	p.click(stpm_execute_count)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_cycles,interval=0.5)
#========stpm_add_new_group
	stpm_add_new_group = p.locateCenterOnScreen("pic/stpm_add_new_group.PNG",confidence = 0.8)
	p.click(stpm_add_new_group)
	time.sleep(1)
#========stpm_save_default_plan
	stpm_save_default_plan = p.locateCenterOnScreen("pic/stpm_save_default_plan.PNG",confidence = 0.8)
	p.click(stpm_save_default_plan)
	time.sleep(1)
#=========stpm_savenexit
	if flag =="1":
		stpm_setup = p.locateCenterOnScreen("pic/stpm_setup.PNG",confidence = 0.5)
		p.click(stpm_setup)
		time.sleep(1)
		stpm_autorun_checked = p.locateCenterOnScreen("pic/stpm_autorun_checked.PNG",confidence = 0.9)
		p.click(stpm_autorun_checked)
		time.sleep(1)
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)
		stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan.PNG",confidence = 0.9)
		p.click(stpm_edit_plan)
		time.sleep(1)

	stpm_savenexit = p.locateCenterOnScreen("pic/stpm_savenexit.PNG",confidence = 0.8)
	p.click(stpm_savenexit)
	time.sleep(1)

	end_time = time.time()

	print("Time eplased :",end_time- start_time)



def Four_K():
	os.chdir(STPM_ini)
	driver_update_bool = os.path.exists("exist.txt")
	if driver_update_bool == False:
		filebool = open("exist.txt","w")
		filebool.write("1")
		filebool.close()
		os.system("disableUAC.BAT")
		os.startfile("ITPM_DriverUpdate.exe")
		time.sleep(3)
		os.chdir(locate)
		ITPM_update = p.locateCenterOnScreen("pic/ITPM_update_4k.PNG",confidence = 0.8)
		p.click(ITPM_update)
		time.sleep(1)
		ITPM_OK = p.locateCenterOnScreen("pic/ITPM_OK_4k.PNG",confidence = 0.8)
		p.click(ITPM_OK)
		time.sleep(1)
		ITPM_exit = p.locateCenterOnScreen("pic/ITPM_exit_4k.PNG",confidence = 0.8)
		p.click(ITPM_exit)

	os.chdir(plan)
	plan_bool = os.path.exists("STPM_TESTPLAN.PLN")

	if plan_bool == True:
		os.remove("STPM_TESTPLAN.PLN")
		flag = "1"
		print("file delted")
	else:
		flag ="0"

	os.chdir(STPM)
	os.startfile("STPM.exe")
	time.sleep(5)
	os.chdir(locate)
#===============================================#
#====stpm_running?==============================#
	stpm_cancel = p.locateCenterOnScreen("pic/stpm_cancel_4k.PNG",confidence = 0.8)
	p.click(stpm_cancel,clicks = 3)
	time.sleep(2)
	stpm_terminate = p.locateCenterOnScreen("pic/stpm_terminate_4k.PNG",confidence = 0.8)
	p.click(stpm_terminate)
	time.sleep(2)
	stpm_reset = p.locateCenterOnScreen("pic/stpm_reset_4k.PNG",confidence = 0.7)
	p.click(stpm_reset)
	time.sleep(2)

#====stpm_stid press=======
	stpm_stid = p.locateCenterOnScreen("pic/stpm_stid_4k.PNG",confidence = 0.5)
	p.keyDown("ctrl")
	p.keyDown("alt")
	p.click(stpm_stid)
	p.keyUp("alt")
	p.keyUp("ctrl")
	time.sleep(5)
#=====stpm_setup press=======
	stpm_setup = p.locateCenterOnScreen("pic/stpm_setup_4k.PNG",confidence = 0.5)
	p.click(stpm_setup)
	time.sleep(1)
#=====stpm_scanAll============
	if flag == "0":
		stpm_scan_all = p.locateCenterOnScreen("pic/stpm_scan_all_4k.PNG",confidence = 0.8)
		p.click(stpm_scan_all)
		time.sleep(1)
#=====stpm_check_both
		stpm_check_both = p.locateCenterOnScreen("pic/stpm_check_both_4k.PNG",confidence = 0.9)
		p.click(stpm_check_both)
		time.sleep(1)
#=====stpm_check_device
		stpm_check_device = p.locateCenterOnScreen("pic/stpm_check_device_4k.PNG",confidence = 0.9)
		p.click(stpm_check_device)
		time.sleep(1)
		stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
		time.sleep(2)
		if stpm_alert is not None:
			p.click(stpm_alert)
	
		time.sleep(1)
#=====stpm_auto_run
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)

#=====stpm_edit_plan
	stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan_4k.PNG",confidence = 0.9)
	p.click(stpm_edit_plan)
	time.sleep(1)
#=====stpm_test_item===============================
	stpm_test_item = p.locateCenterOnScreen("pic/stpm_test_item_4k.PNG",confidence = 0.9)
	p.click(stpm_test_item)
	time.sleep(2)
	if flag =="1":
		stpm_test_item_wb = p.locateCenterOnScreen("pic/stpm_test_item_wb_4k.PNG",confidence = 0.9)
		p.click(stpm_test_item_wb)
		time.sleep(2)
#=====stpm_coldboot
	stpm_coldboot = p.locateCenterOnScreen("pic/stpm_coldboot_4k.PNG",confidence = 0.8)
	p.click(stpm_coldboot)
	time.sleep(1)
#======stpm_count_down
	stpm_count_down = p.locateCenterOnScreen("pic/stpm_count_down_4k.PNG",confidence = 0.8)
	p.click(stpm_count_down)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_count_down_time,interval=0.5)
#=======stpm_sleep_time
	stpm_sleep_time = p.locateCenterOnScreen("pic/stpm_sleep_time_4k.PNG",confidence = 0.8)
	p.click(stpm_sleep_time)
	time.sleep(1)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_sleep_time,interval=0.5)
#========stpm_execute_count
	stpm_execute_count = p.locateCenterOnScreen("pic/stpm_execute_count_4k.PNG",confidence = 0.8)
	p.click(stpm_execute_count)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_cycles,interval=0.5)
#========stpm_add_new_group
	stpm_add_new_group = p.locateCenterOnScreen("pic/stpm_add_new_group_4k.PNG",confidence = 0.8)
	p.click(stpm_add_new_group)
	time.sleep(1)
#========stpm_save_default_plan
	stpm_save_default_plan = p.locateCenterOnScreen("pic/stpm_save_default_plan_4k.PNG",confidence = 0.8)
	p.click(stpm_save_default_plan)
	time.sleep(1)
#=========stpm_savenexit
	if flag =="1":
		stpm_setup = p.locateCenterOnScreen("pic/stpm_setup_4k.PNG",confidence = 0.5)
		p.click(stpm_setup)
		time.sleep(1)
		stpm_autorun_checked = p.locateCenterOnScreen("pic/stpm_autorun_checked_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun_checked)
		time.sleep(1)
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)
		stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan_4k.PNG",confidence = 0.9)
		p.click(stpm_edit_plan)
		time.sleep(1)

	stpm_savenexit = p.locateCenterOnScreen("pic/stpm_savenexit_4k.PNG",confidence = 0.8)
	p.click(stpm_savenexit)
	time.sleep(1)
	


screen = p.size()
	
if run_mode =="s3":
	dc_init(run_mode)
	if screen == (1920,1080):
		dc_compare()
	if screen == (3840,2160):
		dc_compare_4k()
	
	s3_bat()
if run_mode =="s4":
	dc_init(run_mode)
	if screen == (1920,1080):
		dc_compare()
	if screen == (3840,2160):
		dc_compare_4k()
	s4_bat()
	
if run_mode == "wb":
	dc_init(run_mode)
	if screen == (1920,1080):
		dc_compare()
	if screen == (3840,2160):
		dc_compare_4k()
	warmboot_bat()

if run_mode == "cb":
	if amd =="y":
		count_down_time=input("Count Down time before test : ")
		sleep_time=input("Sleep & suspend time : ")
		cycles =input("Cycles : ")

		in_count_down_time=[]
		in_sleep_time=[]
		in_cycles=[]
		for i in count_down_time:
			in_count_down_time.append(i)
		for j in sleep_time:
			in_sleep_time.append(j)
		for k in cycles:
			in_cycles.append(k)
		in_sleep_time.insert(1,"del")
		os.system("mode con cols=80 lines=20")



		if screen == (1920,1080):
			Full_HD()
		if screen == (3840,2160):
			Four_K()
	if amd =="n":
		dc_init(run_mode)
		if screen == (1920,1080):
			dc_compare()
		if screen == (3840,2160):
			dc_compare_4k()
		coldboot_bat()










