# Labconco_data_pro
The python file is a simple script to process the data from the Labconco Stoppering Tray Dryer. Simply enter the location of the data, and the script will process the information and plot the graph. Also included in this document are the instructions for setting up, recording and retrieving the data from the instrument, please see below.

Section I, Freeze drying the samples and stoppering the vails
Purpose:
To provide instructions on how to operate the Labconco Stoppering Tray Dryer for lyophilizing samples, e.g., the drug product.

Procedure:
Freezing the samples
	•	Make sure the lyophilizer (bottom unit) is turned off, to prevent the vacuum pump from engaging during the   freezing process.
	•	Turn on the main power switch for the Stoppering Tray Dryer (top unit)
	•	Make sure the Run option for the top unit is off
	  •	If it is on, press “Run/Stop”
	•	To select the run cycle
	  •	Click “Display” and cycle to “Auto”
	•	In the display panel, select the appropriate program (e.g., P1) by pressing the up or down buttons under   “Program”
	•	Press “Enter” to select the segment for the program (e.g., S1), press the up or down buttons to select the     segment number and view/edit the lyophilization parameter for the given segment step
	•	Press “Run/Stop” button to start the run (i.e., a green light indicates that the unit is on, and the Display       will automatically switch to “Monitor”).
To Dry the samples and engage the vacuum
	•	Once the samples are frozen, Stop the run for the Stoppering Tray Dryer by pressing the “Run/Stop” button
	•	To select the run cycle
	  •	Click “Display” and cycle to “Auto”
	  •	In the display panel, select the appropriate program (e.g., P5) by pressing the up or down buttons under     “Program”
	  •	Press “Enter” to select the segment for the program (e.g., S1), press the up or down buttons to select the         segment number and view/edit the lyophilization parameter for the given segment step
	  •	Press “Run/Stop” button to start the run (i.e., a green light indicates that the unit is on, and the Display         will automatically switch to “Monitor”.

Stoppering the vials
	•	Reduce the pressure of the Stoppering Tray Dryer to approximately 1 torr
	•	 This is done by changing the vacuum pressure settings in the Lyophilizer (i.e., the bottom unit).
	•	Press “menu” until the pressure menu is displayed, and then press “Select” to change the pressure value.
	•	Back fill the chamber with nitrogen (Turn valve counter clockwise) for a minute
	•	Turn off the vacuum
	•	To stopper the samples, for the top unit, turn the “Raise” (left) knob counter clockwise
	•	Turn off the nitrogen gas (i.e., turn the valve clockwise), once the vails are stoppered
	•	Break the vacuum to allow the air to enter the unit, by turning the “Open” (right) knob counter clockwise.
	•	Turn off the main power to both bottom and top units

Section II, Recording and retrieving the phyiscal parameters from the Stoppering Tray Dryer
Purpose:
This section pertains to the recording of the data (i.e., time, temperature and pressure) from the Labconco Stoppering Tray Dryer, which can be saved to a local PC by using the RS232 Receptacle.

Procedure:
To monitor the temperature of the Stoppering Tray Dryer, a cable is connected to the RS232 receptacle on the rear side of the unit.
RS232 receptacle

Connection of the computer interface to the Labconco Freeze Dry System:
Computers with a 25-pin D-sub male serial connector should use Connect Cable, Labconco part number 7537801,
Computers with a 9-pin D-sub male serial connector should use Connect Cable, Labconco part number 7537800

The RS232 interface sends data to a data logging computer to monitor the state and activity of the Freeze Dry System. This data is half duplex data. The data properties are as follows:
1. Data Rate 2400 Baud 
2. 8 Bit word length 
3. 1 Start bit, 1 Stop bit 
4. No parity is transmitted 
5. Standard ASCII character set

Setup for the Connect Cable:
  Connect the RJ12 cable (i.e., fax/modem plug) to the RS232 receptacle, and the female DB25 cable is connected to an     adapter, which connects to the male DB09 port of the PC.
  Male DB09 port for connect-ing to the Connect Cable
  Male DB09 port for connect-ing to the Connect Cable
             
Hyper Terminal Setup:
  Create a new connection (if not done so already)
  In the ‘Connection Description’ dialog box, name the connection, and click OK


To set up the COM properties:
  Select Connect To dialog box
  Select COM port# from Connect using box (either COM1 or COM2)
  Click OK

  Click on ‘COM properties’, and set the communication parameters
	1) Data Rate 2400 Baud 
    	2) 8 Bit word length 
    	3) 1 Start bit, 1 Stop bit 
    	4) no flow control
	Click OK

 To capture the data and save it to the hard drive
	Click on ‘Transfer’, and then ‘Capture Text’
	A ‘Capture Tex’ dialog box will appear (note transmission of data is every 10 sec)
To save the data select the folder and name of the file
Click ‘Start’ and the word ‘Capture’ will appear at the bottom of the HyperTerminal window that capture is enabled
