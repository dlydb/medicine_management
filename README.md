# Medicine Management
The objective of the Medicine Management is to develop a functional prototype for a product that helps senior citizens better adhere to their medication regimen. This product consists of an automatic pill dispenser and an easy-to-use GUI with a calendar function for managing medication schedules. This schedule will be able to include both pill and non-pill medications. 

Please check out the [final presentation](https://drive.google.com/file/d/1fzquxMiW0EZOune0G8FMk1LTMdDHwbn5/view?usp=sharing).

Also here is our final product.

![product](https://github.com/dlydb/medicine_management/blob/master/final_product.jpg)

One of the other major components of the device is its touch screen interface, and accompanying application with which the user will interact. The application is a local web server hosted on a Raspberry Pi. The common Python web development framework, Django is implemented. Python was chosen due to its wide range of applications, allowing all components of the design to be integrated easily. Django allows web pages using conventional HTML and CSS styling to be served to a screen or touch screen device. The Django Application will include a variety of features. The main application includes a sidebar, colloquially referred to as a ‘navbar’, which includes links to all relevant web pages in the application. These pages include the following: Home, Calendar, My Pills, and Login. 

Example of login screen:

![login](https://github.com/dlydb/medicine_management/blob/master/Image/login.png)

Example of edit scren:

![edit](https://github.com/dlydb/medicine_management/blob/master/Image/edit.png)

Example of schedule screen:

![schedule](https://github.com/dlydb/medicine_management/blob/master/Image/schedule.png)

Example of different calendars:

![cal1](https://github.com/dlydb/medicine_management/blob/master/Image/cal1.png)
![cal2](https://github.com/dlydb/medicine_management/blob/master/Image/cal2.png)
![cal3](https://github.com/dlydb/medicine_management/blob/master/Image/cal3.png)

Another feature of backend is the functional database. To satisfy the memory usage for storing medication names and schedule for the user. A database is integrated into the system to support functions and provide backend information to the user interface. To satisfy the offline design of the product, the database is designed using a local server to store the data for different medications and schedules. The Web server is finally integrated with SQLite3 based on the overall consideration for functionality and easy to integrate. 

![data](https://github.com/dlydb/medicine_management/blob/master/Image/data.JPG)
