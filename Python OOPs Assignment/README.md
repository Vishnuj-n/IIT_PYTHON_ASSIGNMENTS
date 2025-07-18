# IIT_PYTHON_ASSIGNMENTS

**Assignment Date:** 11 May, 2025 at 6:00 AM  
**Deadline:** Concludes on 13 May, 2025

1. Library Access System
Problem Statement: You are tasked with developing a simplified library access system. A base class Member holds the basic member information like name and membership ID. A subclass StudentMember allows book checkouts and displays the number of books currently borrowed. Implement necessary methods to add a book, return a book, and display borrowing status.

2. Drone Fleet Management
Problem Statement: Design a system to manage a fleet of drones. A class Device has basic device info. A class Flyer has the method fly() to simulate drone flying. A third class Drone inherits from both Device and Flyer, and includes additional drone-specific actions like capture_image(). Create an object of Drone and demonstrate all functionalities ensuring no conflict arises between inherited methods.

3. Online Learning Platform
Problem Statement: Build a class hierarchy for an online learning platform. The base class User includes name and email. The subclass Instructor adds subject expertise and a method to upload content. A third class CourseCreator (inherits from Instructor) allows creation of complete courses with modules. Override the display_info() method at each level to reflect role-specific details.

4. Smart Home Appliance
Problem Statement: You are developing a system to control smart appliances. Create a base class Appliance with a method status() that prints a default message. Subclasses like Fan, Light, and AC override this method to give device-specific status updates. Store all devices in a list and iterate through it, invoking the status() method to demonstrate polymorphism.

5. Geometry Toolkit
Problem Statement: Develop a class ShapeCalculator to calculate areas. If one argument is passed, treat it as a circle radius and calculate the area. If two arguments are passed, treat them as length and width of a rectangle. Implement a single method area() with default parameters to simulate overloading. Ensure it returns appropriate outputs in each case.