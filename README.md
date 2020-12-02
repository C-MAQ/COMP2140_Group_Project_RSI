# COMP2140_Group_Project_RSI

Code for Interpretation Module Prototype

## System Architecture
![architecture diagram](https://i.imgur.com/6InkB4e.png)

## Component Decompsition of Interpretation Module
![class diagram](https://i.imgur.com/jc1jUZS.png)

## Design Notes
The Interpretation Module uses three distinct classes to display different user interfaces for each category of user. The SetUpUI class is used by the meeting host to set the parameters for interpretation before the meeting is started. The InterpreterUI and AttendeeUI classes are used to display interfaces for interpreters and attendees respectively. The dashboard() method presents all options available to an interpreter while actively interpreting. When fully implemented, the AttendeeUI class will also have its own dashboard() method that will have different options than that of an interpreter. All the UI classes call on methods from the InterpretationManager class which operates centrally at the logic layer. Interpreters and attendees are both types of meeting participants and this relationship is captured by making Interpreter and Attendee subclasses of the MeetingParticipant class. These subclasses contain attributes and methods specific to each type of user. Persistence of module settings and data is handled by the Database class.

## Future Development:
Integration with Jitsi Meet meeting server for full remote interpreting functionality.
