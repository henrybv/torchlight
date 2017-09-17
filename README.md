# Torchlight

## Product demo video: https://www.screencast.com/t/z7PX1CRG 

**Torchlight brings relief, assistance, transparency & efficiency to those most affected after a catastrophic disaster**

Devpost: https://devpost.com/software/torchlight

## Inspiration

September 2017 saw two devastating natural disasters hit Florida and Texas.

Hurricane Harvey displaced more than [30,000 people from their homes](https://www.washingtonpost.com/national/thousands-pile-into-makeshift-shelters-big-and-small-across-texas/2017/08/28/01d3216a-8c0c-11e7-91d5-ab4e4bb76a3a_story.html).

Hurricane Irma had [200,000 Floridians housed in shelters](https://www.cnbc.com/2017/09/11/hurricane-irma-continues-to-pound-florida-extent-of-damage-not-yet-clear.html), with 6.5mil ordered to evacuate.

For many of these victims, their homes have been severely damaged or destroyed by deadly winds and astonishing floodwater, and may need shelter for weeks or months to come.

Currently organizations such as Red Cross have resources for victims to [http://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter](find a shelter) or seek evacuation assistance, but there is little transparency of communication between:

* To victims about the status of a shelter
* To friends and family of victims to know where the location and status of their struggling friend
* Dispatchment of resources to these shelters

Large-impact, devastating hurricanes, earthquakes, and other natural disasters happen every year, leaving chaos, broken homes, and heartbreak in their wake. 

Team Torchlight is building an open-sourced tool for emergency shelter organizers, natural disaster victims, and the wider public to find help, distribute resources, and check in on the wellbeing of their loved ones.

The mission of Torchlight is to bring transparency, assistance, and efficiency to those most affected after a catastrophic event. We allow victims to find open shelters around them, resources to be allocated to the most-in-need shelters, give peace of mind to friends and family of victims, and a way for shelters to manage their inventory and evacuees.  

## Who is it for?

### 1. Shelter organizers

As a shelter organizer,
I’d like to categorize and track my inventory and the evacuees at my location,
So I can ensure that our resources are well managed and no-one is left behind. 

As a shelter organizer,
I’d like to be able to receive resources in areas that we are most deficient, and be able to share resources we have abundance with other shelters that need more help,
So we can ensure that resources are distributed in the most efficient manner across all shelters in the region.  

### 2. Friends and family of victims

As a friend of a victim of a natural disaster who has been difficult to contact,
I want to know where they are, or be notified when they check into a safe shelter,
So I can have peace of mind that they are safe, and know where and how to reach them or offer help.  

As a friend of a victim who has checked into a shelter,
I want to be able to see their live video stream in their shelter,
So I can have peace of mind that they are safe, and know where and how to reach them or offer help.  

### 3. Victims looking for shelter

As a victim of a natural disaster,
I want to notify my emergency contacts that I have checked into a shelter,
So they will know my safety status, my location, and have a method to contact me.

As a victim of a natural disaster,
I want to find all the local shelters around me with their availability status,
So I can take my family to a shelter that is local and won't turn us away.  

## What it does

### For victims and shelter evacuees: 
* Check into a shelter
* Send a safety alert your emergency contacts upon check in to a shelter
* Find the nearest available shelters and review their resource inventory  
* View a live stream of their shelters 

### For friends and family of evacuees: 
* Check the status of a registered shelter evacuee
* Receive a text message alert when a registered missing person has checked into a shelter 
* See a live feed of a shelter 

### For shelter administrators:
* Maintain a registry of your shelter’s evacuees
* Maintain an inventory of your shelter’s resources
* Be alerted to low supplies in your shelter’s resources
* Send a resource request publicly for most-needed resources
* Track the delivery of requested resources from the public 

## How we built it

* Django for the web infrastructure 
* Javascript for the map interface and interactivity 
* Heroku for live video hosting
* HTML/CSS for web interface
* APIs and Challenges (TechCrunch Sponsors)
  * Nexmo SMS API for text messages
  * Intuit Small Business API for inventory management
  * MapQuest API for map visualizations
  * Agora API for live video streams
  * Accenture Social Impact Challenge for inspiration for this project

## What's next for Torchlight

* We would like to make this project open sourced 
* Test the interface and use cases in front of shelter organizers
* Any inquries please contact [us here](mailto:hello@jadenator)

## Team

* [John Jascovski](https://github.com/elejaski)
* [Henry Bao-Viet Nguyen](https://github.com/henrybv)
* [Jonathan Mah](https://github.com/jmah)
* [Jade Feng](https://github.com/jadefeng)
* [Sean Bell](https://github.com/seanbell)



